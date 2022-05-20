#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on Mai 10, 2022, at 13:19
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'BA2'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\pwetz\\Desktop\\Bachelor\\Bachelorarbeit\\Psychopy\\BA2.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 720], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Welcome"
WelcomeClock = core.Clock()
textWelcome = visual.TextStim(win=win, name='textWelcome',
    text="Willkommen zu diesem Experiment. Vielen Dank, dass du daran teilnehmen möchtest.\n\nEs wird 2 Teile geben, wobei du in beiden Teilen Bilder sehen wirst. Im 1. Teil sollst du entscheiden, wie vertrauenswürdig du die Person empfindest. Im 2.Teil wird es darum gehen, wie bekannt dir das gezeigte Bild ist. Das Experiment geht insgesamt etwa 20 Minuten.\n\nFür deine Teilnahme erhälst du 0.5 VPn in Form eines VPN-Codes, welchen du am Ende des Experiemnts erhälst.\n\nSolltest du das Experiement abbrechen wollen, dann wähle 'ESC'.\n\nWeiter mit der LEERTASTE.\n",
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_Welcome = keyboard.Keyboard()

# Initialize components for Routine "Basic_Info"
Basic_InfoClock = core.Clock()
Alter = visual.TextBox2(
     win, text='Alter', font='Arial',
     pos=(0, 0.4),     letterHeight=0.03,
     size=None, borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor='black', borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=True,
     name='Alter',
     autoLog=True,
)
Geschlecht = visual.TextBox2(
     win, text='Geschlecht (w/m/d)', font='Arial',
     pos=(0, 0),     letterHeight=0.03,
     size=None, borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor='black', borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=True,
     name='Geschlecht',
     autoLog=True,
)
text = visual.TextStim(win=win, name='text',
    text='Bitte ausfüllen und weiter mit der LEERTASTE.',
    font='Arial',
    pos=(0, -.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "Instruction1"
Instruction1Clock = core.Clock()
text_Instruction = visual.TextStim(win=win, name='text_Instruction',
    text='TEIL 1\n\nIm Folgenden werden dir einige Bilder gezeigt und im Anschluss hast du die Möglichkeit auf einer Skala zu entscheiden, wie vertrausenwürdig du die gezeigte Person einschätzt. \n\nNutze die Maus, um auf der Skala einen Punkt zu setzen.\n\nWeiter mit der LEERTASTE.\n\n',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_Instruction = keyboard.Keyboard()

# Initialize components for Routine "Test1"
Test1Clock = core.Clock()
textTest = visual.TextStim(win=win, name='textTest',
    text='Zuerst folgt eine kurze Testphase.\n\nWeiter mit der LEERTASTE.\n',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_TestStart = keyboard.Keyboard()

# Initialize components for Routine "Testphase"
TestphaseClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.3,0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "TrustScale"
TrustScaleClock = core.Clock()
sliderTrust = visual.Slider(win=win, name='sliderTrust',
    size=(1.0, 0.05), pos=(0, -0.4), units=None,
    labels=[1,2,3,4,5], ticks=(1, 2, 3, 4, 5), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=0, readOnly=False)
text_2 = visual.TextStim(win=win, name='text_2',
    text='Wie vertrausenswürdig ist die Person? (1-gar nicht, 5-sehr)',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "StartTrust1"
StartTrust1Clock = core.Clock()
textTrust1 = visual.TextStim(win=win, name='textTrust1',
    text='Der Test ist beendet.\n\nMit der LEERTASTE beginnt Teil 1. Deine Aufgabe bleibt die Vertrauenswürdigkeit einzuschätzen.',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
keyTrust1 = keyboard.Keyboard()

# Initialize components for Routine "Trust"
TrustClock = core.Clock()
image_Studyphase = visual.ImageStim(
    win=win,
    name='image_Studyphase', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "TrustScale"
TrustScaleClock = core.Clock()
sliderTrust = visual.Slider(win=win, name='sliderTrust',
    size=(1.0, 0.05), pos=(0, -0.4), units=None,
    labels=[1,2,3,4,5], ticks=(1, 2, 3, 4, 5), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=0, readOnly=False)
text_2 = visual.TextStim(win=win, name='text_2',
    text='Wie vertrausenswürdig ist die Person? (1-gar nicht, 5-sehr)',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "StartTeil2"
StartTeil2Clock = core.Clock()
textMain = visual.TextStim(win=win, name='textMain',
    text='Teil 2\n\nIm Folgenden werden dir wieder Bilder gezeigt. Nach jedem Bild sollst du entscheiden, ob dieses neu, ähnlich oder alt ist zu denen,die du in Teil 1 gesehen hast.\n\nDrücke für :\nNEU die Taste Y\nÄHNLICH die Taste V\nALT die Taste M\n\nUm Teil 2 zu beginnen, wähle die LEERTASTE.\n\n',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "Test1"
Test1Clock = core.Clock()
textTest = visual.TextStim(win=win, name='textTest',
    text='Zuerst folgt eine kurze Testphase.\n\nWeiter mit der LEERTASTE.\n',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_TestStart = keyboard.Keyboard()

# Initialize components for Routine "Testphase"
TestphaseClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.3,0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "ImageResponse"
ImageResponseClock = core.Clock()
textAnswerOptions = visual.TextStim(win=win, name='textAnswerOptions',
    text='NEU = X     ÄHNLICH = V      ALT = M',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "StartMain"
StartMainClock = core.Clock()
text_StartMain = visual.TextStim(win=win, name='text_StartMain',
    text='Test beendet!\n\nDrücke die LEERTASTE sobald du bereit bist. Dann beginnt der Hauptteil.',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "con"
conClock = core.Clock()
import random
condition=random.choice(('A','B'))

# Initialize components for Routine "Main"
MainClock = core.Clock()
image_Main = visual.ImageStim(
    win=win,
    name='image_Main', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "ImageResponse"
ImageResponseClock = core.Clock()
textAnswerOptions = visual.TextStim(win=win, name='textAnswerOptions',
    text='NEU = X     ÄHNLICH = V      ALT = M',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "Ende"
EndeClock = core.Clock()
textbox = visual.TextBox2(
     win, text='BIO/BAWET21/CODE', font='Arial',
     pos=(0,-0.3),     letterHeight=0.03,
     size=None, borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor='black', borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=True,
     name='textbox',
     autoLog=True,
)
text_VPNCode = visual.TextStim(win=win, name='text_VPNCode',
    text='Das Experiment ist nun zu Ende. Vielen Dank für deine Teilnahme!\n\nDu erhälst 0.5 VPn-Stunden. Trage dir diese mit dem heutigen Datum ein. \nAls Unterschrift gilt: BIO/BAWET21/(individueller Code)\n\nDein Code setzt sich zusammmen aus:\n1)die zwei ersten Buchstaben deines Vornamen (z.B. Anna=AN)\n2)die beiden letzten Buchstaben deines Heimatortes (z.B. WEIMAR=AR)\n3)dein Geburtsdatum (z.B. 14.07.=1407)\nBEISPIEL:BIO/BAWET21/ANAR1407\n\nBitte trage denn Code unbedingt unten ein, sonst kann deine VPn-Stunde nicht bestätigt werden. \n\nMit der LEERTASTE endet das Experiment.',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
ENDE = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Welcome"-------
continueRoutine = True
# update component parameters for each repeat
key_Welcome.keys = []
key_Welcome.rt = []
_key_Welcome_allKeys = []
# keep track of which components have finished
WelcomeComponents = [textWelcome, key_Welcome]
for thisComponent in WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Welcome"-------
while continueRoutine:
    # get current time
    t = WelcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textWelcome* updates
    if textWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textWelcome.frameNStart = frameN  # exact frame index
        textWelcome.tStart = t  # local t and not account for scr refresh
        textWelcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textWelcome, 'tStartRefresh')  # time at next scr refresh
        textWelcome.setAutoDraw(True)
    
    # *key_Welcome* updates
    if key_Welcome.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_Welcome.frameNStart = frameN  # exact frame index
        key_Welcome.tStart = t  # local t and not account for scr refresh
        key_Welcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_Welcome, 'tStartRefresh')  # time at next scr refresh
        key_Welcome.status = STARTED
        # keyboard checking is just starting
        key_Welcome.clock.reset()  # now t=0
        key_Welcome.clearEvents(eventType='keyboard')
    if key_Welcome.status == STARTED:
        theseKeys = key_Welcome.getKeys(keyList=['space'], waitRelease=False)
        _key_Welcome_allKeys.extend(theseKeys)
        if len(_key_Welcome_allKeys):
            key_Welcome.keys = _key_Welcome_allKeys[-1].name  # just the last key pressed
            key_Welcome.rt = _key_Welcome_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome"-------
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Basic_Info"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
Basic_InfoComponents = [Alter, Geschlecht, text, key_resp_3]
for thisComponent in Basic_InfoComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Basic_InfoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Basic_Info"-------
while continueRoutine:
    # get current time
    t = Basic_InfoClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Basic_InfoClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Alter* updates
    if Alter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Alter.frameNStart = frameN  # exact frame index
        Alter.tStart = t  # local t and not account for scr refresh
        Alter.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Alter, 'tStartRefresh')  # time at next scr refresh
        Alter.setAutoDraw(True)
    
    # *Geschlecht* updates
    if Geschlecht.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Geschlecht.frameNStart = frameN  # exact frame index
        Geschlecht.tStart = t  # local t and not account for scr refresh
        Geschlecht.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Geschlecht, 'tStartRefresh')  # time at next scr refresh
        Geschlecht.setAutoDraw(True)
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp_3* updates
    if key_resp_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        key_resp_3.clock.reset()  # now t=0
        key_resp_3.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Basic_InfoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Basic_Info"-------
for thisComponent in Basic_InfoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Alter.text',Alter.text)
Alter.reset()
thisExp.addData('Geschlecht.text',Geschlecht.text)
Geschlecht.reset()
# the Routine "Basic_Info" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instruction1"-------
continueRoutine = True
# update component parameters for each repeat
key_Instruction.keys = []
key_Instruction.rt = []
_key_Instruction_allKeys = []
# keep track of which components have finished
Instruction1Components = [text_Instruction, key_Instruction]
for thisComponent in Instruction1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instruction1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instruction1"-------
while continueRoutine:
    # get current time
    t = Instruction1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instruction1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_Instruction* updates
    if text_Instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_Instruction.frameNStart = frameN  # exact frame index
        text_Instruction.tStart = t  # local t and not account for scr refresh
        text_Instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_Instruction, 'tStartRefresh')  # time at next scr refresh
        text_Instruction.setAutoDraw(True)
    
    # *key_Instruction* updates
    if key_Instruction.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_Instruction.frameNStart = frameN  # exact frame index
        key_Instruction.tStart = t  # local t and not account for scr refresh
        key_Instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_Instruction, 'tStartRefresh')  # time at next scr refresh
        key_Instruction.status = STARTED
        # keyboard checking is just starting
        key_Instruction.clock.reset()  # now t=0
        key_Instruction.clearEvents(eventType='keyboard')
    if key_Instruction.status == STARTED:
        theseKeys = key_Instruction.getKeys(keyList=['space'], waitRelease=False)
        _key_Instruction_allKeys.extend(theseKeys)
        if len(_key_Instruction_allKeys):
            key_Instruction.keys = _key_Instruction_allKeys[-1].name  # just the last key pressed
            key_Instruction.rt = _key_Instruction_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instruction1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruction1"-------
for thisComponent in Instruction1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instruction1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Test1"-------
continueRoutine = True
# update component parameters for each repeat
key_TestStart.keys = []
key_TestStart.rt = []
_key_TestStart_allKeys = []
# keep track of which components have finished
Test1Components = [textTest, key_TestStart]
for thisComponent in Test1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Test1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Test1"-------
while continueRoutine:
    # get current time
    t = Test1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Test1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textTest* updates
    if textTest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textTest.frameNStart = frameN  # exact frame index
        textTest.tStart = t  # local t and not account for scr refresh
        textTest.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textTest, 'tStartRefresh')  # time at next scr refresh
        textTest.setAutoDraw(True)
    
    # *key_TestStart* updates
    if key_TestStart.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_TestStart.frameNStart = frameN  # exact frame index
        key_TestStart.tStart = t  # local t and not account for scr refresh
        key_TestStart.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_TestStart, 'tStartRefresh')  # time at next scr refresh
        key_TestStart.status = STARTED
        # keyboard checking is just starting
        key_TestStart.clock.reset()  # now t=0
        key_TestStart.clearEvents(eventType='keyboard')
    if key_TestStart.status == STARTED:
        theseKeys = key_TestStart.getKeys(keyList=['space'], waitRelease=False)
        _key_TestStart_allKeys.extend(theseKeys)
        if len(_key_TestStart_allKeys):
            key_TestStart.keys = _key_TestStart_allKeys[-1].name  # just the last key pressed
            key_TestStart.rt = _key_TestStart_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Test1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Test1"-------
for thisComponent in Test1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Test1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Test.xlsx', selection='0:4'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Testphase"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    image.setImage(ImageTest)
    # keep track of which components have finished
    TestphaseComponents = [image]
    for thisComponent in TestphaseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TestphaseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Testphase"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = TestphaseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TestphaseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TestphaseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Testphase"-------
    for thisComponent in TestphaseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "TrustScale"-------
    continueRoutine = True
    # update component parameters for each repeat
    sliderTrust.reset()
    # keep track of which components have finished
    TrustScaleComponents = [sliderTrust, text_2]
    for thisComponent in TrustScaleComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TrustScaleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "TrustScale"-------
    while continueRoutine:
        # get current time
        t = TrustScaleClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TrustScaleClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *sliderTrust* updates
        if sliderTrust.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sliderTrust.frameNStart = frameN  # exact frame index
            sliderTrust.tStart = t  # local t and not account for scr refresh
            sliderTrust.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sliderTrust, 'tStartRefresh')  # time at next scr refresh
            sliderTrust.setAutoDraw(True)
        
        # Check sliderTrust for response to end routine
        if sliderTrust.getRating() is not None and sliderTrust.status == STARTED:
            continueRoutine = False
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrustScaleComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "TrustScale"-------
    for thisComponent in TrustScaleComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('sliderTrust.response', sliderTrust.getRating())
    trials.addData('sliderTrust.rt', sliderTrust.getRT())
    trials.addData('text_2.started', text_2.tStartRefresh)
    trials.addData('text_2.stopped', text_2.tStopRefresh)
    # the Routine "TrustScale" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "StartTrust1"-------
continueRoutine = True
# update component parameters for each repeat
keyTrust1.keys = []
keyTrust1.rt = []
_keyTrust1_allKeys = []
# keep track of which components have finished
StartTrust1Components = [textTrust1, keyTrust1]
for thisComponent in StartTrust1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
StartTrust1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "StartTrust1"-------
while continueRoutine:
    # get current time
    t = StartTrust1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=StartTrust1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textTrust1* updates
    if textTrust1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textTrust1.frameNStart = frameN  # exact frame index
        textTrust1.tStart = t  # local t and not account for scr refresh
        textTrust1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textTrust1, 'tStartRefresh')  # time at next scr refresh
        textTrust1.setAutoDraw(True)
    
    # *keyTrust1* updates
    if keyTrust1.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyTrust1.frameNStart = frameN  # exact frame index
        keyTrust1.tStart = t  # local t and not account for scr refresh
        keyTrust1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyTrust1, 'tStartRefresh')  # time at next scr refresh
        keyTrust1.status = STARTED
        # keyboard checking is just starting
        keyTrust1.clock.reset()  # now t=0
        keyTrust1.clearEvents(eventType='keyboard')
    if keyTrust1.status == STARTED:
        theseKeys = keyTrust1.getKeys(keyList=['space'], waitRelease=False)
        _keyTrust1_allKeys.extend(theseKeys)
        if len(_keyTrust1_allKeys):
            keyTrust1.keys = _keyTrust1_allKeys[-1].name  # just the last key pressed
            keyTrust1.rt = _keyTrust1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StartTrust1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "StartTrust1"-------
for thisComponent in StartTrust1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "StartTrust1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Trust.xlsx', selection='0:193'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Trust"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    image_Studyphase.setImage(ImageTrust)
    # keep track of which components have finished
    TrustComponents = [image_Studyphase]
    for thisComponent in TrustComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TrustClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Trust"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = TrustClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TrustClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_Studyphase* updates
        if image_Studyphase.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_Studyphase.frameNStart = frameN  # exact frame index
            image_Studyphase.tStart = t  # local t and not account for scr refresh
            image_Studyphase.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_Studyphase, 'tStartRefresh')  # time at next scr refresh
            image_Studyphase.setAutoDraw(True)
        if image_Studyphase.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_Studyphase.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                image_Studyphase.tStop = t  # not accounting for scr refresh
                image_Studyphase.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_Studyphase, 'tStopRefresh')  # time at next scr refresh
                image_Studyphase.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrustComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Trust"-------
    for thisComponent in TrustComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('image_Studyphase.started', image_Studyphase.tStartRefresh)
    trials_2.addData('image_Studyphase.stopped', image_Studyphase.tStopRefresh)
    
    # ------Prepare to start Routine "TrustScale"-------
    continueRoutine = True
    # update component parameters for each repeat
    sliderTrust.reset()
    # keep track of which components have finished
    TrustScaleComponents = [sliderTrust, text_2]
    for thisComponent in TrustScaleComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TrustScaleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "TrustScale"-------
    while continueRoutine:
        # get current time
        t = TrustScaleClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TrustScaleClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *sliderTrust* updates
        if sliderTrust.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sliderTrust.frameNStart = frameN  # exact frame index
            sliderTrust.tStart = t  # local t and not account for scr refresh
            sliderTrust.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sliderTrust, 'tStartRefresh')  # time at next scr refresh
            sliderTrust.setAutoDraw(True)
        
        # Check sliderTrust for response to end routine
        if sliderTrust.getRating() is not None and sliderTrust.status == STARTED:
            continueRoutine = False
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrustScaleComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "TrustScale"-------
    for thisComponent in TrustScaleComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('sliderTrust.response', sliderTrust.getRating())
    trials_2.addData('sliderTrust.rt', sliderTrust.getRT())
    trials_2.addData('text_2.started', text_2.tStartRefresh)
    trials_2.addData('text_2.stopped', text_2.tStopRefresh)
    # the Routine "TrustScale" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_2'

# get names of stimulus parameters
if trials_2.trialList in ([], [None], None):
    params = []
else:
    params = trials_2.trialList[0].keys()
# save data for this loop
trials_2.saveAsExcel(filename + '.xlsx', sheetName='trials_2',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "StartTeil2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
StartTeil2Components = [textMain, key_resp_2]
for thisComponent in StartTeil2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
StartTeil2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "StartTeil2"-------
while continueRoutine:
    # get current time
    t = StartTeil2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=StartTeil2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textMain* updates
    if textMain.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textMain.frameNStart = frameN  # exact frame index
        textMain.tStart = t  # local t and not account for scr refresh
        textMain.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textMain, 'tStartRefresh')  # time at next scr refresh
        textMain.setAutoDraw(True)
    
    # *key_resp_2* updates
    if key_resp_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        key_resp_2.clock.reset()  # now t=0
        key_resp_2.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StartTeil2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "StartTeil2"-------
for thisComponent in StartTeil2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "StartTeil2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Test1"-------
continueRoutine = True
# update component parameters for each repeat
key_TestStart.keys = []
key_TestStart.rt = []
_key_TestStart_allKeys = []
# keep track of which components have finished
Test1Components = [textTest, key_TestStart]
for thisComponent in Test1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Test1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Test1"-------
while continueRoutine:
    # get current time
    t = Test1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Test1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textTest* updates
    if textTest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textTest.frameNStart = frameN  # exact frame index
        textTest.tStart = t  # local t and not account for scr refresh
        textTest.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textTest, 'tStartRefresh')  # time at next scr refresh
        textTest.setAutoDraw(True)
    
    # *key_TestStart* updates
    if key_TestStart.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_TestStart.frameNStart = frameN  # exact frame index
        key_TestStart.tStart = t  # local t and not account for scr refresh
        key_TestStart.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_TestStart, 'tStartRefresh')  # time at next scr refresh
        key_TestStart.status = STARTED
        # keyboard checking is just starting
        key_TestStart.clock.reset()  # now t=0
        key_TestStart.clearEvents(eventType='keyboard')
    if key_TestStart.status == STARTED:
        theseKeys = key_TestStart.getKeys(keyList=['space'], waitRelease=False)
        _key_TestStart_allKeys.extend(theseKeys)
        if len(_key_TestStart_allKeys):
            key_TestStart.keys = _key_TestStart_allKeys[-1].name  # just the last key pressed
            key_TestStart.rt = _key_TestStart_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Test1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Test1"-------
