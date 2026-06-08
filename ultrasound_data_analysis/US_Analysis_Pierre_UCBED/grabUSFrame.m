function [eFramesTbl,sFramesTbl,fullTrialTbl] = grabUSFrame(subjectFilepath,cropFlag,cropBounds,nTrials,fullTrialFlag,whichLimb,SHR_num)

if cropFlag
    if ~exist('cropBounds','var')||isempty(cropBounds)
        cropBounds = [1,200;101,100];%Top & Left Start, Subtract from Bottom and Right
    end
else
    cropBounds = [1 0;1 0];
end

if ~exist('nTrials','var')||isempty(nTrials)
    nTrials = 10;
end

if isempty(gcp('nocreate'))
    ppool = parpool();
    nWorkers = ppool.NumWorkers;
else
    ppool = gcp('nocreate');
    nWorkers = ppool.NumWorkers;
end

if fullTrialFlag == true
    eFramesTbl = [];
    sFramesTbl = [];
end

% Get a list of all files and folders in this folder.
files = dir(subjectFilepath);
% Get a logical vector that tells which is a directory.
dirFlags = [files.isdir];
% Extract only those that are directories.
subFolders = files(dirFlags);
%Remove '.' and '..' from the list of subFolders
subFolders(ismember( {subFolders.name}, {'.', '..'})) = [];

eFrames = cell(nTrials,length(subFolders));
sFrames = cell(nTrials,length(subFolders));
fullTrials = cell(nTrials,length(subFolders));
fullTrialTbl = [];

