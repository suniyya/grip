Set Up



Components:

Stimulus Presentation Program

Lab Streaming Layer

MATLAB scripts for recording

Ultrasound System





Dependencies:

Windows 10/11 needed.

PsychoPy version x

Python version x

Python packages in virtual environment

MATLAB v 2020b

Lab Recorder App version x

liblsl-Matlab version x # do not set up the mex files. They come preinstalled. Don't touch them.

MATLAB add-ons: minGW C++/Fortran Compiler (in case needed to build mex files)

MATLAB add-on: Image Processing Toolbox

MATLAB add-on: Support Package for USB Webcams

MATLAB add-on: Parallel Computing Toolbox

MATLAB add-on: Data Acquisition Toolbox

epiphan DVI2USB3.0 drivers and capture recording software from https://www.epiphan.com/support/dvi2usb-3-0-software-documentation/

EMGWorks software
Installing this requires knowing your Delsys system identification number. In our case, this is: .

Need two free SS/ USB 3.0 ports for Terasons. Need one free USB-C or HDMI to connect a second screen).



GRIP Task

This experiment aims to investigate the neural correlates of attempted motor grasps in children born missing a hand. Participants are asked to attempt various hand movements using their intact and missing hand.

The GRIP task comprises of 5 functional runs.
The code for the PsychoPy task, as well as stimuli and trial orders for each run are in the grip\_task folder.

Parameters

Prompt display duration: 2 seconds

Grasp hold: 3.5 seconds

Relax: 2.5 seconds

Number of grasps per block: 4

Inter-block interval: 6 seconds (from relax period of last grasp to prompt of next grasp)

Number of grasps per run: 10 (5 grasps, 2 limbs)

Run time of one run: 5 min 48 seconds.

Stimuli:

5 grasps are used in this experiment: power, pinch, point, wrist extension and wrist flexion. The first three were chosen as they are useful in activities of daily living and visually distinct and involve different muscle contractions. The latter two were chosen because they involve a different set of muscle groups than the first three and because they may result in a greater cortical signal because of more motor units being involved.

The purpose of the study was to understand whether the neural representations of distinct hand grasps are distinguishable in the cortical motor areas of children born missing a hand.

Task:

Participants are shown a grayscale picture of a grasp on either the right or left side of the screen (2.5 s). This prompt then disappears, and a green dot appears for 3.5s and disappears for 2.5s. This happens 4 times for each grasp. The participant must make and hold the prompted grasp with their left or right hand (depending on where the image appears) repeatedly. Then there is a 6 second break, and another grasp block begins. Each grasp block consists of 4 repetitions of one grasp with one hand.

Order of grasps and hand side is randomized across runs, with the constraint that the same hand side should not be used for more than two grasps in a row, to avoid build up of fatigue.

Note: The trial order for each run is kept the same across participants. The side of the affected or unaffected limb may vary across participants.



Is it okay that same limb can appear twice in a row. Generated random trial order files for runs.

Chose 5 such that 3 start with R, 2 with L, balanced enough...

