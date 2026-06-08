function [graspClassifications] = distMatrixKNN(distMatrix,labelVect,graspNames,nKnown,nIterations)

if isempty(gcp('nocreate'))
    ppool = parpool();
    %     nWorkers = ppool.NumWorkers;
else
    ppool = gcp('nocreate');
    %     nWorkers = ppool.NumWorkers;
end

nGrasps = length(graspNames);
[~,nTrials] = mode(labelVect);
graspInds = nan(nTrials,nGrasps);

parfor a = 1:nGrasps
    tempInds = find(labelVect==a);
    graspInds(:,a) = [tempInds;nan(nTrials-length(tempInds))];
end

nTrialsPerGrasp = sum(~isnan(graspInds));
if any(nKnown >= nTrialsPerGrasp)
    disp('nKnown exceeds max number allowable... switching to LOOCV')
    nKnownPerGrasp = nTrialsPerGrasp-1;
else
    nKnownPerGrasp = repmat(nKnown,1,nGrasps);
end

graspClassifications = zeros(nGrasps);
predLabel = nan(nIterations,nGrasps);

parfor n = 1:nIterations
    
    %=== Randomize Trial Order ===%
    knownInds = nan(max(nKnownPerGrasp),nGrasps);
    unknownInds = nan(1,nGrasps);
    for a = 1:nGrasps
        randOrder = randperm(nTrialsPerGrasp(a));
        knownInds(1:nKnownPerGrasp(a),a) = randOrder(1:nKnownPerGrasp(a))+nTrials*(a-1);
        unknownInds(a) = randOrder(nKnownPerGrasp(a)+1)+nTrials*(a-1);
    end
    
    knownDists = distMatrix(knownInds(:),unknownInds);
    [~,NNlibInds] = min(knownDists,[],1);
    NNtrialInds = knownInds(NNlibInds);
    predLabel(n,:) = labelVect(NNtrialInds);
end

for a = 1:nGrasps
    graspClassifications(a,:) = sum(predLabel==a);
end

figure;
cm = confusionchart(graspClassifications,graspNames,'Normalization','row-normalized');
    