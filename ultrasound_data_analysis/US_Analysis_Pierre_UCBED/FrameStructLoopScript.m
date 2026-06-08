
subjectInfo = struct();

%001
subjectInfo(1,1).subjectFilepath = 'F:\SHR_SACRAMENTO\SHR009\SHR009SS_ForAnalysis\SHR009SS';subjectInfo(9,1).SHR_num = 9;subjectInfo(9,1).nTrials = 25;subjectInfo(9,1).limbStr = 'Aff';
subjectInfo(1,2).subjectFilepath = 'F:\SHR_SACRAMENTO\SHR009\SHR009SS_ForAnalysis\SHR009SS';subjectInfo(9,2).SHR_num = 9;subjectInfo(9,2).nTrials = 25;subjectInfo(9,2).limbStr = 'UA';


savePath = 'F:\DIGIT_FrameAnalysis';
%=========================%

eFlag = 1;
sFlag = 0;
fullFlag = 0;

cropFlag = 0;
cropBounds = [];
distMeasure = 'corr'; %'sqrtPearson'
nIterations = 2000;

whichSubjToRun = [15];% <--- @Eden Change This
whichLimbs = [1,2];
limbList = ["AFF","UA"];
%%
for subjCtr = 1:length(whichSubjToRun)
    currentSubj = whichSubjToRun(subjCtr);
    for limbCtr = 1:length(whichLimbs)
        currentLimb = whichLimbs(limbCtr);
        nKnown = subjectInfo(currentSubj,currentLimb).nTrials-1;
        nDS = 3;

            [eFrameStruct,~,~] = frameAnalysis25(subjectInfo(currentSubj,currentLimb).subjectFilepath,distMeasure,subjectInfo(currentSubj,currentLimb).nTrials,nKnown,cropFlag,eFlag,sFlag,fullFlag,limbList(currentLimb),currentSubj);
        if eFlag
            save(strcat(savePath,sprintf('\\SHR0%02d_',subjectInfo(currentSubj,currentLimb).SHR_num),subjectInfo(currentSubj,currentLimb).limbStr,'_eFrameAnalysis.mat'),'eFrameStruct')
        end
    end
    fprintf('\nSubject %d | Limb %s Done (%d out of %d)\n',whichSubjToRun(subjCtr),limbList(whichLimbs(limbCtr)),subjCtr,length(whichSubjToRun))
end
% if sFlag
% save(strcat(savePath,sprintf('\\SHR0%02d_',SHR_num),limbStr,'_sFrameAnalysis.mat'),'sFrameStruct')
% end
% if fullFlag
% save(strcat(savePath,sprintf('\\SHR0%02d_',SHR_num),limbStr,'_fullFrameAnalysis.mat'),'fullTrialStruct')
% end