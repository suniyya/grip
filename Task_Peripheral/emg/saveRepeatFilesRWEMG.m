function saveRepeatFilesRWEMG(outputDir, baseName, rwFrames, emgData)
    save(fullfile(outputDir, [baseName, '_rwFrames.mat']), 'rwFrames');
    save(fullfile(outputDir, [baseName, '_emg.mat']), 'emgData');
end