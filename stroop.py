#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on July 10, 2025, at 23:41
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2024.2.4')


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

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.4'
expName = 'stroop'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
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
_winSize = [1536, 864]
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
        originPath='C:\\Users\\alvar\\OneDrive\\Escritorio\\Stroop_task\\stroop.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='alphabetical'
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
            monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0, 0, 0]
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
    if deviceManager.getDevice('key_next') is None:
        # initialise key_next
        key_next = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_next',
        )
    if deviceManager.getDevice('key_next_c') is None:
        # initialise key_next_c
        key_next_c = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_next_c',
        )
    if deviceManager.getDevice('respuesta_teclado_ensayo_C') is None:
        # initialise respuesta_teclado_ensayo_C
        respuesta_teclado_ensayo_C = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='respuesta_teclado_ensayo_C',
        )
    if deviceManager.getDevice('respuesta_teclado_C') is None:
        # initialise respuesta_teclado_C
        respuesta_teclado_C = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='respuesta_teclado_C',
        )
    if deviceManager.getDevice('respuesta_teclado_ensayo_PC') is None:
        # initialise respuesta_teclado_ensayo_PC
        respuesta_teclado_ensayo_PC = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='respuesta_teclado_ensayo_PC',
        )
    if deviceManager.getDevice('respuesta_teclado_PC') is None:
        # initialise respuesta_teclado_PC
        respuesta_teclado_PC = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='respuesta_teclado_PC',
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
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
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
    
    # --- Initialize components for Routine "instrucciones_generales" ---
    texto_instrucciones = visual.TextStim(win=win, name='texto_instrucciones',
        text='',
        font='Arial',
        units='height', pos=(0,0), draggable=False, height=0.04, wrapWidth=1.5, ori=0.0, 
        color='white', colorSpace='rgb', opacity=1.0, 
        languageStyle='LTR',
        depth=0.0);
    key_next = keyboard.Keyboard(deviceName='key_next')
    
    # --- Initialize components for Routine "instrucciones_especificas" ---
    texto_instrucciones_c = visual.TextStim(win=win, name='texto_instrucciones_c',
        text='',
        font='Arial',
        units='height', pos=(0, -0.05), draggable=False, height=0.05, wrapWidth=1.5, ori=0.0, 
        color='white', colorSpace='rgb', opacity=1.0, 
        languageStyle='LTR',
        depth=0.0);
    key_next_c = keyboard.Keyboard(deviceName='key_next_c')
    
    # --- Initialize components for Routine "ITI_inicial" ---
    cruz = visual.ShapeStim(
        win=win, name='cruz', vertices='cross',
        size=(0.1, 0.1),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    leyenda = visual.TextStim(win=win, name='leyenda',
        text='↑ = ROJO   ↓ = AZUL   ← = VERDE   → = AMARILLO',
        font='Arial',
        pos=(0, -0.35), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "ensayo_practica_c" ---
    texto_estimulo_ensayo_C = visual.TextStim(win=win, name='texto_estimulo_ensayo_C',
        text='',
        font='Arial',
        units='height', pos=(0, 0), draggable=False, height=0.2, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=1.0, 
        languageStyle='LTR',
        depth=0.0);
    respuesta_teclado_ensayo_C = keyboard.Keyboard(deviceName='respuesta_teclado_ensayo_C')
    CRUZ_ensayo_C = visual.ShapeStim(
        win=win, name='CRUZ_ensayo_C', vertices='cross',
        size=(0.1, 0.1),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-2.0, interpolate=True)
    feedback_text_C = visual.TextStim(win=win, name='feedback_text_C',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    leyenda_2 = visual.TextStim(win=win, name='leyenda_2',
        text='↑ = ROJO   ↓ = AZUL   ← = VERDE   → = AMARILLO',
        font='Arial',
        pos=(0, -0.35), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    
    # --- Initialize components for Routine "instrucciones_especificas" ---
    texto_instrucciones_c = visual.TextStim(win=win, name='texto_instrucciones_c',
        text='',
        font='Arial',
        units='height', pos=(0, -0.05), draggable=False, height=0.05, wrapWidth=1.5, ori=0.0, 
        color='white', colorSpace='rgb', opacity=1.0, 
        languageStyle='LTR',
        depth=0.0);
    key_next_c = keyboard.Keyboard(deviceName='key_next_c')
    
    # --- Initialize components for Routine "ITI_y_datos_C" ---
    cruz_2 = visual.ShapeStim(
        win=win, name='cruz_2', vertices='cross',
        size=(0.1, 0.1),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    # Run 'Begin Experiment' code from setup_c
    archivo_csv_C = "conditions/C/orden_c_p" + expInfo['participant'] + ".csv"
    
    leyenda_3 = visual.TextStim(win=win, name='leyenda_3',
        text='↑ = ROJO   ↓ = AZUL   ← = VERDE   → = AMARILLO',
        font='Arial',
        pos=(0, -0.35), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "condicion_c" ---
    texto_estimulo_C = visual.TextStim(win=win, name='texto_estimulo_C',
        text='',
        font='Arial',
        units='height', pos=(0, 0), draggable=False, height=0.2, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=1.0, 
        languageStyle='LTR',
        depth=0.0);
    respuesta_teclado_C = keyboard.Keyboard(deviceName='respuesta_teclado_C')
    CRUZ_C = visual.ShapeStim(
        win=win, name='CRUZ_C', vertices='cross',
        size=(0.1, 0.1),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-2.0, interpolate=True)
    leyenda_4 = visual.TextStim(win=win, name='leyenda_4',
        text='↑ = ROJO   ↓ = AZUL   ← = VERDE   → = AMARILLO',
        font='Arial',
        pos=(0, -0.35), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "instrucciones_especificas" ---
    texto_instrucciones_c = visual.TextStim(win=win, name='texto_instrucciones_c',
        text='',
        font='Arial',
        units='height', pos=(0, -0.05), draggable=False, height=0.05, wrapWidth=1.5, ori=0.0, 
        color='white', colorSpace='rgb', opacity=1.0, 
        languageStyle='LTR',
        depth=0.0);
    key_next_c = keyboard.Keyboard(deviceName='key_next_c')
    
    # --- Initialize components for Routine "ITI_inicial" ---
    cruz = visual.ShapeStim(
        win=win, name='cruz', vertices='cross',
        size=(0.1, 0.1),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    leyenda = visual.TextStim(win=win, name='leyenda',
        text='↑ = ROJO   ↓ = AZUL   ← = VERDE   → = AMARILLO',
        font='Arial',
        pos=(0, -0.35), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "ensayo_practica_PC" ---
    texto_estimulo_ensayo_PC = visual.TextStim(win=win, name='texto_estimulo_ensayo_PC',
        text='',
        font='Arial',
        units='height', pos=(0, 0), draggable=False, height=0.2, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=1.0, 
        languageStyle='LTR',
        depth=0.0);
    respuesta_teclado_ensayo_PC = keyboard.Keyboard(deviceName='respuesta_teclado_ensayo_PC')
    CRUZ_ensayo_PC = visual.ShapeStim(
        win=win, name='CRUZ_ensayo_PC', vertices='cross',
        size=(0.1, 0.1),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-2.0, interpolate=True)
    feedback_text_PC = visual.TextStim(win=win, name='feedback_text_PC',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    image_5 = visual.ImageStim(
        win=win,
        name='image_5', 
        image='resources/leyenda.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.35), draggable=False, size=(0.7, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    
    # --- Initialize components for Routine "instrucciones_especificas" ---
    texto_instrucciones_c = visual.TextStim(win=win, name='texto_instrucciones_c',
        text='',
        font='Arial',
        units='height', pos=(0, -0.05), draggable=False, height=0.05, wrapWidth=1.5, ori=0.0, 
        color='white', colorSpace='rgb', opacity=1.0, 
        languageStyle='LTR',
        depth=0.0);
    key_next_c = keyboard.Keyboard(deviceName='key_next_c')
    
    # --- Initialize components for Routine "ITI_y_datos_PC" ---
    cruz_3 = visual.ShapeStim(
        win=win, name='cruz_3', vertices='cross',
        size=(0.1, 0.1),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    # Run 'Begin Experiment' code from setup_pc
    archivo_csv_PC = "conditions/PC/orden_pc_p" + expInfo['participant'] + ".csv"
    
    image_6 = visual.ImageStim(
        win=win,
        name='image_6', 
        image='resources/leyenda.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.35), draggable=False, size=(0.7, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    
    # --- Initialize components for Routine "condicion_PC" ---
    texto_estimulo_PC = visual.TextStim(win=win, name='texto_estimulo_PC',
        text='',
        font='Arial',
        units='height', pos=(0, 0), draggable=False, height=0.2, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=1.0, 
        languageStyle='LTR',
        depth=0.0);
    respuesta_teclado_PC = keyboard.Keyboard(deviceName='respuesta_teclado_PC')
    CRUZ_PC = visual.ShapeStim(
        win=win, name='CRUZ_PC', vertices='cross',
        size=(0.1, 0.1),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-2.0, interpolate=True)
    image_7 = visual.ImageStim(
        win=win,
        name='image_7', 
        image='resources/leyenda.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.35), draggable=False, size=(0.7, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    
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
    
    # --- Prepare to start Routine "instrucciones_generales" ---
    # create an object to store info about Routine instrucciones_generales
    instrucciones_generales = data.Routine(
        name='instrucciones_generales',
        components=[texto_instrucciones, key_next],
    )
    instrucciones_generales.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    texto_instrucciones.setText('Durante esta tarea, verás palabras o cadenas de letras presentadas en distintos colores.\nTu tarea es indicar el color de la tinta, ignorando el significado de la palabra.\n\nResponde usando las siguientes teclas:\n↑  para ROJO  \n↓  para AZUL  \n←  para VERDE  \n→  para AMARILLO\n\nHabrá una leyenda visible en pantalla que te recordará estas asociaciones.\n\nIntenta responder lo más rápido y correctamente posible.\nSi no respondes dentro de 2500 ms, se contará como omisión.\n\nPresiona espacio para ir al bloque de practica.\n')
    # create starting attributes for key_next
    key_next.keys = []
    key_next.rt = []
    _key_next_allKeys = []
    # store start times for instrucciones_generales
    instrucciones_generales.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instrucciones_generales.tStart = globalClock.getTime(format='float')
    instrucciones_generales.status = STARTED
    thisExp.addData('instrucciones_generales.started', instrucciones_generales.tStart)
    instrucciones_generales.maxDuration = None
    # keep track of which components have finished
    instrucciones_generalesComponents = instrucciones_generales.components
    for thisComponent in instrucciones_generales.components:
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
    
    # --- Run Routine "instrucciones_generales" ---
    instrucciones_generales.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *texto_instrucciones* updates
        
        # if texto_instrucciones is starting this frame...
        if texto_instrucciones.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            texto_instrucciones.frameNStart = frameN  # exact frame index
            texto_instrucciones.tStart = t  # local t and not account for scr refresh
            texto_instrucciones.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(texto_instrucciones, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'texto_instrucciones.started')
            # update status
            texto_instrucciones.status = STARTED
            texto_instrucciones.setAutoDraw(True)
        
        # if texto_instrucciones is active this frame...
        if texto_instrucciones.status == STARTED:
            # update params
            pass
        
        # *key_next* updates
        waitOnFlip = False
        
        # if key_next is starting this frame...
        if key_next.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_next.frameNStart = frameN  # exact frame index
            key_next.tStart = t  # local t and not account for scr refresh
            key_next.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_next, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_next.started')
            # update status
            key_next.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_next.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_next.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_next.status == STARTED and not waitOnFlip:
            theseKeys = key_next.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_next_allKeys.extend(theseKeys)
            if len(_key_next_allKeys):
                key_next.keys = _key_next_allKeys[-1].name  # just the last key pressed
                key_next.rt = _key_next_allKeys[-1].rt
                key_next.duration = _key_next_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
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
            instrucciones_generales.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instrucciones_generales.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instrucciones_generales" ---
    for thisComponent in instrucciones_generales.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instrucciones_generales
    instrucciones_generales.tStop = globalClock.getTime(format='float')
    instrucciones_generales.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instrucciones_generales.stopped', instrucciones_generales.tStop)
    # check responses
    if key_next.keys in ['', [], None]:  # No response was made
        key_next.keys = None
    thisExp.addData('key_next.keys',key_next.keys)
    if key_next.keys != None:  # we had a response
        thisExp.addData('key_next.rt', key_next.rt)
        thisExp.addData('key_next.duration', key_next.duration)
    thisExp.nextEntry()
    # the Routine "instrucciones_generales" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instrucciones_especificas" ---
    # create an object to store info about Routine instrucciones_especificas
    instrucciones_especificas = data.Routine(
        name='instrucciones_especificas',
        components=[texto_instrucciones_c, key_next_c],
    )
    instrucciones_especificas.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    texto_instrucciones_c.setText('En este bloque verás figuras como “XXXX” presentadas en diferentes colores.  \nTu tarea es indicar el color de la tinta lo más rápido y correctamente posible.\n\nUsa las siguientes teclas:\n↑ = ROJO   ↓ = AZUL   ← = VERDE   → = AMARILLO\n\nRecuerda que la leyenda estará visible durante toda la tarea.\n\nPresiona la barra espaciadora para comenzar.')
    # create starting attributes for key_next_c
    key_next_c.keys = []
    key_next_c.rt = []
    _key_next_c_allKeys = []
    # store start times for instrucciones_especificas
    instrucciones_especificas.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instrucciones_especificas.tStart = globalClock.getTime(format='float')
    instrucciones_especificas.status = STARTED
    thisExp.addData('instrucciones_especificas.started', instrucciones_especificas.tStart)
    instrucciones_especificas.maxDuration = None
    # keep track of which components have finished
    instrucciones_especificasComponents = instrucciones_especificas.components
    for thisComponent in instrucciones_especificas.components:
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
    
    # --- Run Routine "instrucciones_especificas" ---
    instrucciones_especificas.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *texto_instrucciones_c* updates
        
        # if texto_instrucciones_c is starting this frame...
        if texto_instrucciones_c.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            texto_instrucciones_c.frameNStart = frameN  # exact frame index
            texto_instrucciones_c.tStart = t  # local t and not account for scr refresh
            texto_instrucciones_c.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(texto_instrucciones_c, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'texto_instrucciones_c.started')
            # update status
            texto_instrucciones_c.status = STARTED
            texto_instrucciones_c.setAutoDraw(True)
        
        # if texto_instrucciones_c is active this frame...
        if texto_instrucciones_c.status == STARTED:
            # update params
            pass
        
        # *key_next_c* updates
        waitOnFlip = False
        
        # if key_next_c is starting this frame...
        if key_next_c.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_next_c.frameNStart = frameN  # exact frame index
            key_next_c.tStart = t  # local t and not account for scr refresh
            key_next_c.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_next_c, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_next_c.started')
            # update status
            key_next_c.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_next_c.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_next_c.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_next_c.status == STARTED and not waitOnFlip:
            theseKeys = key_next_c.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_next_c_allKeys.extend(theseKeys)
            if len(_key_next_c_allKeys):
                key_next_c.keys = _key_next_c_allKeys[-1].name  # just the last key pressed
                key_next_c.rt = _key_next_c_allKeys[-1].rt
                key_next_c.duration = _key_next_c_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
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
            instrucciones_especificas.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instrucciones_especificas.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instrucciones_especificas" ---
    for thisComponent in instrucciones_especificas.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instrucciones_especificas
    instrucciones_especificas.tStop = globalClock.getTime(format='float')
    instrucciones_especificas.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instrucciones_especificas.stopped', instrucciones_especificas.tStop)
    # check responses
    if key_next_c.keys in ['', [], None]:  # No response was made
        key_next_c.keys = None
    thisExp.addData('key_next_c.keys',key_next_c.keys)
    if key_next_c.keys != None:  # we had a response
        thisExp.addData('key_next_c.rt', key_next_c.rt)
        thisExp.addData('key_next_c.duration', key_next_c.duration)
    thisExp.nextEntry()
    # the Routine "instrucciones_especificas" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ITI_inicial" ---
    # create an object to store info about Routine ITI_inicial
    ITI_inicial = data.Routine(
        name='ITI_inicial',
        components=[cruz, leyenda],
    )
    ITI_inicial.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for ITI_inicial
    ITI_inicial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    ITI_inicial.tStart = globalClock.getTime(format='float')
    ITI_inicial.status = STARTED
    thisExp.addData('ITI_inicial.started', ITI_inicial.tStart)
    ITI_inicial.maxDuration = None
    # keep track of which components have finished
    ITI_inicialComponents = ITI_inicial.components
    for thisComponent in ITI_inicial.components:
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
    
    # --- Run Routine "ITI_inicial" ---
    ITI_inicial.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cruz* updates
        
        # if cruz is starting this frame...
        if cruz.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cruz.frameNStart = frameN  # exact frame index
            cruz.tStart = t  # local t and not account for scr refresh
            cruz.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cruz, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cruz.started')
            # update status
            cruz.status = STARTED
            cruz.setAutoDraw(True)
        
        # if cruz is active this frame...
        if cruz.status == STARTED:
            # update params
            pass
        
        # if cruz is stopping this frame...
        if cruz.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cruz.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                cruz.tStop = t  # not accounting for scr refresh
                cruz.tStopRefresh = tThisFlipGlobal  # on global time
                cruz.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cruz.stopped')
                # update status
                cruz.status = FINISHED
                cruz.setAutoDraw(False)
        
        # *leyenda* updates
        
        # if leyenda is starting this frame...
        if leyenda.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            leyenda.frameNStart = frameN  # exact frame index
            leyenda.tStart = t  # local t and not account for scr refresh
            leyenda.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(leyenda, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'leyenda.started')
            # update status
            leyenda.status = STARTED
            leyenda.setAutoDraw(True)
        
        # if leyenda is active this frame...
        if leyenda.status == STARTED:
            # update params
            pass
        
        # if leyenda is stopping this frame...
        if leyenda.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > leyenda.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                leyenda.tStop = t  # not accounting for scr refresh
                leyenda.tStopRefresh = tThisFlipGlobal  # on global time
                leyenda.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'leyenda.stopped')
                # update status
                leyenda.status = FINISHED
                leyenda.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
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
            ITI_inicial.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITI_inicial.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ITI_inicial" ---
    for thisComponent in ITI_inicial.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for ITI_inicial
    ITI_inicial.tStop = globalClock.getTime(format='float')
    ITI_inicial.tStopRefresh = tThisFlipGlobal
    thisExp.addData('ITI_inicial.stopped', ITI_inicial.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if ITI_inicial.maxDurationReached:
        routineTimer.addTime(-ITI_inicial.maxDuration)
    elif ITI_inicial.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    practica_c = data.TrialHandler2(
        name='practica_c',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('conditions/practica/practica_C.csv'), 
        seed=None, 
    )
    thisExp.addLoop(practica_c)  # add the loop to the experiment
    thisPractica_c = practica_c.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractica_c.rgb)
    if thisPractica_c != None:
        for paramName in thisPractica_c:
            globals()[paramName] = thisPractica_c[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisPractica_c in practica_c:
        currentLoop = practica_c
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisPractica_c.rgb)
        if thisPractica_c != None:
            for paramName in thisPractica_c:
                globals()[paramName] = thisPractica_c[paramName]
        
        # --- Prepare to start Routine "ensayo_practica_c" ---
        # create an object to store info about Routine ensayo_practica_c
        ensayo_practica_c = data.Routine(
            name='ensayo_practica_c',
            components=[texto_estimulo_ensayo_C, respuesta_teclado_ensayo_C, CRUZ_ensayo_C, feedback_text_C, leyenda_2],
        )
        ensayo_practica_c.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        texto_estimulo_ensayo_C.setColor(color_tinta, colorSpace='rgb')
        texto_estimulo_ensayo_C.setText(palabra)
        # create starting attributes for respuesta_teclado_ensayo_C
        respuesta_teclado_ensayo_C.keys = []
        respuesta_teclado_ensayo_C.rt = []
        _respuesta_teclado_ensayo_C_allKeys = []
        # Run 'Begin Routine' code from Code_ensayo_C
        # Inicialización de variables
        respuesta_registrada = False
        tiempo_respuesta = None
        inicio_ensayo = globalClock.getTime()
        
        # Mostrar el estímulo y ocultar la cruz al comienzo
        texto_estimulo_ensayo_C.setAutoDraw(True)
        feedback_text_C.setAutoDraw(False)
        
        # store start times for ensayo_practica_c
        ensayo_practica_c.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        ensayo_practica_c.tStart = globalClock.getTime(format='float')
        ensayo_practica_c.status = STARTED
        thisExp.addData('ensayo_practica_c.started', ensayo_practica_c.tStart)
        ensayo_practica_c.maxDuration = None
        # keep track of which components have finished
        ensayo_practica_cComponents = ensayo_practica_c.components
        for thisComponent in ensayo_practica_c.components:
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
        
        # --- Run Routine "ensayo_practica_c" ---
        # if trial has changed, end Routine now
        if isinstance(practica_c, data.TrialHandler2) and thisPractica_c.thisN != practica_c.thisTrial.thisN:
            continueRoutine = False
        ensayo_practica_c.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *texto_estimulo_ensayo_C* updates
            
            # if texto_estimulo_ensayo_C is starting this frame...
            if texto_estimulo_ensayo_C.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                texto_estimulo_ensayo_C.frameNStart = frameN  # exact frame index
                texto_estimulo_ensayo_C.tStart = t  # local t and not account for scr refresh
                texto_estimulo_ensayo_C.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(texto_estimulo_ensayo_C, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'texto_estimulo_ensayo_C.started')
                # update status
                texto_estimulo_ensayo_C.status = STARTED
                texto_estimulo_ensayo_C.setAutoDraw(True)
            
            # if texto_estimulo_ensayo_C is active this frame...
            if texto_estimulo_ensayo_C.status == STARTED:
                # update params
                pass
            
            # if texto_estimulo_ensayo_C is stopping this frame...
            if texto_estimulo_ensayo_C.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > texto_estimulo_ensayo_C.tStartRefresh + 2.5-frameTolerance:
                    # keep track of stop time/frame for later
                    texto_estimulo_ensayo_C.tStop = t  # not accounting for scr refresh
                    texto_estimulo_ensayo_C.tStopRefresh = tThisFlipGlobal  # on global time
                    texto_estimulo_ensayo_C.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'texto_estimulo_ensayo_C.stopped')
                    # update status
                    texto_estimulo_ensayo_C.status = FINISHED
                    texto_estimulo_ensayo_C.setAutoDraw(False)
            
            # *respuesta_teclado_ensayo_C* updates
            waitOnFlip = False
            
            # if respuesta_teclado_ensayo_C is starting this frame...
            if respuesta_teclado_ensayo_C.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                respuesta_teclado_ensayo_C.frameNStart = frameN  # exact frame index
                respuesta_teclado_ensayo_C.tStart = t  # local t and not account for scr refresh
                respuesta_teclado_ensayo_C.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(respuesta_teclado_ensayo_C, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'respuesta_teclado_ensayo_C.started')
                # update status
                respuesta_teclado_ensayo_C.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(respuesta_teclado_ensayo_C.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(respuesta_teclado_ensayo_C.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if respuesta_teclado_ensayo_C is stopping this frame...
            if respuesta_teclado_ensayo_C.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > respuesta_teclado_ensayo_C.tStartRefresh + 2.5-frameTolerance:
                    # keep track of stop time/frame for later
                    respuesta_teclado_ensayo_C.tStop = t  # not accounting for scr refresh
                    respuesta_teclado_ensayo_C.tStopRefresh = tThisFlipGlobal  # on global time
                    respuesta_teclado_ensayo_C.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'respuesta_teclado_ensayo_C.stopped')
                    # update status
                    respuesta_teclado_ensayo_C.status = FINISHED
                    respuesta_teclado_ensayo_C.status = FINISHED
            if respuesta_teclado_ensayo_C.status == STARTED and not waitOnFlip:
                theseKeys = respuesta_teclado_ensayo_C.getKeys(keyList=['up','down','left','right'], ignoreKeys=["escape"], waitRelease=False)
                _respuesta_teclado_ensayo_C_allKeys.extend(theseKeys)
                if len(_respuesta_teclado_ensayo_C_allKeys):
                    respuesta_teclado_ensayo_C.keys = _respuesta_teclado_ensayo_C_allKeys[-1].name  # just the last key pressed
                    respuesta_teclado_ensayo_C.rt = _respuesta_teclado_ensayo_C_allKeys[-1].rt
                    respuesta_teclado_ensayo_C.duration = _respuesta_teclado_ensayo_C_allKeys[-1].duration
                    # was this correct?
                    if (respuesta_teclado_ensayo_C.keys == str(tecla_correcta)) or (respuesta_teclado_ensayo_C.keys == tecla_correcta):
                        respuesta_teclado_ensayo_C.corr = 1
                    else:
                        respuesta_teclado_ensayo_C.corr = 0
            
            # *CRUZ_ensayo_C* updates
            
            # if CRUZ_ensayo_C is starting this frame...
            if CRUZ_ensayo_C.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
                # keep track of start time/frame for later
                CRUZ_ensayo_C.frameNStart = frameN  # exact frame index
                CRUZ_ensayo_C.tStart = t  # local t and not account for scr refresh
                CRUZ_ensayo_C.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(CRUZ_ensayo_C, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'CRUZ_ensayo_C.started')
                # update status
                CRUZ_ensayo_C.status = STARTED
                CRUZ_ensayo_C.setAutoDraw(True)
            
            # if CRUZ_ensayo_C is active this frame...
            if CRUZ_ensayo_C.status == STARTED:
                # update params
                pass
            
            # if CRUZ_ensayo_C is stopping this frame...
            if CRUZ_ensayo_C.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > CRUZ_ensayo_C.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    CRUZ_ensayo_C.tStop = t  # not accounting for scr refresh
                    CRUZ_ensayo_C.tStopRefresh = tThisFlipGlobal  # on global time
                    CRUZ_ensayo_C.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'CRUZ_ensayo_C.stopped')
                    # update status
                    CRUZ_ensayo_C.status = FINISHED
                    CRUZ_ensayo_C.setAutoDraw(False)
            # Run 'Each Frame' code from Code_ensayo_C
            tiempo_actual = globalClock.getTime() - inicio_ensayo
            
            if respuesta_teclado_ensayo_C.keys and not respuesta_registrada:
                respuesta_registrada = True
                tiempo_respuesta = tiempo_actual
                texto_estimulo_ensayo_C.setAutoDraw(False)
                feedback_text_C.setAutoDraw(True)
                if respuesta_teclado_ensayo_C.corr == 1:
                    feedback_text_C.text = '✔'
                    feedback_text_C.color = 'green'
                else:
                    feedback_text_C.text = '✖'
                    feedback_text_C.color = 'red'
                respuesta_teclado_ensayo_C.status = FINISHED
            
            elif tiempo_actual >= 2.5 and not respuesta_registrada:
                respuesta_registrada = True
                texto_estimulo_ensayo_C.setAutoDraw(False)
                feedback_text_C.setAutoDraw(True)
                if respuesta_teclado_ensayo_C.corr == 1:
                    feedback_text_C.text = '✔'
                    feedback_text_C.color = 'green'
                else:
                    feedback_text_C.text = '✖'
                    feedback_text_C.color = 'red'
                respuesta_teclado_C.status = FINISHED
            
            elif tiempo_actual >= 3.0:
                continueRoutine = False
            
            
            # *feedback_text_C* updates
            
            # if feedback_text_C is starting this frame...
            if feedback_text_C.status == NOT_STARTED and False:
                # keep track of start time/frame for later
                feedback_text_C.frameNStart = frameN  # exact frame index
                feedback_text_C.tStart = t  # local t and not account for scr refresh
                feedback_text_C.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_text_C, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_text_C.started')
                # update status
                feedback_text_C.status = STARTED
                feedback_text_C.setAutoDraw(True)
            
            # if feedback_text_C is active this frame...
            if feedback_text_C.status == STARTED:
                # update params
                pass
            
            # *leyenda_2* updates
            
            # if leyenda_2 is starting this frame...
            if leyenda_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                leyenda_2.frameNStart = frameN  # exact frame index
                leyenda_2.tStart = t  # local t and not account for scr refresh
                leyenda_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(leyenda_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'leyenda_2.started')
                # update status
                leyenda_2.status = STARTED
                leyenda_2.setAutoDraw(True)
            
            # if leyenda_2 is active this frame...
            if leyenda_2.status == STARTED:
                # update params
                pass
            
            # if leyenda_2 is stopping this frame...
            if leyenda_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > leyenda_2.tStartRefresh + 3.5-frameTolerance:
                    # keep track of stop time/frame for later
                    leyenda_2.tStop = t  # not accounting for scr refresh
                    leyenda_2.tStopRefresh = tThisFlipGlobal  # on global time
                    leyenda_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'leyenda_2.stopped')
                    # update status
                    leyenda_2.status = FINISHED
                    leyenda_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
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
                ensayo_practica_c.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ensayo_practica_c.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ensayo_practica_c" ---
        for thisComponent in ensayo_practica_c.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for ensayo_practica_c
        ensayo_practica_c.tStop = globalClock.getTime(format='float')
        ensayo_practica_c.tStopRefresh = tThisFlipGlobal
        thisExp.addData('ensayo_practica_c.stopped', ensayo_practica_c.tStop)
        # check responses
        if respuesta_teclado_ensayo_C.keys in ['', [], None]:  # No response was made
            respuesta_teclado_ensayo_C.keys = None
            # was no response the correct answer?!
            if str(tecla_correcta).lower() == 'none':
               respuesta_teclado_ensayo_C.corr = 1;  # correct non-response
            else:
               respuesta_teclado_ensayo_C.corr = 0;  # failed to respond (incorrectly)
        # store data for practica_c (TrialHandler)
        practica_c.addData('respuesta_teclado_ensayo_C.keys',respuesta_teclado_ensayo_C.keys)
        practica_c.addData('respuesta_teclado_ensayo_C.corr', respuesta_teclado_ensayo_C.corr)
        if respuesta_teclado_ensayo_C.keys != None:  # we had a response
            practica_c.addData('respuesta_teclado_ensayo_C.rt', respuesta_teclado_ensayo_C.rt)
            practica_c.addData('respuesta_teclado_ensayo_C.duration', respuesta_teclado_ensayo_C.duration)
        # Run 'End Routine' code from Code_ensayo_C
        # Clasificación de la validez
        if tiempo_respuesta:
            if tiempo_respuesta < 0.2:
                validez = 'anticipada'
                respuesta_teclado_ensayo_C.corr = 0  # Forzar como incorrecta
            else:
                validez = 'valida'
        else:
            validez = 'omitida'
        
        # Guardar validez
        thisExp.addData('validez', validez)
        feedback_text_C.setAutoDraw(False)
        
        # Guardar datos
        thisExp.addData('RT', tiempo_respuesta if tiempo_respuesta else 'NA')
        thisExp.addData('key', respuesta_teclado_ensayo_C.keys)
        
        # the Routine "ensayo_practica_c" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'practica_c'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "instrucciones_especificas" ---
    # create an object to store info about Routine instrucciones_especificas
    instrucciones_especificas = data.Routine(
        name='instrucciones_especificas',
        components=[texto_instrucciones_c, key_next_c],
    )
    instrucciones_especificas.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    texto_instrucciones_c.setText('En este bloque verás figuras como “XXXX” presentadas en diferentes colores.  \nTu tarea es indicar el color de la tinta lo más rápido y correctamente posible.\n\nUsa las siguientes teclas:\n↑ = ROJO   ↓ = AZUL   ← = VERDE   → = AMARILLO\n\nRecuerda que la leyenda estará visible durante toda la tarea.\n\nPresiona la barra espaciadora para comenzar.')
    # create starting attributes for key_next_c
    key_next_c.keys = []
    key_next_c.rt = []
    _key_next_c_allKeys = []
    # store start times for instrucciones_especificas
    instrucciones_especificas.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instrucciones_especificas.tStart = globalClock.getTime(format='float')
    instrucciones_especificas.status = STARTED
    thisExp.addData('instrucciones_especificas.started', instrucciones_especificas.tStart)
    instrucciones_especificas.maxDuration = None
    # keep track of which components have finished
    instrucciones_especificasComponents = instrucciones_especificas.components
    for thisComponent in instrucciones_especificas.components:
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
    
    # --- Run Routine "instrucciones_especificas" ---
    instrucciones_especificas.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *texto_instrucciones_c* updates
        
        # if texto_instrucciones_c is starting this frame...
        if texto_instrucciones_c.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            texto_instrucciones_c.frameNStart = frameN  # exact frame index
            texto_instrucciones_c.tStart = t  # local t and not account for scr refresh
            texto_instrucciones_c.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(texto_instrucciones_c, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'texto_instrucciones_c.started')
            # update status
            texto_instrucciones_c.status = STARTED
            texto_instrucciones_c.setAutoDraw(True)
        
        # if texto_instrucciones_c is active this frame...
        if texto_instrucciones_c.status == STARTED:
            # update params
            pass
        
        # *key_next_c* updates
        waitOnFlip = False
        
        # if key_next_c is starting this frame...
        if key_next_c.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_next_c.frameNStart = frameN  # exact frame index
            key_next_c.tStart = t  # local t and not account for scr refresh
            key_next_c.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_next_c, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_next_c.started')
            # update status
            key_next_c.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_next_c.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_next_c.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_next_c.status == STARTED and not waitOnFlip:
            theseKeys = key_next_c.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_next_c_allKeys.extend(theseKeys)
            if len(_key_next_c_allKeys):
                key_next_c.keys = _key_next_c_allKeys[-1].name  # just the last key pressed
                key_next_c.rt = _key_next_c_allKeys[-1].rt
                key_next_c.duration = _key_next_c_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
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
            instrucciones_especificas.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instrucciones_especificas.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instrucciones_especificas" ---
    for thisComponent in instrucciones_especificas.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instrucciones_especificas
    instrucciones_especificas.tStop = globalClock.getTime(format='float')
    instrucciones_especificas.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instrucciones_especificas.stopped', instrucciones_especificas.tStop)
    # check responses
    if key_next_c.keys in ['', [], None]:  # No response was made
        key_next_c.keys = None
    thisExp.addData('key_next_c.keys',key_next_c.keys)
    if key_next_c.keys != None:  # we had a response
        thisExp.addData('key_next_c.rt', key_next_c.rt)
        thisExp.addData('key_next_c.duration', key_next_c.duration)
    thisExp.nextEntry()
    # the Routine "instrucciones_especificas" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ITI_y_datos_C" ---
    # create an object to store info about Routine ITI_y_datos_C
    ITI_y_datos_C = data.Routine(
        name='ITI_y_datos_C',
        components=[cruz_2, leyenda_3],
    )
    ITI_y_datos_C.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for ITI_y_datos_C
    ITI_y_datos_C.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    ITI_y_datos_C.tStart = globalClock.getTime(format='float')
    ITI_y_datos_C.status = STARTED
    thisExp.addData('ITI_y_datos_C.started', ITI_y_datos_C.tStart)
    ITI_y_datos_C.maxDuration = None
    # keep track of which components have finished
    ITI_y_datos_CComponents = ITI_y_datos_C.components
    for thisComponent in ITI_y_datos_C.components:
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
    
    # --- Run Routine "ITI_y_datos_C" ---
    ITI_y_datos_C.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cruz_2* updates
        
        # if cruz_2 is starting this frame...
        if cruz_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cruz_2.frameNStart = frameN  # exact frame index
            cruz_2.tStart = t  # local t and not account for scr refresh
            cruz_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cruz_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cruz_2.started')
            # update status
            cruz_2.status = STARTED
            cruz_2.setAutoDraw(True)
        
        # if cruz_2 is active this frame...
        if cruz_2.status == STARTED:
            # update params
            pass
        
        # if cruz_2 is stopping this frame...
        if cruz_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cruz_2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                cruz_2.tStop = t  # not accounting for scr refresh
                cruz_2.tStopRefresh = tThisFlipGlobal  # on global time
                cruz_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cruz_2.stopped')
                # update status
                cruz_2.status = FINISHED
                cruz_2.setAutoDraw(False)
        
        # *leyenda_3* updates
        
        # if leyenda_3 is starting this frame...
        if leyenda_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            leyenda_3.frameNStart = frameN  # exact frame index
            leyenda_3.tStart = t  # local t and not account for scr refresh
            leyenda_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(leyenda_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'leyenda_3.started')
            # update status
            leyenda_3.status = STARTED
            leyenda_3.setAutoDraw(True)
        
        # if leyenda_3 is active this frame...
        if leyenda_3.status == STARTED:
            # update params
            pass
        
        # if leyenda_3 is stopping this frame...
        if leyenda_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > leyenda_3.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                leyenda_3.tStop = t  # not accounting for scr refresh
                leyenda_3.tStopRefresh = tThisFlipGlobal  # on global time
                leyenda_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'leyenda_3.stopped')
                # update status
                leyenda_3.status = FINISHED
                leyenda_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
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
            ITI_y_datos_C.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITI_y_datos_C.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ITI_y_datos_C" ---
    for thisComponent in ITI_y_datos_C.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for ITI_y_datos_C
    ITI_y_datos_C.tStop = globalClock.getTime(format='float')
    ITI_y_datos_C.tStopRefresh = tThisFlipGlobal
    thisExp.addData('ITI_y_datos_C.stopped', ITI_y_datos_C.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if ITI_y_datos_C.maxDurationReached:
        routineTimer.addTime(-ITI_y_datos_C.maxDuration)
    elif ITI_y_datos_C.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    condicion_C = data.TrialHandler2(
        name='condicion_C',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions(archivo_csv_C), 
        seed=None, 
    )
    thisExp.addLoop(condicion_C)  # add the loop to the experiment
    thisCondicion_C = condicion_C.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCondicion_C.rgb)
    if thisCondicion_C != None:
        for paramName in thisCondicion_C:
            globals()[paramName] = thisCondicion_C[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisCondicion_C in condicion_C:
        currentLoop = condicion_C
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisCondicion_C.rgb)
        if thisCondicion_C != None:
            for paramName in thisCondicion_C:
                globals()[paramName] = thisCondicion_C[paramName]
        
        # --- Prepare to start Routine "condicion_c" ---
        # create an object to store info about Routine condicion_c
        condicion_c = data.Routine(
            name='condicion_c',
            components=[texto_estimulo_C, respuesta_teclado_C, CRUZ_C, leyenda_4],
        )
        condicion_c.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        texto_estimulo_C.setColor(color_tinta, colorSpace='rgb')
        texto_estimulo_C.setText(palabra)
        # create starting attributes for respuesta_teclado_C
        respuesta_teclado_C.keys = []
        respuesta_teclado_C.rt = []
        _respuesta_teclado_C_allKeys = []
        # Run 'Begin Routine' code from Code_C
        # Inicialización de variables
        respuesta_registrada = False
        tiempo_respuesta = None
        inicio_ensayo = globalClock.getTime()
        
        # Mostrar el estímulo y ocultar la cruz al comienzo
        texto_estimulo_C.setAutoDraw(True)
        CRUZ_C.setAutoDraw(False)
        
        # store start times for condicion_c
        condicion_c.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        condicion_c.tStart = globalClock.getTime(format='float')
        condicion_c.status = STARTED
        thisExp.addData('condicion_c.started', condicion_c.tStart)
        condicion_c.maxDuration = None
        # keep track of which components have finished
        condicion_cComponents = condicion_c.components
        for thisComponent in condicion_c.components:
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
        
        # --- Run Routine "condicion_c" ---
        # if trial has changed, end Routine now
        if isinstance(condicion_C, data.TrialHandler2) and thisCondicion_C.thisN != condicion_C.thisTrial.thisN:
            continueRoutine = False
        condicion_c.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *texto_estimulo_C* updates
            
            # if texto_estimulo_C is starting this frame...
            if texto_estimulo_C.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                texto_estimulo_C.frameNStart = frameN  # exact frame index
                texto_estimulo_C.tStart = t  # local t and not account for scr refresh
                texto_estimulo_C.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(texto_estimulo_C, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'texto_estimulo_C.started')
                # update status
                texto_estimulo_C.status = STARTED
                texto_estimulo_C.setAutoDraw(True)
            
            # if texto_estimulo_C is active this frame...
            if texto_estimulo_C.status == STARTED:
                # update params
                pass
            
            # if texto_estimulo_C is stopping this frame...
            if texto_estimulo_C.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > texto_estimulo_C.tStartRefresh + 2.5-frameTolerance:
                    # keep track of stop time/frame for later
                    texto_estimulo_C.tStop = t  # not accounting for scr refresh
                    texto_estimulo_C.tStopRefresh = tThisFlipGlobal  # on global time
                    texto_estimulo_C.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'texto_estimulo_C.stopped')
                    # update status
                    texto_estimulo_C.status = FINISHED
                    texto_estimulo_C.setAutoDraw(False)
            
            # *respuesta_teclado_C* updates
            waitOnFlip = False
            
            # if respuesta_teclado_C is starting this frame...
            if respuesta_teclado_C.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                respuesta_teclado_C.frameNStart = frameN  # exact frame index
                respuesta_teclado_C.tStart = t  # local t and not account for scr refresh
                respuesta_teclado_C.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(respuesta_teclado_C, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'respuesta_teclado_C.started')
                # update status
                respuesta_teclado_C.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(respuesta_teclado_C.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(respuesta_teclado_C.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if respuesta_teclado_C is stopping this frame...
            if respuesta_teclado_C.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > respuesta_teclado_C.tStartRefresh + 2.5-frameTolerance:
                    # keep track of stop time/frame for later
                    respuesta_teclado_C.tStop = t  # not accounting for scr refresh
                    respuesta_teclado_C.tStopRefresh = tThisFlipGlobal  # on global time
                    respuesta_teclado_C.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'respuesta_teclado_C.stopped')
                    # update status
                    respuesta_teclado_C.status = FINISHED
                    respuesta_teclado_C.status = FINISHED
            if respuesta_teclado_C.status == STARTED and not waitOnFlip:
                theseKeys = respuesta_teclado_C.getKeys(keyList=['up','down','left','right'], ignoreKeys=["escape"], waitRelease=False)
                _respuesta_teclado_C_allKeys.extend(theseKeys)
                if len(_respuesta_teclado_C_allKeys):
                    respuesta_teclado_C.keys = _respuesta_teclado_C_allKeys[-1].name  # just the last key pressed
                    respuesta_teclado_C.rt = _respuesta_teclado_C_allKeys[-1].rt
                    respuesta_teclado_C.duration = _respuesta_teclado_C_allKeys[-1].duration
                    # was this correct?
                    if (respuesta_teclado_C.keys == str(tecla_correcta)) or (respuesta_teclado_C.keys == tecla_correcta):
                        respuesta_teclado_C.corr = 1
                    else:
                        respuesta_teclado_C.corr = 0
            
            # *CRUZ_C* updates
            
            # if CRUZ_C is starting this frame...
            if CRUZ_C.status == NOT_STARTED and False:
                # keep track of start time/frame for later
                CRUZ_C.frameNStart = frameN  # exact frame index
                CRUZ_C.tStart = t  # local t and not account for scr refresh
                CRUZ_C.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(CRUZ_C, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'CRUZ_C.started')
                # update status
                CRUZ_C.status = STARTED
                CRUZ_C.setAutoDraw(True)
            
            # if CRUZ_C is active this frame...
            if CRUZ_C.status == STARTED:
                # update params
                pass
            # Run 'Each Frame' code from Code_C
            tiempo_actual = globalClock.getTime() - inicio_ensayo
            
            # Si responde antes del límite
            if respuesta_teclado_C.keys and not respuesta_registrada:
                respuesta_registrada = True
                tiempo_respuesta = tiempo_actual
                texto_estimulo_C.setAutoDraw(False)
                CRUZ_C.setAutoDraw(True)
                respuesta_teclado_C.status = FINISHED
            
            # Si no respondió y se agotaron los 2.5 s
            elif tiempo_actual >= 2.5 and not respuesta_registrada:
                respuesta_registrada = True
                texto_estimulo_C.setAutoDraw(False)
                CRUZ_C.setAutoDraw(True)
                respuesta_teclado_C.status = FINISHED
            # Terminar rutina al llegar a 3.0 s exactos
            elif tiempo_actual >= 3.0:
                continueRoutine = False
            
            # *leyenda_4* updates
            
            # if leyenda_4 is starting this frame...
            if leyenda_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                leyenda_4.frameNStart = frameN  # exact frame index
                leyenda_4.tStart = t  # local t and not account for scr refresh
                leyenda_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(leyenda_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'leyenda_4.started')
                # update status
                leyenda_4.status = STARTED
                leyenda_4.setAutoDraw(True)
            
            # if leyenda_4 is active this frame...
            if leyenda_4.status == STARTED:
                # update params
                pass
            
            # if leyenda_4 is stopping this frame...
            if leyenda_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > leyenda_4.tStartRefresh + 2.5-frameTolerance:
                    # keep track of stop time/frame for later
                    leyenda_4.tStop = t  # not accounting for scr refresh
                    leyenda_4.tStopRefresh = tThisFlipGlobal  # on global time
                    leyenda_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'leyenda_4.stopped')
                    # update status
                    leyenda_4.status = FINISHED
                    leyenda_4.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
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
                condicion_c.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in condicion_c.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "condicion_c" ---
        for thisComponent in condicion_c.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for condicion_c
        condicion_c.tStop = globalClock.getTime(format='float')
        condicion_c.tStopRefresh = tThisFlipGlobal
        thisExp.addData('condicion_c.stopped', condicion_c.tStop)
        # check responses
        if respuesta_teclado_C.keys in ['', [], None]:  # No response was made
            respuesta_teclado_C.keys = None
            # was no response the correct answer?!
            if str(tecla_correcta).lower() == 'none':
               respuesta_teclado_C.corr = 1;  # correct non-response
            else:
               respuesta_teclado_C.corr = 0;  # failed to respond (incorrectly)
        # store data for condicion_C (TrialHandler)
        condicion_C.addData('respuesta_teclado_C.keys',respuesta_teclado_C.keys)
        condicion_C.addData('respuesta_teclado_C.corr', respuesta_teclado_C.corr)
        if respuesta_teclado_C.keys != None:  # we had a response
            condicion_C.addData('respuesta_teclado_C.rt', respuesta_teclado_C.rt)
            condicion_C.addData('respuesta_teclado_C.duration', respuesta_teclado_C.duration)
        # Run 'End Routine' code from Code_C
        # Clasificación de la validez
        if tiempo_respuesta:
            if tiempo_respuesta < 0.2:
                validez = 'anticipada'
                respuesta_teclado_C.corr = 0  # Forzar como incorrecta
            else:
                validez = 'valida'
        else:
            validez = 'omitida'
        
        # Guardar validez
        thisExp.addData('validez', validez)
        CRUZ_C.setAutoDraw(False)
        
        # Guardar datos
        thisExp.addData('RT', tiempo_respuesta if tiempo_respuesta else 'NA')
        thisExp.addData('key', respuesta_teclado_C.keys)
        
        # the Routine "condicion_c" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'condicion_C'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "instrucciones_especificas" ---
    # create an object to store info about Routine instrucciones_especificas
    instrucciones_especificas = data.Routine(
        name='instrucciones_especificas',
        components=[texto_instrucciones_c, key_next_c],
    )
    instrucciones_especificas.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    texto_instrucciones_c.setText('En este bloque verás figuras como “XXXX” presentadas en diferentes colores.  \nTu tarea es indicar el color de la tinta lo más rápido y correctamente posible.\n\nUsa las siguientes teclas:\n↑ = ROJO   ↓ = AZUL   ← = VERDE   → = AMARILLO\n\nRecuerda que la leyenda estará visible durante toda la tarea.\n\nPresiona la barra espaciadora para comenzar.')
    # create starting attributes for key_next_c
    key_next_c.keys = []
    key_next_c.rt = []
    _key_next_c_allKeys = []
    # store start times for instrucciones_especificas
    instrucciones_especificas.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instrucciones_especificas.tStart = globalClock.getTime(format='float')
    instrucciones_especificas.status = STARTED
    thisExp.addData('instrucciones_especificas.started', instrucciones_especificas.tStart)
    instrucciones_especificas.maxDuration = None
    # keep track of which components have finished
    instrucciones_especificasComponents = instrucciones_especificas.components
    for thisComponent in instrucciones_especificas.components:
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
    
    # --- Run Routine "instrucciones_especificas" ---
    instrucciones_especificas.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *texto_instrucciones_c* updates
        
        # if texto_instrucciones_c is starting this frame...
        if texto_instrucciones_c.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            texto_instrucciones_c.frameNStart = frameN  # exact frame index
            texto_instrucciones_c.tStart = t  # local t and not account for scr refresh
            texto_instrucciones_c.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(texto_instrucciones_c, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'texto_instrucciones_c.started')
            # update status
            texto_instrucciones_c.status = STARTED
            texto_instrucciones_c.setAutoDraw(True)
        
        # if texto_instrucciones_c is active this frame...
        if texto_instrucciones_c.status == STARTED:
            # update params
            pass
        
        # *key_next_c* updates
        waitOnFlip = False
        
        # if key_next_c is starting this frame...
        if key_next_c.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_next_c.frameNStart = frameN  # exact frame index
            key_next_c.tStart = t  # local t and not account for scr refresh
            key_next_c.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_next_c, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_next_c.started')
            # update status
            key_next_c.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_next_c.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_next_c.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_next_c.status == STARTED and not waitOnFlip:
            theseKeys = key_next_c.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_next_c_allKeys.extend(theseKeys)
            if len(_key_next_c_allKeys):
                key_next_c.keys = _key_next_c_allKeys[-1].name  # just the last key pressed
                key_next_c.rt = _key_next_c_allKeys[-1].rt
                key_next_c.duration = _key_next_c_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
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
            instrucciones_especificas.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instrucciones_especificas.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instrucciones_especificas" ---
    for thisComponent in instrucciones_especificas.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instrucciones_especificas
    instrucciones_especificas.tStop = globalClock.getTime(format='float')
    instrucciones_especificas.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instrucciones_especificas.stopped', instrucciones_especificas.tStop)
    # check responses
    if key_next_c.keys in ['', [], None]:  # No response was made
        key_next_c.keys = None
    thisExp.addData('key_next_c.keys',key_next_c.keys)
    if key_next_c.keys != None:  # we had a response
        thisExp.addData('key_next_c.rt', key_next_c.rt)
        thisExp.addData('key_next_c.duration', key_next_c.duration)
    thisExp.nextEntry()
    # the Routine "instrucciones_especificas" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ITI_inicial" ---
    # create an object to store info about Routine ITI_inicial
    ITI_inicial = data.Routine(
        name='ITI_inicial',
        components=[cruz, leyenda],
    )
    ITI_inicial.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for ITI_inicial
    ITI_inicial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    ITI_inicial.tStart = globalClock.getTime(format='float')
    ITI_inicial.status = STARTED
    thisExp.addData('ITI_inicial.started', ITI_inicial.tStart)
    ITI_inicial.maxDuration = None
    # keep track of which components have finished
    ITI_inicialComponents = ITI_inicial.components
    for thisComponent in ITI_inicial.components:
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
    
    # --- Run Routine "ITI_inicial" ---
    ITI_inicial.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cruz* updates
        
        # if cruz is starting this frame...
        if cruz.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cruz.frameNStart = frameN  # exact frame index
            cruz.tStart = t  # local t and not account for scr refresh
            cruz.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cruz, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cruz.started')
            # update status
            cruz.status = STARTED
            cruz.setAutoDraw(True)
        
        # if cruz is active this frame...
        if cruz.status == STARTED:
            # update params
            pass
        
        # if cruz is stopping this frame...
        if cruz.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cruz.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                cruz.tStop = t  # not accounting for scr refresh
                cruz.tStopRefresh = tThisFlipGlobal  # on global time
                cruz.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cruz.stopped')
                # update status
                cruz.status = FINISHED
                cruz.setAutoDraw(False)
        
        # *leyenda* updates
        
        # if leyenda is starting this frame...
        if leyenda.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            leyenda.frameNStart = frameN  # exact frame index
            leyenda.tStart = t  # local t and not account for scr refresh
            leyenda.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(leyenda, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'leyenda.started')
            # update status
            leyenda.status = STARTED
            leyenda.setAutoDraw(True)
        
        # if leyenda is active this frame...
        if leyenda.status == STARTED:
            # update params
            pass
        
        # if leyenda is stopping this frame...
        if leyenda.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > leyenda.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                leyenda.tStop = t  # not accounting for scr refresh
                leyenda.tStopRefresh = tThisFlipGlobal  # on global time
                leyenda.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'leyenda.stopped')
                # update status
                leyenda.status = FINISHED
                leyenda.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
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
            ITI_inicial.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITI_inicial.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ITI_inicial" ---
    for thisComponent in ITI_inicial.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for ITI_inicial
    ITI_inicial.tStop = globalClock.getTime(format='float')
    ITI_inicial.tStopRefresh = tThisFlipGlobal
    thisExp.addData('ITI_inicial.stopped', ITI_inicial.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if ITI_inicial.maxDurationReached:
        routineTimer.addTime(-ITI_inicial.maxDuration)
    elif ITI_inicial.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    practica_PC = data.TrialHandler2(
        name='practica_PC',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('conditions/practica/practica_PC.csv'), 
        seed=None, 
    )
    thisExp.addLoop(practica_PC)  # add the loop to the experiment
    thisPractica_PC = practica_PC.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractica_PC.rgb)
    if thisPractica_PC != None:
        for paramName in thisPractica_PC:
            globals()[paramName] = thisPractica_PC[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisPractica_PC in practica_PC:
        currentLoop = practica_PC
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisPractica_PC.rgb)
        if thisPractica_PC != None:
            for paramName in thisPractica_PC:
                globals()[paramName] = thisPractica_PC[paramName]
        
        # --- Prepare to start Routine "ensayo_practica_PC" ---
        # create an object to store info about Routine ensayo_practica_PC
        ensayo_practica_PC = data.Routine(
            name='ensayo_practica_PC',
            components=[texto_estimulo_ensayo_PC, respuesta_teclado_ensayo_PC, CRUZ_ensayo_PC, feedback_text_PC, image_5],
        )
        ensayo_practica_PC.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        texto_estimulo_ensayo_PC.setColor(color_tinta, colorSpace='rgb')
        texto_estimulo_ensayo_PC.setText(palabra)
        # create starting attributes for respuesta_teclado_ensayo_PC
        respuesta_teclado_ensayo_PC.keys = []
        respuesta_teclado_ensayo_PC.rt = []
        _respuesta_teclado_ensayo_PC_allKeys = []
        # Run 'Begin Routine' code from Code_ensayo_PC
        # Inicialización de variables
        respuesta_registrada = False
        tiempo_respuesta = None
        inicio_ensayo = globalClock.getTime()
        
        # Mostrar el estímulo y ocultar la cruz al comienzo
        texto_estimulo_ensayo_PC.setAutoDraw(True)
        feedback_text_PC.setAutoDraw(False)
        
        # store start times for ensayo_practica_PC
        ensayo_practica_PC.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        ensayo_practica_PC.tStart = globalClock.getTime(format='float')
        ensayo_practica_PC.status = STARTED
        thisExp.addData('ensayo_practica_PC.started', ensayo_practica_PC.tStart)
        ensayo_practica_PC.maxDuration = None
        # keep track of which components have finished
        ensayo_practica_PCComponents = ensayo_practica_PC.components
        for thisComponent in ensayo_practica_PC.components:
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
        
        # --- Run Routine "ensayo_practica_PC" ---
        # if trial has changed, end Routine now
        if isinstance(practica_PC, data.TrialHandler2) and thisPractica_PC.thisN != practica_PC.thisTrial.thisN:
            continueRoutine = False
        ensayo_practica_PC.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *texto_estimulo_ensayo_PC* updates
            
            # if texto_estimulo_ensayo_PC is starting this frame...
            if texto_estimulo_ensayo_PC.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                texto_estimulo_ensayo_PC.frameNStart = frameN  # exact frame index
                texto_estimulo_ensayo_PC.tStart = t  # local t and not account for scr refresh
                texto_estimulo_ensayo_PC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(texto_estimulo_ensayo_PC, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'texto_estimulo_ensayo_PC.started')
                # update status
                texto_estimulo_ensayo_PC.status = STARTED
                texto_estimulo_ensayo_PC.setAutoDraw(True)
            
            # if texto_estimulo_ensayo_PC is active this frame...
            if texto_estimulo_ensayo_PC.status == STARTED:
                # update params
                pass
            
            # if texto_estimulo_ensayo_PC is stopping this frame...
            if texto_estimulo_ensayo_PC.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > texto_estimulo_ensayo_PC.tStartRefresh + 2.5-frameTolerance:
                    # keep track of stop time/frame for later
                    texto_estimulo_ensayo_PC.tStop = t  # not accounting for scr refresh
                    texto_estimulo_ensayo_PC.tStopRefresh = tThisFlipGlobal  # on global time
                    texto_estimulo_ensayo_PC.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'texto_estimulo_ensayo_PC.stopped')
                    # update status
                    texto_estimulo_ensayo_PC.status = FINISHED
                    texto_estimulo_ensayo_PC.setAutoDraw(False)
            
            # *respuesta_teclado_ensayo_PC* updates
            waitOnFlip = False
            
            # if respuesta_teclado_ensayo_PC is starting this frame...
            if respuesta_teclado_ensayo_PC.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                respuesta_teclado_ensayo_PC.frameNStart = frameN  # exact frame index
                respuesta_teclado_ensayo_PC.tStart = t  # local t and not account for scr refresh
                respuesta_teclado_ensayo_PC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(respuesta_teclado_ensayo_PC, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'respuesta_teclado_ensayo_PC.started')
                # update status
                respuesta_teclado_ensayo_PC.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(respuesta_teclado_ensayo_PC.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(respuesta_teclado_ensayo_PC.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if respuesta_teclado_ensayo_PC is stopping this frame...
            if respuesta_teclado_ensayo_PC.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > respuesta_teclado_ensayo_PC.tStartRefresh + 2.5-frameTolerance:
                    # keep track of stop time/frame for later
                    respuesta_teclado_ensayo_PC.tStop = t  # not accounting for scr refresh
                    respuesta_teclado_ensayo_PC.tStopRefresh = tThisFlipGlobal  # on global time
                    respuesta_teclado_ensayo_PC.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'respuesta_teclado_ensayo_PC.stopped')
                    # update status
                    respuesta_teclado_ensayo_PC.status = FINISHED
                    respuesta_teclado_ensayo_PC.status = FINISHED
            if respuesta_teclado_ensayo_PC.status == STARTED and not waitOnFlip:
                theseKeys = respuesta_teclado_ensayo_PC.getKeys(keyList=['up','down','left','right'], ignoreKeys=["escape"], waitRelease=False)
                _respuesta_teclado_ensayo_PC_allKeys.extend(theseKeys)
                if len(_respuesta_teclado_ensayo_PC_allKeys):
                    respuesta_teclado_ensayo_PC.keys = _respuesta_teclado_ensayo_PC_allKeys[-1].name  # just the last key pressed
                    respuesta_teclado_ensayo_PC.rt = _respuesta_teclado_ensayo_PC_allKeys[-1].rt
                    respuesta_teclado_ensayo_PC.duration = _respuesta_teclado_ensayo_PC_allKeys[-1].duration
                    # was this correct?
                    if (respuesta_teclado_ensayo_PC.keys == str(tecla_correcta)) or (respuesta_teclado_ensayo_PC.keys == tecla_correcta):
                        respuesta_teclado_ensayo_PC.corr = 1
                    else:
                        respuesta_teclado_ensayo_PC.corr = 0
            
            # *CRUZ_ensayo_PC* updates
            
            # if CRUZ_ensayo_PC is starting this frame...
            if CRUZ_ensayo_PC.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
                # keep track of start time/frame for later
                CRUZ_ensayo_PC.frameNStart = frameN  # exact frame index
                CRUZ_ensayo_PC.tStart = t  # local t and not account for scr refresh
                CRUZ_ensayo_PC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(CRUZ_ensayo_PC, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'CRUZ_ensayo_PC.started')
                # update status
                CRUZ_ensayo_PC.status = STARTED
                CRUZ_ensayo_PC.setAutoDraw(True)
            
            # if CRUZ_ensayo_PC is active this frame...
            if CRUZ_ensayo_PC.status == STARTED:
                # update params
                pass
            
            # if CRUZ_ensayo_PC is stopping this frame...
            if CRUZ_ensayo_PC.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > CRUZ_ensayo_PC.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    CRUZ_ensayo_PC.tStop = t  # not accounting for scr refresh
                    CRUZ_ensayo_PC.tStopRefresh = tThisFlipGlobal  # on global time
                    CRUZ_ensayo_PC.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'CRUZ_ensayo_PC.stopped')
                    # update status
                    CRUZ_ensayo_PC.status = FINISHED
                    CRUZ_ensayo_PC.setAutoDraw(False)
            # Run 'Each Frame' code from Code_ensayo_PC
            tiempo_actual = globalClock.getTime() - inicio_ensayo
            
            if respuesta_teclado_ensayo_PC.keys and not respuesta_registrada:
                respuesta_registrada = True
                tiempo_respuesta = tiempo_actual
                texto_estimulo_ensayo_PC.setAutoDraw(False)
                feedback_text_PC.setAutoDraw(True)
                if respuesta_teclado_ensayo_PC.corr == 1:
                    feedback_text_PC.text = '✔'
                    feedback_text_PC.color = 'green'
                else:
                    feedback_text_PC.text = '✖'
                    feedback_text_PC.color = 'red'
                respuesta_teclado_ensayo_PC.status = FINISHED
            
            elif tiempo_actual >= 2.5 and not respuesta_registrada:
                respuesta_registrada = True
                texto_estimulo_ensayo_PC.setAutoDraw(False)
                feedback_text_PC.setAutoDraw(True)
                if respuesta_teclado_ensayo_PC.corr == 1:
                    feedback_text_PC.text = '✔'
                    feedback_text_PC.color = 'green'
                else:
                    feedback_text_PC.text = '✖'
                    feedback_text_PC.color = 'red'
                respuesta_teclado_ensayo_PC.status = FINISHED
            
            elif tiempo_actual >= 3.0:
                continueRoutine = False
            
            
            # *feedback_text_PC* updates
            
            # if feedback_text_PC is starting this frame...
            if feedback_text_PC.status == NOT_STARTED and False:
                # keep track of start time/frame for later
                feedback_text_PC.frameNStart = frameN  # exact frame index
                feedback_text_PC.tStart = t  # local t and not account for scr refresh
                feedback_text_PC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_text_PC, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_text_PC.started')
                # update status
                feedback_text_PC.status = STARTED
                feedback_text_PC.setAutoDraw(True)
            
            # if feedback_text_PC is active this frame...
            if feedback_text_PC.status == STARTED:
                # update params
                pass
            
            # *image_5* updates
            
            # if image_5 is starting this frame...
            if image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_5.frameNStart = frameN  # exact frame index
                image_5.tStart = t  # local t and not account for scr refresh
                image_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_5.started')
                # update status
                image_5.status = STARTED
                image_5.setAutoDraw(True)
            
            # if image_5 is active this frame...
            if image_5.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
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
                ensayo_practica_PC.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ensayo_practica_PC.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ensayo_practica_PC" ---
        for thisComponent in ensayo_practica_PC.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for ensayo_practica_PC
        ensayo_practica_PC.tStop = globalClock.getTime(format='float')
        ensayo_practica_PC.tStopRefresh = tThisFlipGlobal
        thisExp.addData('ensayo_practica_PC.stopped', ensayo_practica_PC.tStop)
        # check responses
        if respuesta_teclado_ensayo_PC.keys in ['', [], None]:  # No response was made
            respuesta_teclado_ensayo_PC.keys = None
            # was no response the correct answer?!
            if str(tecla_correcta).lower() == 'none':
               respuesta_teclado_ensayo_PC.corr = 1;  # correct non-response
            else:
               respuesta_teclado_ensayo_PC.corr = 0;  # failed to respond (incorrectly)
        # store data for practica_PC (TrialHandler)
        practica_PC.addData('respuesta_teclado_ensayo_PC.keys',respuesta_teclado_ensayo_PC.keys)
        practica_PC.addData('respuesta_teclado_ensayo_PC.corr', respuesta_teclado_ensayo_PC.corr)
        if respuesta_teclado_ensayo_PC.keys != None:  # we had a response
            practica_PC.addData('respuesta_teclado_ensayo_PC.rt', respuesta_teclado_ensayo_PC.rt)
            practica_PC.addData('respuesta_teclado_ensayo_PC.duration', respuesta_teclado_ensayo_PC.duration)
        # Run 'End Routine' code from Code_ensayo_PC
        # Clasificación de la validez
        if tiempo_respuesta:
            if tiempo_respuesta < 0.2:
                validez = 'anticipada'
                respuesta_teclado_ensayo_PC.corr = 0  # Forzar como incorrecta
            else:
                validez = 'valida'
        else:
            validez = 'omitida'
        
        # Guardar validez
        thisExp.addData('validez', validez)
        feedback_text_PC.setAutoDraw(False)
        
        # Guardar datos
        thisExp.addData('RT', tiempo_respuesta if tiempo_respuesta else 'NA')
        thisExp.addData('key', respuesta_teclado_ensayo_PC.keys)
        
        # the Routine "ensayo_practica_PC" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'practica_PC'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "instrucciones_especificas" ---
    # create an object to store info about Routine instrucciones_especificas
    instrucciones_especificas = data.Routine(
        name='instrucciones_especificas',
        components=[texto_instrucciones_c, key_next_c],
    )
    instrucciones_especificas.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    texto_instrucciones_c.setText('En este bloque verás figuras como “XXXX” presentadas en diferentes colores.  \nTu tarea es indicar el color de la tinta lo más rápido y correctamente posible.\n\nUsa las siguientes teclas:\n↑ = ROJO   ↓ = AZUL   ← = VERDE   → = AMARILLO\n\nRecuerda que la leyenda estará visible durante toda la tarea.\n\nPresiona la barra espaciadora para comenzar.')
    # create starting attributes for key_next_c
    key_next_c.keys = []
    key_next_c.rt = []
    _key_next_c_allKeys = []
    # store start times for instrucciones_especificas
    instrucciones_especificas.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instrucciones_especificas.tStart = globalClock.getTime(format='float')
    instrucciones_especificas.status = STARTED
    thisExp.addData('instrucciones_especificas.started', instrucciones_especificas.tStart)
    instrucciones_especificas.maxDuration = None
    # keep track of which components have finished
    instrucciones_especificasComponents = instrucciones_especificas.components
    for thisComponent in instrucciones_especificas.components:
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
    
    # --- Run Routine "instrucciones_especificas" ---
    instrucciones_especificas.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *texto_instrucciones_c* updates
        
        # if texto_instrucciones_c is starting this frame...
        if texto_instrucciones_c.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            texto_instrucciones_c.frameNStart = frameN  # exact frame index
            texto_instrucciones_c.tStart = t  # local t and not account for scr refresh
            texto_instrucciones_c.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(texto_instrucciones_c, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'texto_instrucciones_c.started')
            # update status
            texto_instrucciones_c.status = STARTED
            texto_instrucciones_c.setAutoDraw(True)
        
        # if texto_instrucciones_c is active this frame...
        if texto_instrucciones_c.status == STARTED:
            # update params
            pass
        
        # *key_next_c* updates
        waitOnFlip = False
        
        # if key_next_c is starting this frame...
        if key_next_c.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_next_c.frameNStart = frameN  # exact frame index
            key_next_c.tStart = t  # local t and not account for scr refresh
            key_next_c.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_next_c, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_next_c.started')
            # update status
            key_next_c.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_next_c.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_next_c.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_next_c.status == STARTED and not waitOnFlip:
            theseKeys = key_next_c.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_next_c_allKeys.extend(theseKeys)
            if len(_key_next_c_allKeys):
                key_next_c.keys = _key_next_c_allKeys[-1].name  # just the last key pressed
                key_next_c.rt = _key_next_c_allKeys[-1].rt
                key_next_c.duration = _key_next_c_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
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
            instrucciones_especificas.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instrucciones_especificas.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instrucciones_especificas" ---
    for thisComponent in instrucciones_especificas.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instrucciones_especificas
    instrucciones_especificas.tStop = globalClock.getTime(format='float')
    instrucciones_especificas.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instrucciones_especificas.stopped', instrucciones_especificas.tStop)
    # check responses
    if key_next_c.keys in ['', [], None]:  # No response was made
        key_next_c.keys = None
    thisExp.addData('key_next_c.keys',key_next_c.keys)
    if key_next_c.keys != None:  # we had a response
        thisExp.addData('key_next_c.rt', key_next_c.rt)
        thisExp.addData('key_next_c.duration', key_next_c.duration)
    thisExp.nextEntry()
    # the Routine "instrucciones_especificas" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ITI_y_datos_PC" ---
    # create an object to store info about Routine ITI_y_datos_PC
    ITI_y_datos_PC = data.Routine(
        name='ITI_y_datos_PC',
        components=[cruz_3, image_6],
    )
    ITI_y_datos_PC.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for ITI_y_datos_PC
    ITI_y_datos_PC.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    ITI_y_datos_PC.tStart = globalClock.getTime(format='float')
    ITI_y_datos_PC.status = STARTED
    thisExp.addData('ITI_y_datos_PC.started', ITI_y_datos_PC.tStart)
    ITI_y_datos_PC.maxDuration = None
    # keep track of which components have finished
    ITI_y_datos_PCComponents = ITI_y_datos_PC.components
    for thisComponent in ITI_y_datos_PC.components:
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
    
    # --- Run Routine "ITI_y_datos_PC" ---
    ITI_y_datos_PC.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cruz_3* updates
        
        # if cruz_3 is starting this frame...
        if cruz_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cruz_3.frameNStart = frameN  # exact frame index
            cruz_3.tStart = t  # local t and not account for scr refresh
            cruz_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cruz_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cruz_3.started')
            # update status
            cruz_3.status = STARTED
            cruz_3.setAutoDraw(True)
        
        # if cruz_3 is active this frame...
        if cruz_3.status == STARTED:
            # update params
            pass
        
        # if cruz_3 is stopping this frame...
        if cruz_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cruz_3.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                cruz_3.tStop = t  # not accounting for scr refresh
                cruz_3.tStopRefresh = tThisFlipGlobal  # on global time
                cruz_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cruz_3.stopped')
                # update status
                cruz_3.status = FINISHED
                cruz_3.setAutoDraw(False)
        
        # *image_6* updates
        
        # if image_6 is starting this frame...
        if image_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_6.frameNStart = frameN  # exact frame index
            image_6.tStart = t  # local t and not account for scr refresh
            image_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_6.started')
            # update status
            image_6.status = STARTED
            image_6.setAutoDraw(True)
        
        # if image_6 is active this frame...
        if image_6.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
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
            ITI_y_datos_PC.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITI_y_datos_PC.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ITI_y_datos_PC" ---
    for thisComponent in ITI_y_datos_PC.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for ITI_y_datos_PC
    ITI_y_datos_PC.tStop = globalClock.getTime(format='float')
    ITI_y_datos_PC.tStopRefresh = tThisFlipGlobal
    thisExp.addData('ITI_y_datos_PC.stopped', ITI_y_datos_PC.tStop)
    thisExp.nextEntry()
    # the Routine "ITI_y_datos_PC" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    loop_condicion_PC = data.TrialHandler2(
        name='loop_condicion_PC',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions(archivo_csv_PC), 
        seed=None, 
    )
    thisExp.addLoop(loop_condicion_PC)  # add the loop to the experiment
    thisLoop_condicion_PC = loop_condicion_PC.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_condicion_PC.rgb)
    if thisLoop_condicion_PC != None:
        for paramName in thisLoop_condicion_PC:
            globals()[paramName] = thisLoop_condicion_PC[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisLoop_condicion_PC in loop_condicion_PC:
        currentLoop = loop_condicion_PC
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_condicion_PC.rgb)
        if thisLoop_condicion_PC != None:
            for paramName in thisLoop_condicion_PC:
                globals()[paramName] = thisLoop_condicion_PC[paramName]
        
        # --- Prepare to start Routine "condicion_PC" ---
        # create an object to store info about Routine condicion_PC
        condicion_PC = data.Routine(
            name='condicion_PC',
            components=[texto_estimulo_PC, respuesta_teclado_PC, CRUZ_PC, image_7],
        )
        condicion_PC.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        texto_estimulo_PC.setColor(color_tinta, colorSpace='rgb')
        texto_estimulo_PC.setText(palabra)
        # create starting attributes for respuesta_teclado_PC
        respuesta_teclado_PC.keys = []
        respuesta_teclado_PC.rt = []
        _respuesta_teclado_PC_allKeys = []
        # Run 'Begin Routine' code from Code_PC
        # Inicialización de variables
        respuesta_registrada = False
        tiempo_respuesta = None
        inicio_ensayo = globalClock.getTime()
        
        # Mostrar el estímulo y ocultar la cruz al comienzo
        texto_estimulo_PC.setAutoDraw(True)
        CRUZ_PC.setAutoDraw(False)
        
        # store start times for condicion_PC
        condicion_PC.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        condicion_PC.tStart = globalClock.getTime(format='float')
        condicion_PC.status = STARTED
        thisExp.addData('condicion_PC.started', condicion_PC.tStart)
        condicion_PC.maxDuration = None
        # keep track of which components have finished
        condicion_PCComponents = condicion_PC.components
        for thisComponent in condicion_PC.components:
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
        
        # --- Run Routine "condicion_PC" ---
        # if trial has changed, end Routine now
        if isinstance(loop_condicion_PC, data.TrialHandler2) and thisLoop_condicion_PC.thisN != loop_condicion_PC.thisTrial.thisN:
            continueRoutine = False
        condicion_PC.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *texto_estimulo_PC* updates
            
            # if texto_estimulo_PC is starting this frame...
            if texto_estimulo_PC.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                texto_estimulo_PC.frameNStart = frameN  # exact frame index
                texto_estimulo_PC.tStart = t  # local t and not account for scr refresh
                texto_estimulo_PC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(texto_estimulo_PC, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'texto_estimulo_PC.started')
                # update status
                texto_estimulo_PC.status = STARTED
                texto_estimulo_PC.setAutoDraw(True)
            
            # if texto_estimulo_PC is active this frame...
            if texto_estimulo_PC.status == STARTED:
                # update params
                pass
            
            # if texto_estimulo_PC is stopping this frame...
            if texto_estimulo_PC.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > texto_estimulo_PC.tStartRefresh + 2.5-frameTolerance:
                    # keep track of stop time/frame for later
                    texto_estimulo_PC.tStop = t  # not accounting for scr refresh
                    texto_estimulo_PC.tStopRefresh = tThisFlipGlobal  # on global time
                    texto_estimulo_PC.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'texto_estimulo_PC.stopped')
                    # update status
                    texto_estimulo_PC.status = FINISHED
                    texto_estimulo_PC.setAutoDraw(False)
            
            # *respuesta_teclado_PC* updates
            waitOnFlip = False
            
            # if respuesta_teclado_PC is starting this frame...
            if respuesta_teclado_PC.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                respuesta_teclado_PC.frameNStart = frameN  # exact frame index
                respuesta_teclado_PC.tStart = t  # local t and not account for scr refresh
                respuesta_teclado_PC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(respuesta_teclado_PC, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'respuesta_teclado_PC.started')
                # update status
                respuesta_teclado_PC.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(respuesta_teclado_PC.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(respuesta_teclado_PC.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if respuesta_teclado_PC is stopping this frame...
            if respuesta_teclado_PC.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > respuesta_teclado_PC.tStartRefresh + 2.5-frameTolerance:
                    # keep track of stop time/frame for later
                    respuesta_teclado_PC.tStop = t  # not accounting for scr refresh
                    respuesta_teclado_PC.tStopRefresh = tThisFlipGlobal  # on global time
                    respuesta_teclado_PC.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'respuesta_teclado_PC.stopped')
                    # update status
                    respuesta_teclado_PC.status = FINISHED
                    respuesta_teclado_PC.status = FINISHED
            if respuesta_teclado_PC.status == STARTED and not waitOnFlip:
                theseKeys = respuesta_teclado_PC.getKeys(keyList=['up','down','left','right'], ignoreKeys=["escape"], waitRelease=False)
                _respuesta_teclado_PC_allKeys.extend(theseKeys)
                if len(_respuesta_teclado_PC_allKeys):
                    respuesta_teclado_PC.keys = _respuesta_teclado_PC_allKeys[-1].name  # just the last key pressed
                    respuesta_teclado_PC.rt = _respuesta_teclado_PC_allKeys[-1].rt
                    respuesta_teclado_PC.duration = _respuesta_teclado_PC_allKeys[-1].duration
                    # was this correct?
                    if (respuesta_teclado_PC.keys == str(tecla_correcta)) or (respuesta_teclado_PC.keys == tecla_correcta):
                        respuesta_teclado_PC.corr = 1
                    else:
                        respuesta_teclado_PC.corr = 0
            
            # *CRUZ_PC* updates
            
            # if CRUZ_PC is starting this frame...
            if CRUZ_PC.status == NOT_STARTED and False:
                # keep track of start time/frame for later
                CRUZ_PC.frameNStart = frameN  # exact frame index
                CRUZ_PC.tStart = t  # local t and not account for scr refresh
                CRUZ_PC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(CRUZ_PC, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'CRUZ_PC.started')
                # update status
                CRUZ_PC.status = STARTED
                CRUZ_PC.setAutoDraw(True)
            
            # if CRUZ_PC is active this frame...
            if CRUZ_PC.status == STARTED:
                # update params
                pass
            # Run 'Each Frame' code from Code_PC
            tiempo_actual = globalClock.getTime() - inicio_ensayo
            
            # Si responde antes del límite
            if respuesta_teclado_PC.keys and not respuesta_registrada:
                respuesta_registrada = True
                tiempo_respuesta = tiempo_actual
                texto_estimulo_PC.setAutoDraw(False)
                CRUZ_PC.setAutoDraw(True)
                respuesta_teclado_PC.status = FINISHED
            
            # Si no respondió y se agotaron los 2.5 s
            elif tiempo_actual >= 2.5 and not respuesta_registrada:
                respuesta_registrada = True
                texto_estimulo_PC.setAutoDraw(False)
                CRUZ_PC.setAutoDraw(True)
                respuesta_teclado_PC.status = FINISHED
            # Terminar rutina al llegar a 3.0 s exactos
            elif tiempo_actual >= 3.0:
                continueRoutine = False
            
            # *image_7* updates
            
            # if image_7 is starting this frame...
            if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_7.frameNStart = frameN  # exact frame index
                image_7.tStart = t  # local t and not account for scr refresh
                image_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_7.started')
                # update status
                image_7.status = STARTED
                image_7.setAutoDraw(True)
            
            # if image_7 is active this frame...
            if image_7.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
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
                condicion_PC.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in condicion_PC.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "condicion_PC" ---
        for thisComponent in condicion_PC.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for condicion_PC
        condicion_PC.tStop = globalClock.getTime(format='float')
        condicion_PC.tStopRefresh = tThisFlipGlobal
        thisExp.addData('condicion_PC.stopped', condicion_PC.tStop)
        # check responses
        if respuesta_teclado_PC.keys in ['', [], None]:  # No response was made
            respuesta_teclado_PC.keys = None
            # was no response the correct answer?!
            if str(tecla_correcta).lower() == 'none':
               respuesta_teclado_PC.corr = 1;  # correct non-response
            else:
               respuesta_teclado_PC.corr = 0;  # failed to respond (incorrectly)
        # store data for loop_condicion_PC (TrialHandler)
        loop_condicion_PC.addData('respuesta_teclado_PC.keys',respuesta_teclado_PC.keys)
        loop_condicion_PC.addData('respuesta_teclado_PC.corr', respuesta_teclado_PC.corr)
        if respuesta_teclado_PC.keys != None:  # we had a response
            loop_condicion_PC.addData('respuesta_teclado_PC.rt', respuesta_teclado_PC.rt)
            loop_condicion_PC.addData('respuesta_teclado_PC.duration', respuesta_teclado_PC.duration)
        # Run 'End Routine' code from Code_PC
        # Clasificación de la validez
        if tiempo_respuesta:
            if tiempo_respuesta < 0.2:
                validez = 'anticipada'
                respuesta_teclado_PC.corr = 0  # Forzar como incorrecta
            else:
                validez = 'valida'
        else:
            validez = 'omitida'
        
        # Guardar validez
        thisExp.addData('validez', validez)
        CRUZ_PC.setAutoDraw(False)
        
        # Guardar datos
        thisExp.addData('RT', tiempo_respuesta if tiempo_respuesta else 'NA')
        thisExp.addData('key', respuesta_teclado_PC.keys)
        
        # the Routine "condicion_PC" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'loop_condicion_PC'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
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
    thisExp.saveAsWideText(filename + '.csv', delim='comma')
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
