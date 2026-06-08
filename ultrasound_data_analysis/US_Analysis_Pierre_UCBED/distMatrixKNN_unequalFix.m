function [graspClassifications] = distMatrixKNN_unequalFix(distMatrix,labelVect,graspNames,nKnown,nIterations)

% === Create Parallel Pool === %
if isempty(gcp('nocreate'))
    ppool = parpool(8);
    %     nWorkers = ppool.NumWorkers;
else
    ppool = gcp('nocreate');
    %     nWorkers = ppool.NumWorkers;
end
% === Check if we're doing true LOOCV === %
if isempty(nIterations)
    trueLOOCVflag = true;
else
    trueLOOCVflag = false;
end
% === Get # grasps, trials === %
nGrasps = length(graspNames);
[~,nTrials] = mode(labelVect);
graspInds = nan(nTrials,nGrasps);

% === Find which grasp each row in distMatrix is === %
for a = 1:nGrasps
    tempInds = find(labelVect==a);
    graspInds(:,a) = [tempInds;nan(nTrials-length(tempInds))];
end
nTrialsPerGrasp = sum(~isnan(graspInds));

%% === True LOOCV === %%
if trueLOOCVflag
    graspClassifications = zeros(nGrasps);
    predLabel = nan(size(labelVect));

    for a = 1:length(labelVect)

        %Confirm the data isn't missing
        if ~isnan(distMatrix(a,a))

            %Sort the distances
            [~,sortedDistIdx] = sort(distMatrix(:,a));

            %SHOULD skip the first NN since it will always be itself
            if sortedDistIdx(1) == a
                predLabel(a) = labelVect(sortedDistIdx(2));
            %But in case something is going wrong
            else
                predLabel(a) = labelVect(sortedDistIdx(1));
                fprintf('LOOCV Problem: 1st NN is not itself\ntrial: %d\n',a)
            end

            graspClassifications(labelVect(a),predLabel(a)) = graspClassifications(labelVect(a),predLabel(a)) + 1;
        end
    end

else
%% === K-Folds === %%
if isempty(nKnown)
    nKnown = min(nTrialsPerGrasp - 1);
    nUnknown = nTrialsPerGrasp - nKnown;
else
    nUnknown = nTrialsPerGrasp - nKnown;
end

graspClassifications = zeros(nGrasps);

for a = 1:nIterations

    knownLib = nan(nKnown,nGrasps);
    unknownLib = nan(max(nUnknown,[],'all'),nGrasps);
    predLabel = nan(size(unknownLib));

    % === Randomize trial order within each grasp to select known/unknown partitions === %
    for b = 1:nGrasps
        singleGraspInd = graspInds(1:nTrialsPerGrasp(b),b);
        randOrderInd = singleGraspInd(randperm(nTrialsPerGrasp(b)));

        knownLib(:,b) = randOrderInd(1:nKnown);
        unknownLib(1:nUnknown(b),b) = randOrderInd(nKnown+1:nKnown+nUnknown(b));
    end

    % === For each trial in the unknown partition, find the NN === %
    for b = 1:numel(unknownLib)

        ismemLoopFlag = false;
        %Make sure element is a real trial
        if ~isnan(unknownLib(b))

            %Sort the distances to the unknown and grab the indices
            [~,sortedDistIdx] = sort(distMatrix(:,unknownLib(b)));

            %Loop thru the sorted distance indices (smallest to largest dist)
            for c = 1:length(sortedDistIdx)

                %Check if the next NN is in the known library
                if ismember(sortedDistIdx(c),knownLib)

                    %Add label of NN as prediction
                    predLabel(b) = labelVect(sortedDistIdx(c));

                    graspClassifications(labelVect(unknownLib(b)),predLabel(b)) = graspClassifications(labelVect(unknownLib(b)),predLabel(b)) + 1;

                    ismemLoopFlag = true;
                end

                %Check if we've found a valid NN yet
                if ismemLoopFlag == true
                    %If we have found a NN, end the loop
                    ismemLoopFlag = false;%reset the flag
                    break

                    %Display a warning if a NN couldn't be found after all trials checked (something went wrong)
                elseif c == length(sortedDistIdx) && ismemLoopFlag == false
                    printf('Problem in finding NN: \nUnknown Trial: %d\n',unknownLib(b))
                    ismemLoopFlag = false;%reset the flag anyway
                end

            end
        end
    end


end
end









%%
% nTrialsPerGrasp = sum(~isnan(graspInds));
% nTrialsPerGrasp = nKnown+1;
% if any(nKnown >= nTrialsPerGrasp)
%     disp('nKnown exceeds max number allowable... switching to LOOCV')
%     nKnownPerGrasp = nTrialsPerGrasp-1;
% else
%     % tweak to pass nKnown as array
%     nKnownPerGrasp = nKnown;
%     % nKnownPerGrasp = repmat(nKnown,1,nGrasps);
% end
% 
% graspClassifications = zeros(nGrasps);
% predLabel = nan(nIterations,nGrasps);

% for n = 1:nIterations
% 
%     %=== Randomize Trial Order ===%
% 
% 
%     knownInds = nan(max(nKnownPerGrasp),nGrasps);
% 
%     unknownInds = nan(1,nGrasps);
%     disp(unknownInds);
%     for a = 1:nGrasps
% 
%         randOrder = randperm(nTrialsPerGrasp(a));
% 
%         knownInds(1:nKnownPerGrasp(a),a) = randOrder(1:nKnownPerGrasp(a))+nTrials*(a-1);
% 
%         unknownInds(a) = randOrder(nKnownPerGrasp(a)+1)+nTrials*(a-1);
% 
%     end
% 
% 
%     % loop through each grasp, grab 1-known
%     knownDists = distMatrix(knownInds(~isnan(knownInds(:))),unknownInds);
% 
%     [~,NNlibInds] = min(knownDists,[],1);
% 
%     NNtrialInds = nan(size(NNlibInds));
%     for gg = 1:length(NNlibInds)
%         NNtrialInds(gg) = knownInds(NNlibInds,gg);
%     end
% 
%     % NNtrialInds = knownInds(NNlibInds);
%     predLabel(n,:) = labelVect(NNtrialInds);
% 
% end
% 
% for a = 1:nGrasps
%     graspClassifications(a,:) = sum(predLabel==a);
% end

figure;
cm = confusionchart(graspClassifications,graspNames,'Normalization','row-normalized');
    