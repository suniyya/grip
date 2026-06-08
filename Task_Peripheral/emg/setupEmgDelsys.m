function dq = setupEmgDelsys()

    % Marcus Battraw
    % Main code used to setup the DAQ for EMG recording
    clear all
    close all
    clc
    
    %================ Daq Setup ================%
    dq = daq("ni"); % Initialize the DAQ
    dq.Rate = 6000; % 6000 Setup number of samples 
    
    % Define the inputs
    ch01 = addinput(dq, "DEV1", "ai0", "Voltage");
    ch02 = addinput(dq, "DEV1", "ai1", "Voltage");
    ch03 = addinput(dq, "DEV1", "ai2", "Voltage");
    ch04 = addinput(dq, "DEV1", "ai3", "Voltage");
    ch05 = addinput(dq, "DEV1", "ai4", "Voltage");
    ch06 = addinput(dq, "DEV1", "ai5", "Voltage");
    ch07 = addinput(dq, "DEV1", "ai6", "Voltage");
    ch08 = addinput(dq, "DEV1", "ai7", "Voltage");
    ch09 = addinput(dq, "DEV1", "ai8", "Voltage");
    ch10 = addinput(dq, "DEV1", "ai9", "Voltage");
    ch11 = addinput(dq, "DEV1", "ai10", "Voltage");
    ch12 = addinput(dq, "DEV1", "ai11", "Voltage");
    ch13 = addinput(dq, "DEV1", "ai12", "Voltage");
    ch14 = addinput(dq, "DEV1", "ai13", "Voltage");
    ch15 = addinput(dq, "DEV1", "ai14", "Voltage");
    ch16 = addinput(dq, "DEV1", "ai15", "Voltage");
    
    % Configure terminal type
    ch01.TerminalConfig = 'SingleEnded'; 
    ch02.TerminalConfig = 'SingleEnded'; 
    ch03.TerminalConfig = 'SingleEnded'; 
    ch04.TerminalConfig = 'SingleEnded'; 
    ch05.TerminalConfig = 'SingleEnded'; 
    ch06.TerminalConfig = 'SingleEnded'; 
    ch07.TerminalConfig = 'SingleEnded'; 
    ch08.TerminalConfig = 'SingleEnded'; 
    ch09.TerminalConfig = 'SingleEnded'; 
    ch10.TerminalConfig = 'SingleEnded'; 
    ch11.TerminalConfig = 'SingleEnded'; 
    ch12.TerminalConfig = 'SingleEnded'; 
    ch13.TerminalConfig = 'SingleEnded'; 
    ch14.TerminalConfig = 'SingleEnded'; 
    ch15.TerminalConfig = 'SingleEnded'; 
    ch16.TerminalConfig = 'SingleEnded'; 
    
    % Define input range
    ch01.Range = [-5,5];
    ch02.Range = [-5,5];
    ch03.Range = [-5,5];
    ch04.Range = [-5,5];
    ch05.Range = [-5,5];
    ch06.Range = [-5,5];
    ch07.Range = [-5,5];
    ch08.Range = [-5,5];
    ch09.Range = [-5,5];
    ch10.Range = [-5,5];
    ch11.Range = [-5,5];
    ch12.Range = [-5,5];
    ch13.Range = [-5,5];
    ch14.Range = [-5,5];
    ch15.Range = [-5,5];
    ch16.Range = [-5,5];

end