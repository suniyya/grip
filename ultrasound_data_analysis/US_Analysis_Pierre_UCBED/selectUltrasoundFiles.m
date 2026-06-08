function [affFilesInds,uaFilesInds] = selectUltrasoundFiles(dataFilepath)
cd(dataFilepath)
trialsFileInfo = dir('*.mat');

expression1 = 'RW';
rwCheck = regexp({trialsFileInfo.name},expression1,'ONCE');
rwFlags = ~cellfun(@isempty,rwCheck);%"rwcheck is NOT empty"

expression2 = 'US2';
uaCheck = regexp({trialsFileInfo.name},expression2,'ONCE');%Unaffected limb, dual US setup
uaFlags = ~cellfun(@isempty,uaCheck);%"unaffected check is NOT empty"

affCheck = ~rwFlags&~uaFlags;

allFileInds = 1:length(trialsFileInfo);
affFilesInds = allFileInds(affCheck);
uaFilesInds = allFileInds(uaFlags);
end