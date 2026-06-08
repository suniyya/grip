function saveRepeatFiles(basePath, baseName, usFrames, rwFrames, us2Frames)
    save(fullfile(basePath, [baseName '_US.mat']), 'usFrames', '-v7.3');
    save(fullfile(basePath, [baseName '_RW.mat']), 'rwFrames', '-v7.3');
    save(fullfile(basePath, [baseName '_US2.mat']), 'us2Frames', '-v7.3');
    fprintf('Saving %s: %d US, %d RW, %d US2 frames\n', baseName, length(usFrames), length(rwFrames), length(us2Frames));
end