function [eFrameStruct,sFrameStruct,fullTrialStruct] = frameAnalysis25(subjectFilepath,distMeasure,nTrials,nKnown,cropFlag,eFlag,sFlag,fullFlag,whichLimb,SHR_num)

if isempty(cropFlag)
    cropFlag = 0;
end
cropBounds = [];
if isempty(distMeasure)
    distMeasure = 'corr';
end
nIterations = 2000;
if isempty(nTrials)
    disp('WARNING: Total Trial # not specified, assumming 10...')
    nTrials = 10;
end
if isempty(nKnown)
    disp('WARNING: # Known Trials for KNN not specified, defaulting to LOO')
    nKnown = nTrials-1;
end
nDS = 3;

eFrameStruct = struct();
sFrameStruct = struct();
fullTrialStruct = struct();

%=== Get Create Frame Struct ===%
[eFrameStruct.data,sFrameStruct.data,fullTrialStruct.data] = grabUSFrame(subjectFilepath,cropFlag,cropBounds,nTrials,fullFlag,whichLimb,SHR_num);
for a = 1:size(eFrameStruct.data,1)
    for b = 1:size(eFrameStruct.data,2)
        if isempty(eFrameStruct.data{a,b}{:})
            eFrameStruct.data{a,b} = {nan(1024,1024)};
        end
    end
end
if eFlag

    %Edit 2025, Only want downscaled data
    %=== Downscale Image Data ===%
    for a = 2:nDS+1
        eFrameStruct(a).data = cell2table(cellfun(@(x) imresize(x,.5,'bicubic'),table2cell(eFrameStruct(a-1).data),'uniformOutput',false),'VariableNames',eFrameStruct(1).data.Properties.VariableNames);
        if a == nDS+1
            [eFrameStruct(a).distMatrix,eFrameStruct(a).labelVect,eFrameStruct(a).graspNames] = trialPairwiseDist(eFrameStruct(a).data,distMeasure);
            [eFrameStruct(a).graspClassifications] = distMatrixKNN_unequalFix(eFrameStruct(a).distMatrix,eFrameStruct(a).labelVect,eFrameStruct(a).graspNames,nKnown,[]);
        end
    end


    %=== Get Frame Pairwise Distances ===% %%%%%%%% Justin edit %%%%%%%%
    % [eFrameStruct.distMatrix,eFrameStruct.labelVect,eFrameStruct.graspNames] = trialPairwiseDist(eFrameStruct.data,distMeasure);
    % %=== Run KNN on Distance Matrix ===%
    % [eFrameStruct.graspClassifications] = distMatrixKNN(eFrameStruct(1).distMatrix,eFrameStruct.labelVect,eFrameStruct.graspNames,nKnown,nIterations);
    % %=== RSA ===%   
    % [eFrameStruct.RDM] = createRDMfromDistMat(eFrameStruct.distMatrix,eFrameStruct.labelVect,eFrameStruct.graspNames);
    % %=== Downscale Image Data ===%
    % for a = 2:nDS+1
    %     eFrameStruct(a).data = cell2table(cellfun(@(x) imresize(x,.5,'bicubic'),table2cell(eFrameStruct(a-1).data),'uniformOutput',false),'VariableNames',eFrameStruct(1).data.Properties.VariableNames);
    %     if a == nDS+1
    %         [eFrameStruct(a).distMatrix,eFrameStruct(a).labelVect,eFrameStruct(a).graspNames] = trialPairwiseDist(eFrameStruct(a).data,distMeasure);
    %         [eFrameStruct(a).graspClassifications] = distMatrixKNN(eFrameStruct(a).distMatrix,eFrameStruct(a).labelVect,eFrameStruct(a).graspNames,nKnown,nIterations);
    %     end
    %     % [eFrameStruct(a).RDM] = createRDMfromDistMat(eFrameStruct(a).distMatrix,eFrameStruct(a).labelVect,eFrameStruct(a).graspNames);
    % end
end
if sFlag
    %=== Get Frame Pairwise Distances ===%
    [sFrameStruct.distMatrix,sFrameStruct.labelVect,sFrameStruct.graspNames] = trialPairwiseDist(sFrameStruct.data,distMeasure);
    %=== Run KNN on Distance Matrix ===%
    [sFrameStruct.graspClassifications] = distMatrixKNN(sFrameStruct(1).distMatrix,sFrameStruct.labelVect,sFrameStruct.graspNames,nKnown,nIterations);
    %=== RSA ===%
    [sFrameStruct.RDM] = createRDMfromDistMat(sFrameStruct.distMatrix,sFrameStruct.labelVect,sFrameStruct.graspNames);
    %=== Downscale Image Data ===%
    for a = 2:nDS+1
        sFrameStruct(a).data = cell2table(cellfun(@(x) imresize(x,.5,'bicubic'),table2cell(sFrameStruct(a-1).data),'uniformOutput',false),'VariableNames',sFrameStruct(1).data.Properties.VariableNames);
        [sFrameStruct(a).distMatrix,sFrameStruct(a).labelVect,sFrameStruct(a).graspNames] = trialPairwiseDist(sFrameStruct(a).data,distMeasure);
        [sFrameStruct(a).graspClassifications] = distMatrixKNN(sFrameStruct(a).distMatrix,sFrameStruct(a).labelVect,sFrameStruct(a).graspNames,nKnown,nIterations);
        [sFrameStruct(a).RDM] = createRDMfromDistMat(sFrameStruct(a).distMatrix,sFrameStruct(a).labelVect,sFrameStruct(a).graspNames);
    end
end
if fullFlag
    %=== Get Frame Pairwise Distances ===%
%     [fullTrialStruct.distMatrix,fullTrialStruct.labelVect,fullTrialStruct.graspNames,fullTrialStruct.info] = trialPairwiseDist(fullTrialStruct.data,distMeasure);
%     [fullTrialStruct(a).graspClassifications] = distMatrixKNN(fullTrialStruct(a).distMatrix,fullTrialStruct.labelVect,fullTrialStruct(a).graspNames,nKnown,nIterations);
    for a = 2:nDS+1
        fullTrialStruct(a).data = cell2table(cellfun(@(x) imresize(x,.5,'bicubic'),table2cell(fullTrialStruct(a-1).data),'uniformOutput',false),'VariableNames',fullTrialStruct(1).data.Properties.VariableNames);
        if a == nDS+1
            [fullTrialStruct(a).distMatrix,fullTrialStruct(a).labelVect,fullTrialStruct(a).graspNames,fullTrialStruct(a).info] = trialPairwiseDist(fullTrialStruct(a).data,distMeasure);
        end
    end
end

% %%
% figure;
% for a = 1:length(eFrameStruct)
%     subplot(2,2,a)
%     heatmap(eFrameStruct(a).graspNames,eFrameStruct(a).graspNames,eFrameStruct(a).RDM,'colormap',hot);
% end
end