if fullTrialFlag
    gTimer = tic;
    for gg = 1:length(subFolders)
        [AFF_FilesInds,UA_FilesInds] = selectUltrasoundFiles(strcat(subjectFilepath,'\',subFolders(gg).name));
        if strcmp(whichLimb,'AFF')
            usFilesInds = AFF_FilesInds;
            disp('Grabbing Affected Limb Data')
        elseif strcmp(whichLimb,'UA')
            usFilesInds = UA_FilesInds;
            disp('Grabbing Unaffected Limb Data')
        else
            error("ERROR, LIMB NOT SPECIFIED")
        end
        trialsFileInfo = dir('*.mat');

        %% === SPMD === %%
        %         for tt = 1:ceil(length(usFilesInds)/nWorkers)
        %             dm = [];
        %             trialInd = [];
        % %             eFrameC = [];
        % %             sFrameC = [];
        %
        %             spmd
        %
        %                 trialInd = nWorkers*(tt-1)+spmdindex;
        %                 if trialInd <= length(usFilesInds)
        %                     dm = load(trialsFileInfo(usFilesInds(trialInd)).name,'dataMatrix');
        %                     datMatC = dm.dataMatrix;
        %
        %                     %                     eFrameInd = find(sum(dm.dataMatrix,[1 2])~=0,1,'last');
        %                     %                     eFrameC = dm.dataMatrix(cropBounds(1,1):end-cropBounds(1,2),...
        %                     %                         cropBounds(2,1):end-cropBounds(2,2),eFrameInd);
        %                     %                     sFrameInd = find(sum(dm.dataMatrix,[1 2])~=0,1,'first');
        %                     %                     sFrameC = dm.dataMatrix(cropBounds(1,1):end-cropBounds(1,2),...
        %                     %                         cropBounds(2,1):end-cropBounds(2,2),sFrameInd);
        %
        %                 end
        %             end
        %             realLabInds = 1:min(nWorkers,length(usFilesInds)-nWorkers*(tt-1));
        %             %             eFrames(((tt-1)*nWorkers)+realLabInds,gg) = (eFrameC(realLabInds));
        %             %             sFrames(((tt-1)*nWorkers)+realLabInds,gg) = (sFrameC(realLabInds));
        %             fullTrials(((tt-1)*nWorkers)+realLabInds,gg) = (datMatC(realLabInds));
        %
        %         end

        % % === SPMD END === % %



        %         %% === DEBUG === %%
        for tt = 1:length(usFilesInds)
            dm = [];
            trialInd = [];
            %             eFrameC = [];
            %             sFrameC = [];


            trialInd = tt;% nWorkers*(tt-1)+spmdindex;
            if trialInd <= length(usFilesInds)
                if strcmp(whichLimb,'AFF')
                    dm = load(trialsFileInfo(usFilesInds(trialInd)).name,'dataMatrix');
                    datMatC = dm.dataMatrix;
                elseif strcmp(whichLimb,'UA')
                    dm = load(trialsFileInfo(usFilesInds(trialInd)).name,'dataMatrixUS2');
                    datMatC = dm.dataMatrixUS2;
                else
                    error('LIMB NOT SPECIFIED')
                end

            end
            %realLabInds = 1:min(nWorkers,length(usFilesInds)-nWorkers*(tt-1));
            fullTrials{tt,gg} = datMatC;

        end
        %
        %         % % DEBUG END === % %
        %
        %
        %         disp([subFolders(gg).name ' ' 'is done...'])
        %         toc(gTimer)
    end

    %     eFrames(all(cellfun(@isempty, eFrames),2), :) = [];
    %     sFrames(all(cellfun(@isempty, sFrames),2), :) = [];
    fullTrials(all(cellfun(@isempty, fullTrials),2),:) = [];

    %     eFramesTbl = cell2table(eFrames,'VariableNames',{subFolders.name});
    %     sFramesTbl = cell2table(sFrames,'VariableNames',{subFolders.name});
    fullTrialTbl = cell2table(fullTrials,'VariableNames',{subFolders.name});

end

if ~fullTrialFlag
    gTimer = tic;
    for gg = 1:length(subFolders)
        %usFilesInds = selectUltrasoundFiles(strcat(subjectFilepath,'\',subFolders(gg).name));
        [AFF_FilesInds,UA_FilesInds] = selectUltrasoundFiles(strcat(subjectFilepath,'\',subFolders(gg).name));
        if strcmp(whichLimb,'AFF')
            usFilesInds = AFF_FilesInds;
            disp('Grabbing Affected Limb Data')
        elseif strcmp(whichLimb,'UA')
            usFilesInds = UA_FilesInds;
            disp('Grabbing Unaffected Limb Data')
        else
            error("ERROR, LIMB NOT SPECIFIED")
        end
        trialsFileInfo = dir('*.mat');

        for tt = 1:ceil(length(usFilesInds)/nWorkers)
            dm = [];
            trialInd = [];
            eFrameC = [];
            sFrameC = [];

            spmd

                trialInd = nWorkers*(tt-1)+labindex;
                if trialInd <= length(usFilesInds)

                    if strcmp(whichLimb,'AFF')
                        dm = load(trialsFileInfo(usFilesInds(trialInd)).name,'dataMatrix');
                        % matfile(trialsFileInfo(usFilesInds(trialInd)).name,)
                        if isa(dm.dataMatrix,'double')
                            dm.dataMatrix = uint8(dm.dataMatrix);
                        end

                        eFrameInd = find(sum(dm.dataMatrix,[1 2])~=0,1,'last');
                        eFrameC = dm.dataMatrix(cropBounds(1,1):end-cropBounds(1,2),...
                            cropBounds(2,1):end-cropBounds(2,2),eFrameInd);
                        sFrameInd = find(sum(dm.dataMatrix,[1 2])~=0,1,'first');
                        sFrameC = dm.dataMatrix(cropBounds(1,1):end-cropBounds(1,2),...
                            cropBounds(2,1):end-cropBounds(2,2),sFrameInd);
                    elseif strcmp(whichLimb,'UA')
                        if SHR_num > 13
                            dm = load(trialsFileInfo(usFilesInds(trialInd)).name,'dataMatrixUS2');
                            if isa(dm.dataMatrixUS2,'double')
                                dm.dataMatrix = uint8(dm.dataMatrixUS2);
                            end
                        else
                            dm = load(trialsFileInfo(usFilesInds(trialInd)).name,'dataMatrix');
                            dm.dataMatrixUS2 = uint8(dm.dataMatrix);
                            dm.dataMatrix = [];
                        end
                        eFrameInd = find(sum(dm.dataMatrixUS2,[1 2])~=0,1,'last');
                        eFrameC = dm.dataMatrixUS2(cropBounds(1,1):end-cropBounds(1,2),...
                            cropBounds(2,1):end-cropBounds(2,2),eFrameInd);
                        sFrameInd = find(sum(dm.dataMatrixUS2,[1 2])~=0,1,'first');
                        sFrameC = dm.dataMatrixUS2(cropBounds(1,1):end-cropBounds(1,2),...
                            cropBounds(2,1):end-cropBounds(2,2),sFrameInd);
                    else
                        error('LIMB NOT SPECIFIED')
                    end
                end
            end
            realLabInds = 1:min(nWorkers,length(usFilesInds)-nWorkers*(tt-1));
            eFrames(((tt-1)*nWorkers)+realLabInds,gg) = (eFrameC(realLabInds));
            sFrames(((tt-1)*nWorkers)+realLabInds,gg) = (sFrameC(realLabInds));

        end
        disp([subFolders(gg).name ' ' 'is done...'])
        toc(gTimer)
    end

    eFrames(all(cellfun(@isempty, eFrames),2), :) = [];
    sFrames(all(cellfun(@isempty, sFrames),2), :) = [];

    eFramesTbl = cell2table(eFrames,'VariableNames',{subFolders.name});
    sFramesTbl = cell2table(sFrames,'VariableNames',{subFolders.name});
end

end