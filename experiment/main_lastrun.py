#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on styczeń 05, 2026, at 05:17
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2023.2.3')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
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
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.3'
expName = 'auditory_semantic_1back_pilot'  # from the Builder filename that created this script
expInfo = {
    'participant': 'pilot01',
    'run': '1',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
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
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'../results/%s_%s_run%s_%s' % (expInfo['participant'], expName, expInfo['run'], expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\kinga\\Documents\\Blindbrain\\4. Courses\\fMRI - design of the experiment and data analysis\\cognes-auditory-1back-pilot\\experiment\\main_lastrun.py',
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
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.EXP)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    
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
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1536, 960], fullscr=True, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = False
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
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
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='iohub')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
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
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='ioHub')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
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
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
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
    
    # --- Initialize components for Routine "setup" ---
    # Run 'Begin Experiment' code from setup_code
    from psychopy import core, logging
    
    # global clock for logging
    globalClock = core.Clock()
    logging.setDefaultClock(globalClock)
    
    # run-level clock
    runClock = core.Clock()
    
    
    # --- Initialize components for Routine "instructions" ---
    instructions_text = visual.TextStim(win=win, name='instructions_text',
        text='',
        font='Open Sans',
        units='height', pos=(0, 0), height=0.05, wrapWidth=1.4, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    instructions_key = keyboard.Keyboard()
    
    # --- Initialize components for Routine "wait_for_trigger" ---
    trigger_key = keyboard.Keyboard()
    
    # --- Initialize components for Routine "dummy_TR" ---
    dummy_text = visual.TextStim(win=win, name='dummy_text',
        text='Oczekiwanie na skaner',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "block_start" ---
    # Run 'Begin Experiment' code from block_start_code
    block_instruction = ""
    
    block_instr_text = visual.TextStim(win=win, name='block_instr_text',
        text='',
        font='Open Sans',
        units='height', pos=(0, 0), height=0.05, wrapWidth=1.2, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "trial" ---
    fixation = visual.TextStim(win=win, name='fixation',
        text='',
        font='Open Sans',
        units='height', pos=(0.0, 0), height=0.08, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    stim_sound = sound.Sound('A', secs=1.5, stereo=True, hamming=False,
        name='stim_sound')
    stim_sound.setVolume(1.0)
    resp_prompt = visual.TextStim(win=win, name='resp_prompt',
        text='',
        font='Open Sans',
        units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=1.0, 
        languageStyle='LTR',
        depth=-3.0);
    resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "end" ---
    end_text = visual.TextStim(win=win, name='end_text',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    end_key = keyboard.Keyboard()
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "setup" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('setup.started', globalClock.getTime())
    # keep track of which components have finished
    setupComponents = []
    for thisComponent in setupComponents:
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
    
    # --- Run Routine "setup" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in setupComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "setup" ---
    for thisComponent in setupComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('setup.stopped', globalClock.getTime())
    # the Routine "setup" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    instr_pages = data.TrialHandler(nReps=3.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='instr_pages')
    thisExp.addLoop(instr_pages)  # add the loop to the experiment
    thisInstr_page = instr_pages.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisInstr_page.rgb)
    if thisInstr_page != None:
        for paramName in thisInstr_page:
            globals()[paramName] = thisInstr_page[paramName]
    
    for thisInstr_page in instr_pages:
        currentLoop = instr_pages
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisInstr_page.rgb)
        if thisInstr_page != None:
            for paramName in thisInstr_page:
                globals()[paramName] = thisInstr_page[paramName]
        
        # --- Prepare to start Routine "instructions" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('instructions.started', globalClock.getTime())
        # Run 'Begin Routine' code from instructions_code
        import io
        import re
        
        # load instruction texts
        if 'instr_dict' not in globals():
            raw = io.open("resources/instructions/instr_pl.txt", encoding="utf-8").read()
            parts = re.split(
                r'^\[(GENERAL_1|GENERAL_2|GENERAL_3|CON|ABS|BASE)\]\s*$',
                raw,
                flags=re.MULTILINE
            )
            globals()['instr_dict'] = {
                parts[i]: parts[i + 1].strip()
                for i in range(1, len(parts), 2)
            }
        
        # choose general instruction page per loop iteration
        page_num = instr_pages.thisN + 1   # 1..3
        general_instruction = globals()['instr_dict'].get(
            f"GENERAL_{page_num}",
            f"BŁĄD: brak sekcji [GENERAL_{page_num}] w instr_pl.txt"
        )
        
        instructions_text.setText(general_instruction)
        instructions_key.keys = []
        instructions_key.rt = []
        _instructions_key_allKeys = []
        # keep track of which components have finished
        instructionsComponents = [instructions_text, instructions_key]
        for thisComponent in instructionsComponents:
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
        
        # --- Run Routine "instructions" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *instructions_text* updates
            
            # if instructions_text is starting this frame...
            if instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                instructions_text.frameNStart = frameN  # exact frame index
                instructions_text.tStart = t  # local t and not account for scr refresh
                instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(instructions_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'instructions_text.started')
                # update status
                instructions_text.status = STARTED
                instructions_text.setAutoDraw(True)
            
            # if instructions_text is active this frame...
            if instructions_text.status == STARTED:
                # update params
                pass
            
            # *instructions_key* updates
            waitOnFlip = False
            
            # if instructions_key is starting this frame...
            if instructions_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                instructions_key.frameNStart = frameN  # exact frame index
                instructions_key.tStart = t  # local t and not account for scr refresh
                instructions_key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(instructions_key, 'tStartRefresh')  # time at next scr refresh
                # update status
                instructions_key.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(instructions_key.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(instructions_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if instructions_key.status == STARTED and not waitOnFlip:
                theseKeys = instructions_key.getKeys(keyList=['a','b','c','d','space'], ignoreKeys=["escape"], waitRelease=False)
                _instructions_key_allKeys.extend(theseKeys)
                if len(_instructions_key_allKeys):
                    instructions_key.keys = _instructions_key_allKeys[-1].name  # just the last key pressed
                    instructions_key.rt = _instructions_key_allKeys[-1].rt
                    instructions_key.duration = _instructions_key_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in instructionsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "instructions" ---
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('instructions.stopped', globalClock.getTime())
        # check responses
        if instructions_key.keys in ['', [], None]:  # No response was made
            instructions_key.keys = None
        instr_pages.addData('instructions_key.keys',instructions_key.keys)
        if instructions_key.keys != None:  # we had a response
            instr_pages.addData('instructions_key.rt', instructions_key.rt)
            instr_pages.addData('instructions_key.duration', instructions_key.duration)
        # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 3.0 repeats of 'instr_pages'
    
    
    # --- Prepare to start Routine "wait_for_trigger" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('wait_for_trigger.started', globalClock.getTime())
    # Run 'Begin Routine' code from trigger_code
    # manual run selection from the startup dialog
    run_id = int(expInfo["run"])
    
    # choose conditions file for blocks loop
    if run_id == 1:
        blocks_file = "resources/lists/blocks_run1.csv"
    elif run_id == 2:
        blocks_file = "resources/lists/blocks_run2.csv"
    else:
        raise ValueError("expInfo['run'] must be 1 or 2.")
    
    runClock.reset()
    
    trigger_key.keys = []
    trigger_key.rt = []
    _trigger_key_allKeys = []
    # keep track of which components have finished
    wait_for_triggerComponents = [trigger_key]
    for thisComponent in wait_for_triggerComponents:
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
    
    # --- Run Routine "wait_for_trigger" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trigger_key* updates
        waitOnFlip = False
        
        # if trigger_key is starting this frame...
        if trigger_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trigger_key.frameNStart = frameN  # exact frame index
            trigger_key.tStart = t  # local t and not account for scr refresh
            trigger_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trigger_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trigger_key.started')
            # update status
            trigger_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(trigger_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(trigger_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if trigger_key.status == STARTED and not waitOnFlip:
            theseKeys = trigger_key.getKeys(keyList=['s'], ignoreKeys=["escape"], waitRelease=False)
            _trigger_key_allKeys.extend(theseKeys)
            if len(_trigger_key_allKeys):
                trigger_key.keys = _trigger_key_allKeys[-1].name  # just the last key pressed
                trigger_key.rt = _trigger_key_allKeys[-1].rt
                trigger_key.duration = _trigger_key_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in wait_for_triggerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "wait_for_trigger" ---
    for thisComponent in wait_for_triggerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('wait_for_trigger.stopped', globalClock.getTime())
    # check responses
    if trigger_key.keys in ['', [], None]:  # No response was made
        trigger_key.keys = None
    thisExp.addData('trigger_key.keys',trigger_key.keys)
    if trigger_key.keys != None:  # we had a response
        thisExp.addData('trigger_key.rt', trigger_key.rt)
        thisExp.addData('trigger_key.duration', trigger_key.duration)
    thisExp.nextEntry()
    # the Routine "wait_for_trigger" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "dummy_TR" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('dummy_TR.started', globalClock.getTime())
    # keep track of which components have finished
    dummy_TRComponents = [dummy_text]
    for thisComponent in dummy_TRComponents:
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
    
    # --- Run Routine "dummy_TR" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 8.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 8.0-frameTolerance:
            continueRoutine = False
        
        # *dummy_text* updates
        
        # if dummy_text is starting this frame...
        if dummy_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dummy_text.frameNStart = frameN  # exact frame index
            dummy_text.tStart = t  # local t and not account for scr refresh
            dummy_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dummy_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'dummy_text.started')
            # update status
            dummy_text.status = STARTED
            dummy_text.setAutoDraw(True)
        
        # if dummy_text is active this frame...
        if dummy_text.status == STARTED:
            # update params
            pass
        
        # if dummy_text is stopping this frame...
        if dummy_text.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 6.0-frameTolerance:
                # keep track of stop time/frame for later
                dummy_text.tStop = t  # not accounting for scr refresh
                dummy_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dummy_text.stopped')
                # update status
                dummy_text.status = FINISHED
                dummy_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in dummy_TRComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "dummy_TR" ---
    for thisComponent in dummy_TRComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('dummy_TR.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-8.000000)
    
    # set up handler to look after randomisation of conditions etc
    blocks = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(blocks_file),
        seed=None, name='blocks')
    thisExp.addLoop(blocks)  # add the loop to the experiment
    thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            globals()[paramName] = thisBlock[paramName]
    
    for thisBlock in blocks:
        currentLoop = blocks
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
        if thisBlock != None:
            for paramName in thisBlock:
                globals()[paramName] = thisBlock[paramName]
        
        # --- Prepare to start Routine "block_start" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('block_start.started', globalClock.getTime())
        # Run 'Begin Routine' code from block_start_code
        # reset run clock (first block only)
        if blocks.thisN == 0:
            runClock.reset()
        
        # block onset (time since start of run)
        block_onset = runClock.getTime()
        
        import io
        import re
        
        # load instruction texts
        if 'instr_dict' not in globals():
            raw = io.open("resources/instructions/instr_pl.txt", encoding="utf-8").read()
            parts = re.split(
                r'^\[(GENERAL_1|GENERAL_2|GENERAL_3|CON|ABS|BASE)\]\s*$',
                raw,
                flags=re.MULTILINE
            )
            globals()['instr_dict'] = {
                parts[i]: parts[i + 1].strip()
                for i in range(1, len(parts), 2)
            }
        
        # block identifiers
        block_id = blocks.thisN + 1
        run_id = int(expInfo["run"])
        
        # instruction text for this block
        block_instruction = globals()['instr_dict'].get(
            block_type,
            "BŁĄD: brak instrukcji dla bloku."
        )
        
        # select trials file for this block
        if block_type == "CON":
            trials_file = f"resources/lists/con_run{run_id}.csv"
        elif block_type == "ABS":
            trials_file = f"resources/lists/abs_run{run_id}.csv"
        else:
            trials_file = f"resources/lists/base_run{run_id}.csv"
        
        block_instr_text.setText(block_instruction)
        # keep track of which components have finished
        block_startComponents = [block_instr_text]
        for thisComponent in block_startComponents:
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
        
        # --- Run Routine "block_start" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 6.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *block_instr_text* updates
            
            # if block_instr_text is starting this frame...
            if block_instr_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                block_instr_text.frameNStart = frameN  # exact frame index
                block_instr_text.tStart = t  # local t and not account for scr refresh
                block_instr_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(block_instr_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block_instr_text.started')
                # update status
                block_instr_text.status = STARTED
                block_instr_text.setAutoDraw(True)
            
            # if block_instr_text is active this frame...
            if block_instr_text.status == STARTED:
                # update params
                pass
            
            # if block_instr_text is stopping this frame...
            if block_instr_text.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 6.0-frameTolerance:
                    # keep track of stop time/frame for later
                    block_instr_text.tStop = t  # not accounting for scr refresh
                    block_instr_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'block_instr_text.stopped')
                    # update status
                    block_instr_text.status = FINISHED
                    block_instr_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in block_startComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "block_start" ---
        for thisComponent in block_startComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('block_start.stopped', globalClock.getTime())
        # Run 'End Routine' code from block_start_code
        thisExp.addData("block_onset", block_onset)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-6.000000)
        
        # set up handler to look after randomisation of conditions etc
        trials = data.TrialHandler(nReps=1.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(trials_file),
            seed=None, name='trials')
        thisExp.addLoop(trials)  # add the loop to the experiment
        thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        for thisTrial in trials:
            currentLoop = trials
            thisExp.timestampOnFlip(win, 'thisRow.t')
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    inputs=inputs, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
            if thisTrial != None:
                for paramName in thisTrial:
                    globals()[paramName] = thisTrial[paramName]
            
            # --- Prepare to start Routine "trial" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('trial.started', globalClock.getTime())
            # Run 'Begin Routine' code from trial_timing
            # reset response container for this trial
            resp.keys = None
            resp.rt = None
            
            # IDs (run is chosen manually in the dialog)
            run_id = int(expInfo["run"])
            block_id = blocks.thisN + 1
            
            # trial counters
            trial_index0 = trials.thisN          
            trial_index1 = trial_index0 + 1      
            is_first_in_block = int(trial_index0 == 0)
            
            # time since start of run
            trial_onset = runClock.getTime()
            
            # prompt text depends on block type
            if block_type == "CON":
                resp_prompt_text = "MNIEJSZY  ←        →  WIĘKSZY"
            elif block_type == "ABS":
                resp_prompt_text = "MNIEJ WAŻNE  ←        →  WAŻNIEJSZE"
            else:
                resp_prompt_text = "DOWOLNY PRZYCISK"
            
            # store a copy of the filename actually used
            stim_file_used = stimFile
            
            # save to CSV
            thisExp.addData("trial_onset", trial_onset)
            thisExp.addData("block_onset", block_onset)
            thisExp.addData("trial_index1", trial_index1)
            thisExp.addData("is_first_in_block", is_first_in_block)
            thisExp.addData("stim_file_used", stim_file_used)
            thisExp.addData("resp_prompt_text", resp_prompt_text)
            
            fixation.setText('+')
            stim_sound.setSound(stimFile, secs=1.5, hamming=False)
            stim_sound.setVolume(1.0, log=False)
            stim_sound.seek(0)
            resp_prompt.setText(resp_prompt_text)
            resp.keys = []
            resp.rt = []
            _resp_allKeys = []
            # keep track of which components have finished
            trialComponents = [fixation, stim_sound, resp_prompt, resp]
            for thisComponent in trialComponents:
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
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 3.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # is it time to end the Routine? (based on local clock)
                if tThisFlip > 3.0-frameTolerance:
                    continueRoutine = False
                
                # *fixation* updates
                
                # if fixation is starting this frame...
                if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fixation.frameNStart = frameN  # exact frame index
                    fixation.tStart = t  # local t and not account for scr refresh
                    fixation.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation.started')
                    # update status
                    fixation.status = STARTED
                    fixation.setAutoDraw(True)
                
                # if fixation is active this frame...
                if fixation.status == STARTED:
                    # update params
                    pass
                
                # if fixation is stopping this frame...
                if fixation.status == STARTED:
                    # is it time to stop? (based on local clock)
                    if tThisFlip > 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        fixation.tStop = t  # not accounting for scr refresh
                        fixation.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixation.stopped')
                        # update status
                        fixation.status = FINISHED
                        fixation.setAutoDraw(False)
                
                # if stim_sound is starting this frame...
                if stim_sound.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    stim_sound.frameNStart = frameN  # exact frame index
                    stim_sound.tStart = t  # local t and not account for scr refresh
                    stim_sound.tStartRefresh = tThisFlipGlobal  # on global time
                    # add timestamp to datafile
                    thisExp.addData('stim_sound.started', t)
                    # update status
                    stim_sound.status = STARTED
                    stim_sound.play()  # start the sound (it finishes automatically)
                
                # if stim_sound is stopping this frame...
                if stim_sound.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > stim_sound.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        stim_sound.tStop = t  # not accounting for scr refresh
                        stim_sound.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.addData('stim_sound.stopped', t)
                        # update status
                        stim_sound.status = FINISHED
                        stim_sound.stop()
                # update stim_sound status according to whether it's playing
                if stim_sound.isPlaying:
                    stim_sound.status = STARTED
                elif stim_sound.isFinished:
                    stim_sound.status = FINISHED
                
                # *resp_prompt* updates
                
                # if resp_prompt is starting this frame...
                if resp_prompt.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                    # keep track of start time/frame for later
                    resp_prompt.frameNStart = frameN  # exact frame index
                    resp_prompt.tStart = t  # local t and not account for scr refresh
                    resp_prompt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(resp_prompt, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'resp_prompt.started')
                    # update status
                    resp_prompt.status = STARTED
                    resp_prompt.setAutoDraw(True)
                
                # if resp_prompt is active this frame...
                if resp_prompt.status == STARTED:
                    # update params
                    pass
                
                # if resp_prompt is stopping this frame...
                if resp_prompt.status == STARTED:
                    # is it time to stop? (based on local clock)
                    if tThisFlip > 3.0-frameTolerance:
                        # keep track of stop time/frame for later
                        resp_prompt.tStop = t  # not accounting for scr refresh
                        resp_prompt.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'resp_prompt.stopped')
                        # update status
                        resp_prompt.status = FINISHED
                        resp_prompt.setAutoDraw(False)
                
                # *resp* updates
                waitOnFlip = False
                
                # if resp is starting this frame...
                if resp.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                    # keep track of start time/frame for later
                    resp.frameNStart = frameN  # exact frame index
                    resp.tStart = t  # local t and not account for scr refresh
                    resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'resp.started')
                    # update status
                    resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if resp is stopping this frame...
                if resp.status == STARTED:
                    # is it time to stop? (based on local clock)
                    if tThisFlip > 3.0-frameTolerance:
                        # keep track of stop time/frame for later
                        resp.tStop = t  # not accounting for scr refresh
                        resp.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'resp.stopped')
                        # update status
                        resp.status = FINISHED
                        resp.status = FINISHED
                if resp.status == STARTED and not waitOnFlip:
                    theseKeys = resp.getKeys(keyList=['a','b','c','d'], ignoreKeys=["escape"], waitRelease=False)
                    _resp_allKeys.extend(theseKeys)
                    if len(_resp_allKeys):
                        resp.keys = _resp_allKeys[-1].name  # just the last key pressed
                        resp.rt = _resp_allKeys[-1].rt
                        resp.duration = _resp_allKeys[-1].duration
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial" ---
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('trial.stopped', globalClock.getTime())
            # check responses
            if resp.keys in ['', [], None]:  # No response was made
                resp.keys = None
            trials.addData('resp.keys',resp.keys)
            if resp.keys != None:  # we had a response
                trials.addData('resp.rt', resp.rt)
                trials.addData('resp.duration', resp.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-3.000000)
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 1.0 repeats of 'trials'
        
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'blocks'
    
    
    # --- Prepare to start Routine "end" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('end.started', globalClock.getTime())
    # Run 'Begin Routine' code from code
    run_id = int(expInfo["run"])
    
    if run_id == 1:
        end_message = (
            "Jesteśmy w połowie badania.\n\n\n"
            "Aby kontynuować, naciśnij dowolny przycisk."
        )
    else:
        end_message = (
            "To koniec badania.\n"
            "Dziękuję za udział!\n\n"
            "Aby zakończyć, naciśnij dowolny przycisk."
        )
    
    end_text.setText(end_message)
    end_key.keys = []
    end_key.rt = []
    _end_key_allKeys = []
    # keep track of which components have finished
    endComponents = [end_text, end_key]
    for thisComponent in endComponents:
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
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *end_text* updates
        
        # if end_text is starting this frame...
        if end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end_text.frameNStart = frameN  # exact frame index
            end_text.tStart = t  # local t and not account for scr refresh
            end_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'end_text.started')
            # update status
            end_text.status = STARTED
            end_text.setAutoDraw(True)
        
        # if end_text is active this frame...
        if end_text.status == STARTED:
            # update params
            pass
        
        # *end_key* updates
        waitOnFlip = False
        
        # if end_key is starting this frame...
        if end_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end_key.frameNStart = frameN  # exact frame index
            end_key.tStart = t  # local t and not account for scr refresh
            end_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'end_key.started')
            # update status
            end_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(end_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(end_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if end_key.status == STARTED and not waitOnFlip:
            theseKeys = end_key.getKeys(keyList=['a','b','c','d','space'], ignoreKeys=["escape"], waitRelease=False)
            _end_key_allKeys.extend(theseKeys)
            if len(_end_key_allKeys):
                end_key.keys = _end_key_allKeys[-1].name  # just the last key pressed
                end_key.rt = _end_key_allKeys[-1].rt
                end_key.duration = _end_key_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in endComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "end" ---
    for thisComponent in endComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('end.stopped', globalClock.getTime())
    # check responses
    if end_key.keys in ['', [], None]:  # No response was made
        end_key.keys = None
    thisExp.addData('end_key.keys',end_key.keys)
    if end_key.keys != None:  # we had a response
        thisExp.addData('end_key.rt', end_key.rt)
        thisExp.addData('end_key.duration', end_key.duration)
    thisExp.nextEntry()
    # the Routine "end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


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


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
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
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
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
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
