function [rwFrames, emgData, timeStamps] = recordTrialData(outlet, rwcam, dq, trialTime, fps)
    
    % Send LSL marker
    outlet.push_sample({'RECORDING_START'});

    % Start EMG in background
    start(dq,"Duration",seconds(trialTime));  % non-blocking
    % Start video capture
    % Wait for EMG acquisition to finish and read data
    timingWiggleRoom = 0.0001;
    timeCheck = 1/fps - timingWiggleRoom;

    startTime = tic;
    currentAcqTime = toc(startTime);
    frameIdx = 1;

    while toc(startTime) < trialTime || dq.Running
        if (toc(startTime) - currentAcqTime) > timeCheck
            currentAcqTime = toc(startTime);
            img2 = rgb2gray(snapshot(rwcam));
            rwFrames(:,:,frameIdx) = img2;
            frameIdx = frameIdx + 1;
        end
    end
    % Send end marker
    [emgData, timeStamps] = read(dq, "all", "OutputFormat", "Matrix");
    flush(dq); % to clear buffer before next acq
    disp('Stopped recording');
    outlet.push_sample({'RECORDING_END'});
    [x, y] = size(emgData);
    disp(strcat("Num EMG samples ", num2str(x)));
end