for thisComponent in Test1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Test1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_5 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Test.xlsx', selection='0:4'),
    seed=None, name='trials_5')
thisExp.addLoop(trials_5)  # add the loop to the experiment
thisTrial_5 = trials_5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
if thisTrial_5 != None:
    for paramName in thisTrial_5:
        exec('{} = thisTrial_5[paramName]'.format(paramName))

for thisTrial_5 in trials_5:
    currentLoop = trials_5
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
    if thisTrial_5 != None:
        for paramName in thisTrial_5:
            exec('{} = thisTrial_5[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Testphase"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    image.setImage(ImageTest)
    # keep track of which components have finished
    TestphaseComponents = [image]
    for thisComponent in TestphaseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TestphaseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Testphase"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = TestphaseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TestphaseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TestphaseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Testphase"-------
    for thisComponent in TestphaseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "ImageResponse"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    ImageResponseComponents = [textAnswerOptions, key_resp]
    for thisComponent in ImageResponseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ImageResponseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ImageResponse"-------
    while continueRoutine:
        # get current time
        t = ImageResponseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ImageResponseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textAnswerOptions* updates
        if textAnswerOptions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textAnswerOptions.frameNStart = frameN  # exact frame index
            textAnswerOptions.tStart = t  # local t and not account for scr refresh
            textAnswerOptions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textAnswerOptions, 'tStartRefresh')  # time at next scr refresh
            textAnswerOptions.setAutoDraw(True)
        
        # *key_resp* updates
        if key_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            key_resp.clock.reset()  # now t=0
            key_resp.clearEvents(eventType='keyboard')
        if key_resp.status == STARTED:
            theseKeys = key_resp.getKeys(keyList=['x', 'v', 'm'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[0].name  # just the first key pressed
                key_resp.rt = _key_resp_allKeys[0].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ImageResponseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ImageResponse"-------
    for thisComponent in ImageResponseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials_5.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials_5.addData('key_resp.rt', key_resp.rt)
    # the Routine "ImageResponse" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_5'

# get names of stimulus parameters
if trials_5.trialList in ([], [None], None):
    params = []
else:
    params = trials_5.trialList[0].keys()
# save data for this loop
trials_5.saveAsExcel(filename + '.xlsx', sheetName='trials_5',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "StartMain"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
StartMainComponents = [text_StartMain, key_resp_4]
for thisComponent in StartMainComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
StartMainClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "StartMain"-------
while continueRoutine:
    # get current time
    t = StartMainClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=StartMainClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_StartMain* updates
    if text_StartMain.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_StartMain.frameNStart = frameN  # exact frame index
        text_StartMain.tStart = t  # local t and not account for scr refresh
        text_StartMain.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_StartMain, 'tStartRefresh')  # time at next scr refresh
        text_StartMain.setAutoDraw(True)
    
    # *key_resp_4* updates
    if key_resp_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        key_resp_4.clock.reset()  # now t=0
        key_resp_4.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StartMainComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "StartMain"-------
for thisComponent in StartMainComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "StartMain" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "con"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
conComponents = []
for thisComponent in conComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
conClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "con"-------
while continueRoutine:
    # get current time
    t = conClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=conClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in conComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "con"-------
for thisComponent in conComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "con" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Order'+condition+'.xlsx', selection='0:193'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Main"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    image_Main.setImage(ImageFiles)
    # keep track of which components have finished
    MainComponents = [image_Main]
    for thisComponent in MainComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    MainClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Main"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = MainClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=MainClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_Main* updates
        if image_Main.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_Main.frameNStart = frameN  # exact frame index
            image_Main.tStart = t  # local t and not account for scr refresh
            image_Main.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_Main, 'tStartRefresh')  # time at next scr refresh
            image_Main.setAutoDraw(True)
        if image_Main.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_Main.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                image_Main.tStop = t  # not accounting for scr refresh
                image_Main.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_Main, 'tStopRefresh')  # time at next scr refresh
                image_Main.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in MainComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Main"-------
    for thisComponent in MainComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('image_Main.started', image_Main.tStartRefresh)
    trials_3.addData('image_Main.stopped', image_Main.tStopRefresh)
    
    # ------Prepare to start Routine "ImageResponse"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    ImageResponseComponents = [textAnswerOptions, key_resp]
    for thisComponent in ImageResponseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ImageResponseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ImageResponse"-------
    while continueRoutine:
        # get current time
        t = ImageResponseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ImageResponseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textAnswerOptions* updates
        if textAnswerOptions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textAnswerOptions.frameNStart = frameN  # exact frame index
            textAnswerOptions.tStart = t  # local t and not account for scr refresh
            textAnswerOptions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textAnswerOptions, 'tStartRefresh')  # time at next scr refresh
            textAnswerOptions.setAutoDraw(True)
        
        # *key_resp* updates
        if key_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            key_resp.clock.reset()  # now t=0
            key_resp.clearEvents(eventType='keyboard')
        if key_resp.status == STARTED:
            theseKeys = key_resp.getKeys(keyList=['x', 'v', 'm'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[0].name  # just the first key pressed
                key_resp.rt = _key_resp_allKeys[0].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ImageResponseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ImageResponse"-------
    for thisComponent in ImageResponseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials_3.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials_3.addData('key_resp.rt', key_resp.rt)
    # the Routine "ImageResponse" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_3'

# get names of stimulus parameters
if trials_3.trialList in ([], [None], None):
    params = []
else:
    params = trials_3.trialList[0].keys()
# save data for this loop
trials_3.saveAsExcel(filename + '.xlsx', sheetName='trials_3',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "Ende"-------
continueRoutine = True
# update component parameters for each repeat
ENDE.keys = []
ENDE.rt = []
_ENDE_allKeys = []
# keep track of which components have finished
EndeComponents = [textbox, text_VPNCode, ENDE]
for thisComponent in EndeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Ende"-------
while continueRoutine:
    # get current time
    t = EndeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textbox* updates
    if textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textbox.frameNStart = frameN  # exact frame index
        textbox.tStart = t  # local t and not account for scr refresh
        textbox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
        textbox.setAutoDraw(True)
    
    # *text_VPNCode* updates
    if text_VPNCode.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_VPNCode.frameNStart = frameN  # exact frame index
        text_VPNCode.tStart = t  # local t and not account for scr refresh
        text_VPNCode.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_VPNCode, 'tStartRefresh')  # time at next scr refresh
        text_VPNCode.setAutoDraw(True)
    
    # *ENDE* updates
    waitOnFlip = False
    if ENDE.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ENDE.frameNStart = frameN  # exact frame index
        ENDE.tStart = t  # local t and not account for scr refresh
        ENDE.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ENDE, 'tStartRefresh')  # time at next scr refresh
        ENDE.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(ENDE.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(ENDE.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if ENDE.status == STARTED and not waitOnFlip:
        theseKeys = ENDE.getKeys(keyList=['space'], waitRelease=False)
        _ENDE_allKeys.extend(theseKeys)
        if len(_ENDE_allKeys):
            ENDE.keys = _ENDE_allKeys[-1].name  # just the last key pressed
            ENDE.rt = _ENDE_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Ende"-------
for thisComponent in EndeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textbox.text',textbox.text)
textbox.reset()
# the Routine "Ende" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
