function [allVideoData, emgData, timeStamps] = recordTrialData(outlet, uscam, uscam2, rwcam, dq, trialTime, fps, finalRes, fullResRW, cropBounds, allVideoData)
    allVideoData.us(:, :, :) = 0;
    allVideoData.us2(:, :, :) = 0;
    allVideoData.rw(:, :, :) = 0;

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

            img1 = rgb2gray(snapshot(uscam));
            img2 = rgb2gray(snapshot(rwcam));
            img3 = rgb2gray(snapshot(uscam2));
            

            img1_cropped = img1(cropBounds(1):cropBounds(1)+finalRes(1)-1, cropBounds(2):cropBounds(2)+finalRes(2)-1);
            img3_cropped = img3(cropBounds(1):cropBounds(1)+finalRes(1)-1, cropBounds(2):cropBounds(2)+finalRes(2)-1);

            allVideoData.us(:,:,frameIdx) = img1_cropped;
            allVideoData.rw(:,:,frameIdx) = img2;
            allVideoData.us2(:,:,frameIdx) = img3_cropped;
            
            toSend = num2str(frameIdx);
            outlet.push_sample({toSend});

            frameIdx = frameIdx + 1;
        end
    end
    % Send end marker
    [emgData, timeStamps] = read(dq, "all", "OutputFormat", "Matrix");
    flush(dq); % to clear buffer before next acq
    outlet.push_sample({'RECORDING_END'});
    disp('Stopped recording');
    [x, y] = size(emgData);
    disp(strcat("Num EMG samples ", num2str(x)));
end
