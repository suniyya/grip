function dq = mocksetupEmgDelsys()

    % Marcus Battraw
    % Main code used to setup the DAQ for EMG recording
    clear all
    close all
    clc
    
    %================ Daq Setup ================%
    dq = daq("ni"); % Initialize the DAQ
    dq.Rate = 6000; % 6000 Setup number of samples 
    
    % Define the inputs
    % do nothing - mock

end