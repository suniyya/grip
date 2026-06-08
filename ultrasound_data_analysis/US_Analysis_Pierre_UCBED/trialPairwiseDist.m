function [distMatrix,labelVect,graspNames,fullTrialInfo] = trialPairwiseDist(frameTbl,distMeasure)

if isempty(gcp('nocreate'))
    ppool = parpool(6);
    %     nWorkers = ppool.NumWorkers;
else
    ppool = gcp('nocreate');
    %     nWorkers = ppool.NumWorkers;
end

% dq = parallel.pool.DataQueue;
% wb = waitbar(0,'Waiting on Pairwise Dist...');

fullTrialInfo = [];
labelVect = [];
% nGrasps = length(fn);
% nReps = size(frameTbl,1);
graspNames = frameTbl.Properties.VariableNames;
frameCells = table2cell(frameTbl);
if ismatrix(frameCells{1})
    
    nPairs = numel(frameCells);
    
    labelVect = nan(nPairs,1);
    distMatrix = nan(nPairs);

    % wb.UserData = [0,nPairs];
    % afterEach(dq,@(varargin) iIncrementWaitbar(wb))
    % afterEach(dq,@(idx) fprintf('Completed iteration '))
    for a = 1:nPairs
        tempRep = frameCells{a};
        if ~isempty(tempRep)&&~all(isnan(tempRep),'all')
            %parfor
            parfor b = 1:nPairs
                if ~isempty(frameCells{b})&&~all(isnan(frameCells{b}),'all')
                    if strcmp(distMeasure,'corr')||strcmp(distMeasure,'Pearson')
                        distMatrix(a,b) = 1-corr2(tempRep,frameCells{b});
                    elseif strcmp(distMeasure,'euclidean')
                        distMatrix(a,b) = norm(tempRep-frameCells{b});
                    elseif strcmpi(distMeasure,'sqrtPearson')
                        distMatrix(a,b) = sqrt(1-corr2(tempRep,frameCells{b}));
                    else
                        badDistText = 'UNKNOWN DISSIMILARITY MEASURE';
                        err(badDistText)
                    end
                end
                % send(dq,b)
            end
        end
        [~,labelVect(a)] = ind2sub(size(frameTbl),a);
    end


elseif ndims(frameCells{1})==3

    nTrials = size(frameTbl,1);
    nGrasps = size(frameTbl,2);
    
    nFrames = max(cellfun(@(x) size(x,3),frameCells),[],'all');
    nFramePairsGuess = nFrames*nTrials*nGrasps;
    
    labelVect = zeros(nFramePairsGuess,1);
    tLabel = zeros(nFramePairsGuess,1);
    fSyncInd = repmat(1:nFrames,1,nGrasps*nTrials)';
    
    nFF = 1;
    fprintf('\nStarting Frame by Frame Extraction and Time Sync\n')
    gTimer = tic;
    for gg = 1:nGrasps
        for tt = 1:nTrials
            if ~isempty(frameCells{tt,gg})
                fullTrialsUI8(:,:,nFF:nFF+size(frameCells{tt,gg},3)-1) = uint8(frameCells{tt,gg});
                labelVect(nFF:nFF+size(frameCells{tt,gg},3)-1) = gg;
                tLabel(nFF:nFF+size(frameCells{tt,gg},3)-1) = tt;
                nFF = nFF+size(frameCells{tt,gg},3);
            end
        end
        fprintf('\n%02d out of %02d Complete \n',gg,nGrasps)
        toc(gTimer)
    end
    % labelVect(labelVect==0)
    nFramePairs = size(fullTrialsUI8,3);
    distMatrix = zeros(nFramePairs);
    TimeIndCheck = ceil(nFramePairs/10);

    % wb.UserData = [0,nFramePairs];
    % afterEach(dq,@(varargin) iIncrementWaitbar(wb))

    fprintf('\n Starting Pairwise distance calculation\n')
    fpTimer = tic;
    for a = 1:nFramePairs
        f1 = double(fullTrialsUI8(:,:,a));
        %parfor

        parfor b = 1:nFramePairs
            if strcmpi(distMeasure,'corr')||strcmp(distMeasure,'Pearson')
                distMatrix(a,b) = 1-corr2(f1,double(fullTrialsUI8(:,:,b)));
            elseif strcmpi(distMeasure,'euclidean')
                norm(f1-double(fullTrialsUI8(:,:,b)));
            elseif strcmpi(distMeasure,'sqrtPearson')
                distMatrix(a,b) = sqrt(1-corr2(f1,double(fullTrialsUI8(:,:,b))));
            else
                badDistText = 'UNKNOWN DISSIMILARITY MEASURE';
                err(badDistText)
            end
        end

        if mod(a,TimeIndCheck)==0
            fprintf('\n%02d / 10th Complete\n',a)
            toc(fpTimer)
        end
    end
    %%
    badFrames = isnan(distMatrix(:,1));
    % badFrameInds = mod(find(sum(fullTrialsUI8,[1 2])==0),nFrames);
    % badFrameInds(badFrameInds==0)=nFrames;
    
    distMatrix(badFrames,:) = [];
    distMatrix(:,badFrames) = [];
    
    labelVect(badFrames) = [];
    tLabel(badFrames) = [];
    fSyncInd(badFrames) = [];
    fullTrialInfo = struct('gLabel',labelVect,'tLabel',tLabel,'fSyncInd',fSyncInd);
end
