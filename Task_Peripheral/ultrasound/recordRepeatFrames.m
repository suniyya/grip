function allTrialData = recordRepeatFrames(outlet, uscam, rwcam, uscam2, trialTime, fps, finalRes, fullResRW, cropBounds, allTrialData)
    allTrialData.us(:, :, :) = 0;
    allTrialData.us2(:, :, :) = 0;
    allTrialData.rw(:, :, :) = 0;

    timingWiggleRoom = 0.0001;
    timeCheck = 1/fps - timingWiggleRoom;

    startTime = tic;
    currentAcqTime = toc(startTime);
    frameIdx = 1;

    while toc(startTime) < trialTime
        if (toc(startTime) - currentAcqTime) > timeCheck
            currentAcqTime = toc(startTime);
            
            img1 = rgb2gray(snapshot(uscam));
            img2 = rgb2gray(snapshot(rwcam));
            img3 = rgb2gray(snapshot(uscam2));
            

            img1_cropped = img1(cropBounds(1):cropBounds(1)+finalRes(1)-1, cropBounds(2):cropBounds(2)+finalRes(2)-1);
            img3_cropped = img3(cropBounds(1):cropBounds(1)+finalRes(1)-1, cropBounds(2):cropBounds(2)+finalRes(2)-1);

            allTrialData.us(:,:,frameIdx) = img1_cropped;
            allTrialData.rw(:,:,frameIdx) = img2;
            allTrialData.us2(:,:,frameIdx) = img3_cropped;
            
            toSend = num2str(frameIdx);
            outlet.push_sample({toSend});

            frameIdx = frameIdx + 1;
        end
    end
    %frameIdx
end
