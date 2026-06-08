#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on November 21, 2025, at 12:51
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from code_8
from pandas import read_csv
from psychopy import core
# Run 'Before Experiment' code from code_3


# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.4'
expName = 'grip_task'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': 'S1',
    'affected side (L/R)': '',
    'paradigm (fmri, ultrasound, or emg)': 'emg',
    'conditions file': 'run_1A.csv',
    'mode': 'run',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1920, 1080]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='E:\\UCBED\\Task_Peripheral\\stim_presentation\\grip_task_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('next') is None:
        # initialise next
        next = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='next',
        )
    if deviceManager.getDevice('continue_listener') is None:
        # initialise continue_listener
        continue_listener = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='continue_listener',
        )
    if deviceManager.getDevice('trigger') is None:
        # initialise trigger
        trigger = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='trigger',
        )
    if deviceManager.getDevice('listener1') is None:
        # initialise listener1
        listener1 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='listener1',
        )
    if deviceManager.getDevice('listener_prompt') is None:
        # initialise listener_prompt
        listener_prompt = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='listener_prompt',
        )
    if deviceManager.getDevice('listener') is None:
        # initialise listener
        listener = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='listener',
        )
    if deviceManager.getDevice('listener_break') is None:
        # initialise listener_break
        listener_break = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='listener_break',
        )
    if deviceManager.getDevice('listener_end') is None:
        # initialise listener_end
        listener_end = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='listener_end',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "preload_images" ---
    next = keyboard.Keyboard(deviceName='next')
    # Run 'Begin Experiment' code from code_8
    from pylsl import StreamInfo, StreamOutlet
    
    # Instantiate the StreamInfo
    info = StreamInfo(name='PsychoPy_Markers',
                      type='Markers',
                      channel_count=1,
                      nominal_srate=0,
                      channel_format='string',
                      source_id='griptask')
    
    # Create the outlet — your single pipe for all events
    outlet = StreamOutlet(info)
    
    t_grayscreen_on = None
    
    thisExpLog = data.ExperimentHandler(
                name=expName,
                version='1.0',
                extraInfo=expInfo,
                runtimeInfo=None,
                dataFileName='{}_stimulus_times'.format(filename)
                )
    thisExpPulses = data.ExperimentHandler(
                name=expName,
                version='1.0',
                extraInfo=expInfo,
                runtimeInfo=None,
                dataFileName='{}_pulses'.format(filename)
                )
                
                
    allowedKeys = ['t', 'T', '5', 'escape', 'space']
    conditionsFile = './conditions/'+ expInfo['paradigm (fmri, ultrasound, or emg)']+'/'+expInfo['conditions file']
    print(conditionsFile)
    
    # --- Initialize components for Routine "instruc" ---
    continue_listener = keyboard.Keyboard(deviceName='continue_listener')
    instructions = visual.TextStim(win=win, name='instructions',
        text='Instructions \nYou’ll see pictures of hand shapes on one side of the screen. When the green dot comes, make the hand shape using the same side of your body. When the red dot comes, relax your hand. Keep looking at the dot in the middle.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    # Run 'Begin Experiment' code from code_3
    
    
    
    
    
    # --- Initialize components for Routine "wait_trigger" ---
    trigger = keyboard.Keyboard(deviceName='trigger')
    wait = visual.TextStim(win=win, name='wait',
        text='ready to start',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    # Run 'Begin Experiment' code from code_4
    stimulusNum = 1
    time0 = None
                                
    
    # --- Initialize components for Routine "initial_frames" ---
    # Set experiment start values for variable component dot_size
    dot_size = 1
    dot_sizeContainer = []
    # Set experiment start values for variable component cross_size
    cross_size = 0.3
    cross_sizeContainer = []
    listener1 = keyboard.Keyboard(deviceName='listener1')
    # Run 'Begin Experiment' code from code_2
    if expInfo['mode'] == 'test':
        wait_period = 3
        signal_period = 0
    elif expInfo['mode'] == 'run':
        wait_period = 15
        signal_period = 3
        
        
    green = [-0.145, 0.576, -0.106]
    red = [0.9608, -0.2078, -0.3020]
    
    
    cross = visual.ShapeStim(
            win=win,
            name='stop',
            units='cm', 
            size=cross_size,
            vertices='cross',
            ori=0.0,
            pos=(0, 0),
            draggable=False,
            anchor='center',
            lineWidth=1.0,
            colorSpace='rgb',
            lineColor='white',
            fillColor='white',
            opacity=1,
            depth=-1.0,
            interpolate=True
           )
    
    
    # --- Initialize components for Routine "prompt" ---
    listener_prompt = keyboard.Keyboard(deviceName='listener_prompt')
    # Run 'Begin Experiment' code from code
    
    stop = visual.ShapeStim(
            win=win,
            name='stop',
            units='cm', 
            size=dot_size,
            vertices='circle',
            ori=0.0,
            pos=(0, 0),
            draggable=False,
            anchor='center',
            lineWidth=1.0,
            colorSpace='rgb',
            lineColor='black',
            fillColor=red,
            opacity=None,
            depth=-1.0,
            interpolate=True
           )
    go = visual.ShapeStim(
            win=win,
            name='go',
            units='cm', 
            size=dot_size,
            vertices='circle',
            ori=0.0, pos=(0, 0),
            draggable=False,
            anchor='center',
            lineWidth=1.0,
            colorSpace='rgb',
            lineColor='black',
            fillColor=green,
            opacity=None,
            depth=-2.0,
            interpolate=True
           )
        
        
        
    
    # --- Initialize components for Routine "trial" ---
    listener = keyboard.Keyboard(deviceName='listener')
    
    # --- Initialize components for Routine "interblock_interval" ---
    listener_break = keyboard.Keyboard(deviceName='listener_break')
    
    # --- Initialize components for Routine "end" ---
    text = visual.TextStim(win=win, name='text',
        text='Thank you :)',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    cross_end = visual.ShapeStim(
        win=win, name='cross_end', vertices='cross',units='cm', 
        size=cross_size,
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    listener_end = keyboard.Keyboard(deviceName='listener_end')
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "preload_images" ---
    # create an object to store info about Routine preload_images
    preload_images = data.Routine(
        name='preload_images',
        components=[next],
    )
    preload_images.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for next
    next.keys = []
    next.rt = []
    _next_allKeys = []
    # allowedKeys looks like a variable, so make sure it exists locally
    if 'allowedKeys' in globals():
        allowedKeys = globals()['allowedKeys']
    # Run 'Begin Routine' code from code_8
    # preload images and create image_stim
    sides = ['L', 'R']
    screen_position = {'L': (-300, 0), 'R': (300, 0)}
    grasps = ['iflex', 'key', 'tripod', 'wrot', 'rpower',
    'wrist_flex', 'wrist_ext', 'pinch', 'power', 'point']
    num_grasps = 2*len(grasps)
    stimulus_path = 'stimuli/{}_{}.png'
    
    image_stim = {}
    
    for grasp in grasps:
        for side in sides:
            im_path = stimulus_path.format(grasp, side)
            image_stim[im_path] = visual.ImageStim(
                                        win=win,
                                        name=grasp+side,
                                        units='pix', 
                                        image=im_path,
                                        mask=None,
                                        anchor='center',
                                        ori=0.0,
                                        pos=screen_position[side],
                                        draggable=False,
                                        size=[300, 300],
                                        color=[1,1,1],
                                        colorSpace='rgb',
                                        opacity=1,
                                        flipHoriz=True,
                                        flipVert=False,
                                        texRes=128.0,
                                        interpolate=True,
                                        depth=0.0
                                       )
                                       
    
    
    # store start times for preload_images
    preload_images.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    preload_images.tStart = globalClock.getTime(format='float')
    preload_images.status = STARTED
    thisExp.addData('preload_images.started', preload_images.tStart)
    preload_images.maxDuration = None
    # keep track of which components have finished
    preload_imagesComponents = preload_images.components
    for thisComponent in preload_images.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "preload_images" ---
    preload_images.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *next* updates
        waitOnFlip = False
        
        # if next is starting this frame...
        if next.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            next.frameNStart = frameN  # exact frame index
            next.tStart = t  # local t and not account for scr refresh
            next.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(next, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'next.started')
            # update status
            next.status = STARTED
            # allowed keys looks like a variable named `allowedKeys`
            if not type(allowedKeys) in [list, tuple, np.ndarray]:
                if not isinstance(allowedKeys, str):
                    allowedKeys = str(allowedKeys)
                elif not ',' in allowedKeys:
                    allowedKeys = (allowedKeys,)
                else:
                    allowedKeys = eval(allowedKeys)
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(next.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(next.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if next.status == STARTED and not waitOnFlip:
            theseKeys = next.getKeys(keyList=list(allowedKeys), ignoreKeys=None, waitRelease=False)
            _next_allKeys.extend(theseKeys)
            if len(_next_allKeys):
                next.keys = _next_allKeys[-1].name  # just the last key pressed
                next.rt = _next_allKeys[-1].rt
                next.duration = _next_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        # Run 'Each Frame' code from code_8
        if len(image_stim) >= num_grasps:    
            continueRoutine = False
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            preload_images.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in preload_images.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "preload_images" ---
    for thisComponent in preload_images.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for preload_images
    preload_images.tStop = globalClock.getTime(format='float')
    preload_images.tStopRefresh = tThisFlipGlobal
    thisExp.addData('preload_images.stopped', preload_images.tStop)
    # check responses
    if next.keys in ['', [], None]:  # No response was made
        next.keys = None
    thisExp.addData('next.keys',next.keys)
    if next.keys != None:  # we had a response
        thisExp.addData('next.rt', next.rt)
        thisExp.addData('next.duration', next.duration)
    thisExp.nextEntry()
    # the Routine "preload_images" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instruc" ---
    # create an object to store info about Routine instruc
    instruc = data.Routine(
        name='instruc',
        components=[continue_listener, instructions],
    )
    instruc.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for continue_listener
    continue_listener.keys = []
    continue_listener.rt = []
    _continue_listener_allKeys = []
    # allowedKeys looks like a variable, so make sure it exists locally
    if 'allowedKeys' in globals():
        allowedKeys = globals()['allowedKeys']
    # Run 'Begin Routine' code from code_3
    scanner_keys = []
    scanner_pulses = []
    continue_listener.clearEvents()
    # store start times for instruc
    instruc.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instruc.tStart = globalClock.getTime(format='float')
    instruc.status = STARTED
    thisExp.addData('instruc.started', instruc.tStart)
    instruc.maxDuration = None
    # keep track of which components have finished
    instrucComponents = instruc.components
    for thisComponent in instruc.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instruc" ---
    instruc.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *continue_listener* updates
        waitOnFlip = False
        
        # if continue_listener is starting this frame...
        if continue_listener.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            continue_listener.frameNStart = frameN  # exact frame index
            continue_listener.tStart = t  # local t and not account for scr refresh
            continue_listener.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(continue_listener, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'continue_listener.started')
            # update status
            continue_listener.status = STARTED
            # allowed keys looks like a variable named `allowedKeys`
            if not type(allowedKeys) in [list, tuple, np.ndarray]:
                if not isinstance(allowedKeys, str):
                    allowedKeys = str(allowedKeys)
                elif not ',' in allowedKeys:
                    allowedKeys = (allowedKeys,)
                else:
                    allowedKeys = eval(allowedKeys)
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(continue_listener.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(continue_listener.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if continue_listener.status == STARTED and not waitOnFlip:
            theseKeys = continue_listener.getKeys(keyList=list(allowedKeys), ignoreKeys=None, waitRelease=False)
            _continue_listener_allKeys.extend(theseKeys)
            if len(_continue_listener_allKeys):
                continue_listener.keys = [key.name for key in _continue_listener_allKeys]  # storing all keys
                continue_listener.rt = [key.rt for key in _continue_listener_allKeys]
                continue_listener.duration = [key.duration for key in _continue_listener_allKeys]
        
        # *instructions* updates
        
        # if instructions is starting this frame...
        if instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions.frameNStart = frameN  # exact frame index
            instructions.tStart = t  # local t and not account for scr refresh
            instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instructions.started')
            # update status
            instructions.status = STARTED
            instructions.setAutoDraw(True)
        
        # if instructions is active this frame...
        if instructions.status == STARTED:
            # update params
            pass
        # Run 'Each Frame' code from code_3
        if t_grayscreen_on is None:
            t_grayscreen_on = core.getTime()
            outlet.push_sample(['GRAYSCREEN_ON'])
        
        temp = continue_listener.getKeys()
        if len(temp) > 0:
             scanner_keys.append([key.value for key in temp])
             scanner_pulses.append(core.getTime())
             outlet.push_sample(['START_EXP'])
             continueRoutine = False
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instruc.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instruc.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instruc" ---
    for thisComponent in instruc.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instruc
    instruc.tStop = globalClock.getTime(format='float')
    instruc.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instruc.stopped', instruc.tStop)
    # check responses
    if continue_listener.keys in ['', [], None]:  # No response was made
        continue_listener.keys = None
    thisExp.addData('continue_listener.keys',continue_listener.keys)
    if continue_listener.keys != None:  # we had a response
        thisExp.addData('continue_listener.rt', continue_listener.rt)
        thisExp.addData('continue_listener.duration', continue_listener.duration)
    # Run 'End Routine' code from code_3
    for i in range(len(scanner_keys)):
        thisExpPulses.addData('time_grayscreen_on', t_grayscreen_on)
        thisExpPulses.addData('time0', None)
        thisExpPulses.addData('keys_pressed', scanner_keys[i])
        thisExpPulses.addData('time', scanner_pulses[i])
        thisExpPulses.nextEntry()
    thisExp.nextEntry()
    # the Routine "instruc" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "wait_trigger" ---
    # create an object to store info about Routine wait_trigger
    wait_trigger = data.Routine(
        name='wait_trigger',
        components=[trigger, wait],
    )
    wait_trigger.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for trigger
    trigger.keys = []
    trigger.rt = []
    _trigger_allKeys = []
    # Run 'Begin Routine' code from code_4
    scanner_keys = []
    scanner_pulses = []
    # store start times for wait_trigger
    wait_trigger.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    wait_trigger.tStart = globalClock.getTime(format='float')
    wait_trigger.status = STARTED
    thisExp.addData('wait_trigger.started', wait_trigger.tStart)
    wait_trigger.maxDuration = None
    # keep track of which components have finished
    wait_triggerComponents = wait_trigger.components
    for thisComponent in wait_trigger.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "wait_trigger" ---
    wait_trigger.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trigger* updates
        waitOnFlip = False
        
        # if trigger is starting this frame...
        if trigger.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trigger.frameNStart = frameN  # exact frame index
            trigger.tStart = t  # local t and not account for scr refresh
            trigger.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trigger, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trigger.started')
            # update status
            trigger.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(trigger.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(trigger.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if trigger.status == STARTED and not waitOnFlip:
            theseKeys = trigger.getKeys(keyList=['t', 'T', '5'], ignoreKeys=None, waitRelease=False)
            _trigger_allKeys.extend(theseKeys)
            if len(_trigger_allKeys):
                trigger.keys = _trigger_allKeys[-1].name  # just the last key pressed
                trigger.rt = _trigger_allKeys[-1].rt
                trigger.duration = _trigger_allKeys[-1].duration
        
        # *wait* updates
        
        # if wait is starting this frame...
        if wait.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wait.frameNStart = frameN  # exact frame index
            wait.tStart = t  # local t and not account for scr refresh
            wait.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wait, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'wait.started')
            # update status
            wait.status = STARTED
            wait.setAutoDraw(True)
        
        # if wait is active this frame...
        if wait.status == STARTED:
            # update params
            pass
        # Run 'Each Frame' code from code_4
        temp = trigger.getKeys()
        if len(temp) > 0:
            if time0 is None:
                time0 = core.getTime()
                outlet.push_sample(['TRIGGER'])
            scanner_pulses.append(time0)
            scanner_keys.append([key.value for key in temp])
            continueRoutine = False
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            wait_trigger.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in wait_trigger.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "wait_trigger" ---
    for thisComponent in wait_trigger.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for wait_trigger
    wait_trigger.tStop = globalClock.getTime(format='float')
    wait_trigger.tStopRefresh = tThisFlipGlobal
    thisExp.addData('wait_trigger.stopped', wait_trigger.tStop)
    # check responses
    if trigger.keys in ['', [], None]:  # No response was made
        trigger.keys = None
    thisExp.addData('trigger.keys',trigger.keys)
    if trigger.keys != None:  # we had a response
        thisExp.addData('trigger.rt', trigger.rt)
        thisExp.addData('trigger.duration', trigger.duration)
    # Run 'End Routine' code from code_4
    thisExpLog.addData('time_grayscreen_on', t_grayscreen_on)
    thisExpLog.addData('time0', time0)
    for i in range(len(scanner_keys)):
        thisExpPulses.addData('time_grayscreen_on', t_grayscreen_on)
        thisExpPulses.addData('time0', None)
        thisExpPulses.addData('keys_pressed', scanner_keys[i])
        thisExpPulses.addData('time', scanner_pulses[i])
        thisExpPulses.nextEntry()
    thisExp.nextEntry()
    # the Routine "wait_trigger" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "initial_frames" ---
    # create an object to store info about Routine initial_frames
    initial_frames = data.Routine(
        name='initial_frames',
        components=[listener1],
    )
    initial_frames.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for listener1
    listener1.keys = []
    listener1.rt = []
    _listener1_allKeys = []
    # allowedKeys looks like a variable, so make sure it exists locally
    if 'allowedKeys' in globals():
        allowedKeys = globals()['allowedKeys']
    # Run 'Begin Routine' code from code_2
    scanner_keys = []
    scanner_pulses = []
    
    wait_timer = core.CountdownTimer(wait_period)
    # store start times for initial_frames
    initial_frames.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    initial_frames.tStart = globalClock.getTime(format='float')
    initial_frames.status = STARTED
    thisExp.addData('initial_frames.started', initial_frames.tStart)
    initial_frames.maxDuration = None
    # keep track of which components have finished
    initial_framesComponents = initial_frames.components
    for thisComponent in initial_frames.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "initial_frames" ---
    initial_frames.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *listener1* updates
        waitOnFlip = False
        
        # if listener1 is starting this frame...
        if listener1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            listener1.frameNStart = frameN  # exact frame index
            listener1.tStart = t  # local t and not account for scr refresh
            listener1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(listener1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'listener1.started')
            # update status
            listener1.status = STARTED
            # allowed keys looks like a variable named `allowedKeys`
            if not type(allowedKeys) in [list, tuple, np.ndarray]:
                if not isinstance(allowedKeys, str):
                    allowedKeys = str(allowedKeys)
                elif not ',' in allowedKeys:
                    allowedKeys = (allowedKeys,)
                else:
                    allowedKeys = eval(allowedKeys)
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(listener1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(listener1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if listener1 is stopping this frame...
        if listener1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > listener1.tStartRefresh + wait_period+3-frameTolerance:
                # keep track of stop time/frame for later
                listener1.tStop = t  # not accounting for scr refresh
                listener1.tStopRefresh = tThisFlipGlobal  # on global time
                listener1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'listener1.stopped')
                # update status
                listener1.status = FINISHED
                listener1.status = FINISHED
        if listener1.status == STARTED and not waitOnFlip:
            theseKeys = listener1.getKeys(keyList=list(allowedKeys), ignoreKeys=None, waitRelease=False)
            _listener1_allKeys.extend(theseKeys)
            if len(_listener1_allKeys):
                listener1.keys = _listener1_allKeys[-1].name  # just the last key pressed
                listener1.rt = _listener1_allKeys[-1].rt
                listener1.duration = _listener1_allKeys[-1].duration
        # Run 'Each Frame' code from code_2
        temp = listener1.getKeys()
        
        t = wait_timer.getTime()
        
        if t > 0 and cross.status != STARTED:
            cross.setAutoDraw(True)
            cross.status = STARTED
        
        if t > 0 and t < signal_period:
            cross.setColor('black')
        
        if t <= 0:
            cross.status = FINISHED
            cross.setAutoDraw(False)
            continueRoutine = False
        
        
        if len(temp) > 0:
            scanner_pulses.append(core.getTime())
            scanner_keys.append([key.value for key in temp])
            
            if 'escape' in temp:
                outlet.push_sample(['END'])
                core.quit()
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            initial_frames.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in initial_frames.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "initial_frames" ---
    for thisComponent in initial_frames.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for initial_frames
    initial_frames.tStop = globalClock.getTime(format='float')
    initial_frames.tStopRefresh = tThisFlipGlobal
    thisExp.addData('initial_frames.stopped', initial_frames.tStop)
    
    
    # check responses
    if listener1.keys in ['', [], None]:  # No response was made
        listener1.keys = None
    thisExp.addData('listener1.keys',listener1.keys)
    if listener1.keys != None:  # we had a response
        thisExp.addData('listener1.rt', listener1.rt)
        thisExp.addData('listener1.duration', listener1.duration)
    # Run 'End Routine' code from code_2
    
    for i in range(len(scanner_keys)):
        thisExpPulses.addData('time_grayscreen_on', t_grayscreen_on)
        thisExpPulses.addData('time0', time0)
        thisExpPulses.addData('keys_pressed', scanner_keys[i])
        thisExpPulses.addData('time', scanner_pulses[i])
        thisExpPulses.nextEntry()
    
    
    thisExp.nextEntry()
    # the Routine "initial_frames" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    grasps = data.TrialHandler2(
        name='grasps',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions(conditionsFile), 
        seed=None, 
    )
    thisExp.addLoop(grasps)  # add the loop to the experiment
    thisGrasp = grasps.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisGrasp.rgb)
    if thisGrasp != None:
        for paramName in thisGrasp:
            globals()[paramName] = thisGrasp[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisGrasp in grasps:
        currentLoop = grasps
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisGrasp.rgb)
        if thisGrasp != None:
            for paramName in thisGrasp:
                globals()[paramName] = thisGrasp[paramName]
        
        # --- Prepare to start Routine "prompt" ---
        # create an object to store info about Routine prompt
        prompt = data.Routine(
            name='prompt',
            components=[listener_prompt],
        )
        prompt.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for listener_prompt
        listener_prompt.keys = []
        listener_prompt.rt = []
        _listener_prompt_allKeys = []
        # allowedKeys looks like a variable, so make sure it exists locally
        if 'allowedKeys' in globals():
            allowedKeys = globals()['allowedKeys']
        # Run 'Begin Routine' code from code
        
        grasp = image_stim[image]
        
        timer = core.CountdownTimer(2.5)
        fullTimer = core.CountdownTimer(5)
        
        scanner_keys = []
        scanner_pulses = []
        
        thisExpLog.addData('grasp', image)
        thisExpLog.addData('stimulusNumber', stimulusNum)
        thisExpLog.addData('side', side)
        thisExpLog.addData('position (pix)', screen_position[side])
        # store start times for prompt
        prompt.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        prompt.tStart = globalClock.getTime(format='float')
        prompt.status = STARTED
        thisExp.addData('prompt.started', prompt.tStart)
        prompt.maxDuration = None
        # keep track of which components have finished
        promptComponents = prompt.components
        for thisComponent in prompt.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "prompt" ---
        # if trial has changed, end Routine now
        if isinstance(grasps, data.TrialHandler2) and thisGrasp.thisN != grasps.thisTrial.thisN:
            continueRoutine = False
        prompt.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *listener_prompt* updates
            waitOnFlip = False
            
            # if listener_prompt is starting this frame...
            if listener_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                listener_prompt.frameNStart = frameN  # exact frame index
                listener_prompt.tStart = t  # local t and not account for scr refresh
                listener_prompt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(listener_prompt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'listener_prompt.started')
                # update status
                listener_prompt.status = STARTED
                # allowed keys looks like a variable named `allowedKeys`
                if not type(allowedKeys) in [list, tuple, np.ndarray]:
                    if not isinstance(allowedKeys, str):
                        allowedKeys = str(allowedKeys)
                    elif not ',' in allowedKeys:
                        allowedKeys = (allowedKeys,)
                    else:
                        allowedKeys = eval(allowedKeys)
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(listener_prompt.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(listener_prompt.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if listener_prompt.status == STARTED and not waitOnFlip:
                theseKeys = listener_prompt.getKeys(keyList=list(allowedKeys), ignoreKeys=None, waitRelease=False)
                _listener_prompt_allKeys.extend(theseKeys)
                if len(_listener_prompt_allKeys):
                    listener_prompt.keys = _listener_prompt_allKeys[-1].name  # just the last key pressed
                    listener_prompt.rt = _listener_prompt_allKeys[-1].rt
                    listener_prompt.duration = _listener_prompt_allKeys[-1].duration
            # Run 'Each Frame' code from code
            t = timer.getTime()
            t_full = fullTimer.getTime()
            
            if t > 0:
                if grasp.status != STARTED:
                    grasp.setAutoDraw(True)
                    go.setAutoDraw(True)
                    t_im_on = core.getTime()
                    thisExpLog.addData('image_onset', t_im_on)
                    thisExpLog.addData('go_cue_on', 'null')
                    outlet.push_sample(['IMG_ONSET_'+grasp.name])
                    outlet.push_sample(['GO_ONSET'])
                    grasp.status = STARTED
                    go.status = STARTED
                    
            if t <= 0:
                if grasp.status == STARTED:
                    grasp.setAutoDraw(False)
                    go.setAutoDraw(False)
                    t_im_off = core.getTime()
                    thisExpLog.addData('image_offset', t_im_off)
                    thisExpLog.addData('go_cue_off', 'null')
                    outlet.push_sample(['IMG_OFFSET_'+grasp.name])
                    grasp.status = FINISHED
                    go.status = FINISHED
            
            if t_full > 0 and t <=0:
                if stop.status != STARTED:
                    # stop signal
                    stop.setAutoDraw(True)
                    thisExpLog.addData('stop_cue_on', core.getTime())
                    outlet.push_sample(['STOP_ONSET'])
                    stop.status = STARTED
            
            if t_full <= 0:
                thisExpLog.addData('stop_cue_off', core.getTime())
                stop.setAutoDraw(False)
                stop.status = FINISHED
                continueRoutine = False
            
            temp = listener_prompt.getKeys()
            if len(temp) > 0:
                scanner_pulses.append(core.getTime())
                scanner_keys.append([key.value for key in temp])
                if 'escape' in temp:
                    outlet.push_sample(['END'])
                    core.quit()
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                prompt.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in prompt.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "prompt" ---
        for thisComponent in prompt.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for prompt
        prompt.tStop = globalClock.getTime(format='float')
        prompt.tStopRefresh = tThisFlipGlobal
        thisExp.addData('prompt.stopped', prompt.tStop)
        # check responses
        if listener_prompt.keys in ['', [], None]:  # No response was made
            listener_prompt.keys = None
        grasps.addData('listener_prompt.keys',listener_prompt.keys)
        if listener_prompt.keys != None:  # we had a response
            grasps.addData('listener_prompt.rt', listener_prompt.rt)
            grasps.addData('listener_prompt.duration', listener_prompt.duration)
        # Run 'End Routine' code from code
        trial = grasps.thisTrial
        
        win.flip()
        thisExpLog.addData('time0', time0)
        thisExpLog.addData('time_grayscreen_on', t_grayscreen_on)
        thisExpLog.nextEntry()
        
        for i in range(len(scanner_keys)):
            thisExpPulses.addData('time_grayscreen_on', t_grayscreen_on)
            thisExpPulses.addData('time0', time0)
            thisExpPulses.addData('keys_pressed', scanner_keys[i])
            thisExpPulses.addData('time', scanner_pulses[i])
            thisExpPulses.addData('stimulusNumber', stimulusNum)
            thisExpPulses.nextEntry()
        
        
        
        # the Routine "prompt" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        repeats = data.TrialHandler2(
            name='repeats',
            nReps=4.0, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
        )
        thisExp.addLoop(repeats)  # add the loop to the experiment
        thisRepeat = repeats.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisRepeat.rgb)
        if thisRepeat != None:
            for paramName in thisRepeat:
                globals()[paramName] = thisRepeat[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisRepeat in repeats:
            currentLoop = repeats
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisRepeat.rgb)
            if thisRepeat != None:
                for paramName in thisRepeat:
                    globals()[paramName] = thisRepeat[paramName]
            
            # --- Prepare to start Routine "trial" ---
            # create an object to store info about Routine trial
            trial = data.Routine(
                name='trial',
                components=[listener],
            )
            trial.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # create starting attributes for listener
            listener.keys = []
            listener.rt = []
            _listener_allKeys = []
            # allowedKeys looks like a variable, so make sure it exists locally
            if 'allowedKeys' in globals():
                allowedKeys = globals()['allowedKeys']
            # Run 'Begin Routine' code from code_5
            hold_dur = 3.5
            stop_dur = 2.5
            go_timer = core.CountdownTimer(hold_dur)
            stop_timer = core.CountdownTimer(hold_dur + stop_dur)
            
            scanner_keys = []
            scanner_pulses = []
            # store start times for trial
            trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            trial.tStart = globalClock.getTime(format='float')
            trial.status = STARTED
            thisExp.addData('trial.started', trial.tStart)
            trial.maxDuration = None
            # keep track of which components have finished
            trialComponents = trial.components
            for thisComponent in trial.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "trial" ---
            # if trial has changed, end Routine now
            if isinstance(repeats, data.TrialHandler2) and thisRepeat.thisN != repeats.thisTrial.thisN:
                continueRoutine = False
            trial.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *listener* updates
                waitOnFlip = False
                
                # if listener is starting this frame...
                if listener.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    listener.frameNStart = frameN  # exact frame index
                    listener.tStart = t  # local t and not account for scr refresh
                    listener.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(listener, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'listener.started')
                    # update status
                    listener.status = STARTED
                    # allowed keys looks like a variable named `allowedKeys`
                    if not type(allowedKeys) in [list, tuple, np.ndarray]:
                        if not isinstance(allowedKeys, str):
                            allowedKeys = str(allowedKeys)
                        elif not ',' in allowedKeys:
                            allowedKeys = (allowedKeys,)
                        else:
                            allowedKeys = eval(allowedKeys)
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(listener.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(listener.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if listener.status == STARTED and not waitOnFlip:
                    theseKeys = listener.getKeys(keyList=list(allowedKeys), ignoreKeys=None, waitRelease=False)
                    _listener_allKeys.extend(theseKeys)
                    if len(_listener_allKeys):
                        listener.keys = _listener_allKeys[-1].name  # just the last key pressed
                        listener.rt = _listener_allKeys[-1].rt
                        listener.duration = _listener_allKeys[-1].duration
                # Run 'Each Frame' code from code_5
                t_go = go_timer.getTime()
                t_stop = stop_timer.getTime()
                
                if t_go > 0 and go.status != STARTED:
                   go.setAutoDraw(True)
                   thisExpLog.addData('go_cue_on', core.getTime())
                   outlet.push_sample(['GO_ONSET'])
                   go.status = STARTED
                
                if t_go <= 0 and go.status != FINISHED:
                    go.setAutoDraw(False)
                    thisExpLog.addData('go_cue_off', core.getTime())
                    go.status = FINISHED
                    
                if t_stop > 0 and t_go <= 0:
                    if stop.status != STARTED:
                        thisExpLog.addData('stop_cue_on', core.getTime())
                        stop.setAutoDraw(True)
                        outlet.push_sample(['STOP_ONSET'])
                        stop.status = STARTED
                    
                if t_stop <= 0 and stop.status != FINISHED:
                    stop.setAutoDraw(False)
                    thisExpLog.addData('stop_cue_off', core.getTime())
                    stop.status = FINISHED
                    continueRoutine = False
                
                temp = listener.getKeys()
                if len(temp) > 0:
                    scanner_pulses.append(core.getTime())
                    scanner_keys.append([key.value for key in temp])
                    if 'escape' in temp:
                        outlet.push_sample(['END'])
                        core.quit()
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    trial.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial" ---
            for thisComponent in trial.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for trial
            trial.tStop = globalClock.getTime(format='float')
            trial.tStopRefresh = tThisFlipGlobal
            thisExp.addData('trial.stopped', trial.tStop)
            # check responses
            if listener.keys in ['', [], None]:  # No response was made
                listener.keys = None
            repeats.addData('listener.keys',listener.keys)
            if listener.keys != None:  # we had a response
                repeats.addData('listener.rt', listener.rt)
                repeats.addData('listener.duration', listener.duration)
            # Run 'End Routine' code from code_5
            thisExpLog.addData('stimulusNumber', stimulusNum)
            thisExpLog.addData('image_onset', 'null')
            thisExpLog.addData('image_offset', 'null')
            thisExpLog.addData('side', side)
            thisExpLog.addData('grasp', image)
            thisExpLog.addData('position (pix)', 'null')
            thisExpLog.nextEntry()
            
            for i in range(len(scanner_keys)):
                thisExpPulses.addData('time_grayscreen_on', t_grayscreen_on)
                thisExpPulses.addData('time0', time0)
                thisExpPulses.addData('keys_pressed', scanner_keys[i])
                thisExpPulses.addData('time', scanner_pulses[i])
                thisExpPulses.addData('stimulusNumber', stimulusNum)
                thisExpPulses.nextEntry()
            
            
            # the Routine "trial" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 4.0 repeats of 'repeats'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "interblock_interval" ---
        # create an object to store info about Routine interblock_interval
        interblock_interval = data.Routine(
            name='interblock_interval',
            components=[listener_break],
        )
        interblock_interval.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for listener_break
        listener_break.keys = []
        listener_break.rt = []
        _listener_break_allKeys = []
        # allowedKeys looks like a variable, so make sure it exists locally
        if 'allowedKeys' in globals():
            allowedKeys = globals()['allowedKeys']
        # Run 'Begin Routine' code from code_7
        scanner_keys = []
        scanner_pulses = []
        
        stimulusNum += 1
        
        break_timer = core.CountdownTimer(3.5)
        # store start times for interblock_interval
        interblock_interval.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        interblock_interval.tStart = globalClock.getTime(format='float')
        interblock_interval.status = STARTED
        thisExp.addData('interblock_interval.started', interblock_interval.tStart)
        interblock_interval.maxDuration = None
        # keep track of which components have finished
        interblock_intervalComponents = interblock_interval.components
        for thisComponent in interblock_interval.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "interblock_interval" ---
        # if trial has changed, end Routine now
        if isinstance(grasps, data.TrialHandler2) and thisGrasp.thisN != grasps.thisTrial.thisN:
            continueRoutine = False
        interblock_interval.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *listener_break* updates
            waitOnFlip = False
            
            # if listener_break is starting this frame...
            if listener_break.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                listener_break.frameNStart = frameN  # exact frame index
                listener_break.tStart = t  # local t and not account for scr refresh
                listener_break.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(listener_break, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'listener_break.started')
                # update status
                listener_break.status = STARTED
                # allowed keys looks like a variable named `allowedKeys`
                if not type(allowedKeys) in [list, tuple, np.ndarray]:
                    if not isinstance(allowedKeys, str):
                        allowedKeys = str(allowedKeys)
                    elif not ',' in allowedKeys:
                        allowedKeys = (allowedKeys,)
                    else:
                        allowedKeys = eval(allowedKeys)
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(listener_break.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(listener_break.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if listener_break.status == STARTED and not waitOnFlip:
                theseKeys = listener_break.getKeys(keyList=list(allowedKeys), ignoreKeys=None, waitRelease=False)
                _listener_break_allKeys.extend(theseKeys)
                if len(_listener_break_allKeys):
                    listener_break.keys = _listener_break_allKeys[-1].name  # just the last key pressed
                    listener_break.rt = _listener_break_allKeys[-1].rt
                    listener_break.duration = _listener_break_allKeys[-1].duration
            # Run 'Each Frame' code from code_7
            t = break_timer.getTime()
            
            if t > 0 and stop.status != STARTED:
                thisExpLog.addData('break_cue_on', core.getTime())
                outlet.push_sample(['BREAK_START'])
                stop.setAutoDraw(True)
                stop.status = STARTED
                
            if t <= 0 and stop.status != FINISHED:
                stop.setAutoDraw(False)
                thisExpLog.addData('break_cue_off', core.getTime())
                outlet.push_sample(['BREAK_END'])
                stop.status = FINISHED
                continueRoutine = False
            
            temp = listener_break.getKeys()
            if len(temp) > 0:
                scanner_pulses.append(core.getTime())
                scanner_keys.append([key.value for key in temp])
                if 'escape' in temp:
                    outlet.push_sample(['END'])
                    core.quit()
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                interblock_interval.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in interblock_interval.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "interblock_interval" ---
        for thisComponent in interblock_interval.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for interblock_interval
        interblock_interval.tStop = globalClock.getTime(format='float')
        interblock_interval.tStopRefresh = tThisFlipGlobal
        thisExp.addData('interblock_interval.stopped', interblock_interval.tStop)
        # check responses
        if listener_break.keys in ['', [], None]:  # No response was made
            listener_break.keys = None
        grasps.addData('listener_break.keys',listener_break.keys)
        if listener_break.keys != None:  # we had a response
            grasps.addData('listener_break.rt', listener_break.rt)
            grasps.addData('listener_break.duration', listener_break.duration)
        # Run 'End Routine' code from code_7
        for i in range(len(scanner_keys)):
            thisExpPulses.addData('time_grayscreen_on', t_grayscreen_on)
            thisExpPulses.addData('time0', time0)
            thisExpPulses.addData('keys_pressed', scanner_keys[i])
            thisExpPulses.addData('time', scanner_pulses[i])
            thisExpPulses.addData('stimulusNumber', stimulusNum)
            thisExpPulses.nextEntry()
        
        # the Routine "interblock_interval" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'grasps'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "end" ---
    # create an object to store info about Routine end
    end = data.Routine(
        name='end',
        components=[text, cross_end, listener_end],
    )
    end.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for listener_end
    listener_end.keys = []
    listener_end.rt = []
    _listener_end_allKeys = []
    # allowedKeys looks like a variable, so make sure it exists locally
    if 'allowedKeys' in globals():
        allowedKeys = globals()['allowedKeys']
    # Run 'Begin Routine' code from code_6
    scanner_keys = []
    scanner_pulses = []
    # store start times for end
    end.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    end.tStart = globalClock.getTime(format='float')
    end.status = STARTED
    thisExp.addData('end.started', end.tStart)
    end.maxDuration = None
    # keep track of which components have finished
    endComponents = end.components
    for thisComponent in end.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "end" ---
    end.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 7.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # if text is stopping this frame...
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.tStopRefresh = tThisFlipGlobal  # on global time
                text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.stopped')
                # update status
                text.status = FINISHED
                text.setAutoDraw(False)
        
        # *cross_end* updates
        
        # if cross_end is starting this frame...
        if cross_end.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            cross_end.frameNStart = frameN  # exact frame index
            cross_end.tStart = t  # local t and not account for scr refresh
            cross_end.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross_end, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cross_end.started')
            # update status
            cross_end.status = STARTED
            cross_end.setAutoDraw(True)
        
        # if cross_end is active this frame...
        if cross_end.status == STARTED:
            # update params
            pass
        
        # if cross_end is stopping this frame...
        if cross_end.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross_end.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                cross_end.tStop = t  # not accounting for scr refresh
                cross_end.tStopRefresh = tThisFlipGlobal  # on global time
                cross_end.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross_end.stopped')
                # update status
                cross_end.status = FINISHED
                cross_end.setAutoDraw(False)
        
        # *listener_end* updates
        waitOnFlip = False
        
        # if listener_end is starting this frame...
        if listener_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            listener_end.frameNStart = frameN  # exact frame index
            listener_end.tStart = t  # local t and not account for scr refresh
            listener_end.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(listener_end, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'listener_end.started')
            # update status
            listener_end.status = STARTED
            # allowed keys looks like a variable named `allowedKeys`
            if not type(allowedKeys) in [list, tuple, np.ndarray]:
                if not isinstance(allowedKeys, str):
                    allowedKeys = str(allowedKeys)
                elif not ',' in allowedKeys:
                    allowedKeys = (allowedKeys,)
                else:
                    allowedKeys = eval(allowedKeys)
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(listener_end.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(listener_end.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if listener_end is stopping this frame...
        if listener_end.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > listener_end.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                listener_end.tStop = t  # not accounting for scr refresh
                listener_end.tStopRefresh = tThisFlipGlobal  # on global time
                listener_end.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'listener_end.stopped')
                # update status
                listener_end.status = FINISHED
                listener_end.status = FINISHED
        if listener_end.status == STARTED and not waitOnFlip:
            theseKeys = listener_end.getKeys(keyList=list(allowedKeys), ignoreKeys=None, waitRelease=False)
            _listener_end_allKeys.extend(theseKeys)
            if len(_listener_end_allKeys):
                listener_end.keys = _listener_end_allKeys[-1].name  # just the last key pressed
                listener_end.rt = _listener_end_allKeys[-1].rt
                listener_end.duration = _listener_end_allKeys[-1].duration
        # Run 'Each Frame' code from code_6
        temp = listener_end.getKeys()
        if len(temp) > 0:
            scanner_pulses.append(core.getTime())
            scanner_keys.append([key.value for key in temp])
            if 'escape' in temp:
                outlet.push_sample(['END'])
                core.quit()
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            end.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "end" ---
    for thisComponent in end.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for end
    end.tStop = globalClock.getTime(format='float')
    end.tStopRefresh = tThisFlipGlobal
    thisExp.addData('end.stopped', end.tStop)
    # check responses
    if listener_end.keys in ['', [], None]:  # No response was made
        listener_end.keys = None
    thisExp.addData('listener_end.keys',listener_end.keys)
    if listener_end.keys != None:  # we had a response
        thisExp.addData('listener_end.rt', listener_end.rt)
        thisExp.addData('listener_end.duration', listener_end.duration)
    # Run 'End Routine' code from code_6
    for i in range(len(scanner_keys)):
        thisExpPulses.addData('time_grayscreen_on', t_grayscreen_on)
        thisExpPulses.addData('time0', time0)
        thisExpPulses.addData('keys_pressed', scanner_keys[i])
        thisExpPulses.addData('time', scanner_pulses[i])
        thisExpPulses.addData('stimulusNumber', stimulusNum)
        thisExpPulses.nextEntry()
    
    outlet.push_sample(['END'])
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if end.maxDurationReached:
        routineTimer.addTime(-end.maxDuration)
    elif end.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-7.000000)
    thisExp.nextEntry()
    
    
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
