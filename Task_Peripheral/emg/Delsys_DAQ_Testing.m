% Marcus Battraw
% Ni USB-6210 DAQ 
% Setup for EMG Data Acqusition
%% v2 Eden Winslow, using loops, works for all Devs   
% v3 Bear_Cub PC, not modified

clear
close all
clc

rangelow = -10;
rangehigh = 10;

disp("Initializing the DAQ")
dq = daq("ni"); % Initialize the DAQ
disp("Done")
dq.Rate = 2000; % Setup number of samples
n = 1;      % ADJUST DEPENDING ON WHICH DEV YOU'RE USING (1 for old emg, 2 or 3 for force, 5 for new emg)

deviceID = sprintf('Dev%d', n);

disp("Setup")

numChannels = 16;        % CHANGE THIS!!!!!!!!!!!!!!!!!!!!

% Create channel objects
channels = cell(1, numChannels);
channelName = cell(1, numChannels);
dataFields = cell(1, numChannels);

disp("ok")

for i = 1:numChannels
    channelName{i} = sprintf('ai%d', i-1);
    dataFields{i} = sprintf('Dev%d_ai%d', n, i-1);
end

disp("yep")

% NOTE TO SELF: CHECK CHANNELS FOR LOAD CELL

% Define inputs, terminal type, and input range
for i = 1:numChannels
    channels{i} = addinput(dq, deviceID, channelName{i}, "Voltage"); % Create and store channel
    channels{i}.TerminalConfig = 'SingleEnded';
    channels{i}.Range = [rangelow, rangehigh];
end

disp("Start squeezing")
pause(1.5);

% Configure terminal type and input range
% for i = 1:numel(channels)
%     channels{i}.TerminalConfig = 'SingleEnded';
%     channels{i}.Range = [rangelow, rangehigh];
% end


% Read data
disp('Begin Recording Data')
data = read(dq,seconds(4));
disp('Data recorded')

t = data.Time;
s = seconds(t);
% Plot data

numFigures = ceil(length(dataFields) / 4);

for fig = 1:numFigures
    figure;
    for subplotIdx = 1:4
        subplot(4, 1, subplotIdx);
        dataIdx = (fig - 1) * 4 + subplotIdx;
        if dataIdx <= length(dataFields)
            plot(s, data.(dataFields{dataIdx}));
            ylabel("Voltage (V)");
            if subplotIdx == 4
                xlabel("Time (Sec)");
            end
        else
            axis off; % Hide empty subplot
        end
    end
end

%ave = mean(data.Dev2_ai0)