% Ultrasound + EMG + Real-World Camera Recording Synced to LSL Markers and
% PsychoPy task

clear; close all; clc;
% ========= Delsys + Real-World Camera Recording Synced to LSL Markers
dq = setupEmgDelsys(); 

% ==== INIT CAMERAS ====
uscam = webcam(3);       % Ultrasound cam 1 (new/affected)
rwcam = webcam(2);       % Real-world cam
uscam2 = webcam(1);  % Ultrasound cam 2

%preview(uscam);
%preview(rwcam);
%preview(uscam2);

% ==== PARAMETERS ====
fps = 20;
finalRes = [1024;1024];
cropBounds = [30;370];
fullRes = size(snapshot(uscam));
fullResRW = size(snapshot(rwcam));

trialDir = './subject-data';
subjectFilename = input('Subject ID: ', 's');
runNum = input("Run Number: ", 's');
outputDir = fullfile(trialDir, subjectFilename, runNum);
if ~exist(outputDir, 'dir')
    mkdir(outputDir);
end

% ==== SET PATHS ====
lslPath = 'C:\Users\ucdbe\grip\liblsl-Matlab'; 
addpath(genpath(lslPath));

% ==== INIT LSL ====
disp('Loading LSL library...');
lib = lsl_loadlib();

disp('Resolving LSL inlet for marker stream...');
results = lsl_resolve_byprop(lib,'type','Markers',1,5);
if isempty(results)
    error('No LSL marker stream found!');
end
inlet = lsl_inlet(results{1});
disp('LSL inlet connected.');

info_out = lsl_streaminfo(lib, 'emg_us_frame_outlet', 'Markers', 1, fps, 'cf_string', 'us_frame_id');
outlet = lsl_outlet(info_out);

ask = input("Did you press 'Start Recording' in Lab Recorder?\n And did you check that both streams are green? This is important. ",'s');
if strcmpi(ask, 'no')
    error('Setup not complete. Exiting code.');
end

ask = input("Did you preview and check all cams? ",'s');
if strcmpi(ask, 'no')
    error('Setup not complete. Exiting code.');
end

% ==== INIT PARPOOL ====
% create parallel pool and warm up with the function that will be given to
% it, so that there are no JIT compilation lags on the first call

disp("Warming up parallel processing workers");
numWorkers = 12;
if ~isempty(gcp('nocreate'))
    parpool('local', numWorkers);
end

dummyData = zeros(fullRes(1), fullRes(2), 70);
parfor i=1:numWorkers
    testfilename = sprintf('warmup_dummy_%d', i);
    saveRepeatFiles('./scratch', testfilename, dummyData, dummyData, dummyData, dummyData);
end

disp("Warm up complete. OK to proceed.");

% ==== VARIABLES ====
recording = false;
repeatCount = 0;
currentGrasp = '';

% make global and ref
trialTime = 3.6;
numFrames = ceil(trialTime * fps); % a bit larger than needed

usFrames = zeros(finalRes(1), finalRes(2), numFrames, 'uint8');
rwFrames = zeros(fullResRW(1), fullResRW(2), numFrames, 'uint8');
us2Frames = zeros(finalRes(1), finalRes(2), numFrames, 'uint8'); 
allVideoData = struct('us', usFrames, 'us2', us2Frames, 'rw', rwFrames); % set to x(:, :) = 0 every time func call ends

% ==== MAIN LOOP ====
disp('Starting main acquisition loop...');
disp('Waiting for markers...');
savingFutures = parallel.FevalFuture.empty;

outlet.push_sample({outputDir});

%try
    while true
        [marker, ts] = inlet.pull_sample(0.0);
        if ~isempty(marker)
            m = marker{1};
            fprintf('Marker received: %s\n', m);
            if startsWith(m, 'IMG_ONSET')
                currentGrasp = extractAfter(m, 'IMG_ONSET_');
                repeatCount = 0;
                fprintf('Starting new grasp: %s\n', currentGrasp);
                outlet.push_sample({m});
            end
            switch m % case switch
                case 'END'
                    fprintf('END marker received. Exiting...\n');
                    outlet.push_sample({'END'});
                    break;
                case 'GO_ONSET'
                    toSend = strcat('repeat:', num2str(repeatCount));
                    outlet.push_sample({toSend});
                    [allVideoData, emgData, timeStamps] = recordTrialData(outlet, uscam, uscam2, rwcam, dq, trialTime, fps, finalRes, fullResRW, cropBounds, allVideoData);
                    repeatCount = repeatCount + 1;
                    tstamp = datestr(now,'yyyymmdd_HHMMSS_FFF');
                    baseName = sprintf('grasp-%s_rep-%d_%s', currentGrasp, repeatCount, tstamp);
                    outlet.push_sample({baseName});
                    f = parfeval(@saveRepeatFiles, 0, outputDir, baseName, allVideoData.us, allVideoData.rw, allVideoData.us2, emgData);
                    savingFutures(end+1) = f;
            end
        end
    end

% catch ME
%     fprintf('Exception caught: %s\n', ME.message);
% end

% ==== CLEANUP ====
% Clean up completed async saves to avoid memory bloat
if ~isempty(savingFutures)
    doneIdx = [savingFutures.State] == "finished";
    savingFutures(doneIdx) = [];
    if ~isempty(gcp('nocreate'))
        delete(gcp('nocreate'));
    end
end
clear uscam rwcam uscam2;
disp('Cleaned up webcams and exiting.');

