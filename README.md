
# Python Real-Time Combat Simulator
I created a simple combat simulator to get experience with developing GUIs in Python. I intended to show this to a local group of Python developers, and chose **tkInter** as the application's UI library because it ships with Python on Linux/Windows, so no additional installation is required for other users to install and run the application.

### Overview
The application has two UI states: `UNIT_INPUT` and `COMBAT`.  
The application starts in the `UNIT_INPUT` state, where users can add/edit/delete units from the simulation (see below). Users can also run a simulation in "headless mode", which will simulate 1,000 battles and display the attackers' chance of winning the battle.
![image](https://github.com/user-attachments/assets/877d87a4-1fa1-47d1-aab7-dc2f5eab1170)

Once the user is satisfied with the units specified, they move to the `COMBAT` state by pressing `Enter`. In this state, the simulation will run in real-time until the battle is finished, and users have the option to change simulation speed and pause the battle. A demo of the combat simulation can be seen below.  

https://github.com/user-attachments/assets/4e06eca9-e975-4fb8-ace9-6994750d2782


### Run Instructions
Download the project files. Run `python main_ui.py` to start the combat sim.  
**Note: this project requires Python 3 and tkInter to run. Mac installations of Python 3 may not automatically have tkInter installed.**

Press `Enter` to switch between adding units and the battle screen. Press `R` on the unit input screen to run headless mode.
On the battle screen, press `Space` twice to start the simulation (use `Space` to pause/resume afterwords). You can also use the `left`/`right` arrow keys to change the simulation speed.

### Simulation Mechanics




This is a list of mechanics used in the simulation:  
[Combat](/docs/combat.md)  
[Feature Ideas](/docs/future.md)  
[Units](/docs/units.md)  

### Lessons Learned
Developing UI with tkInter was difficult for a number of reasons; documentation on tkInter is sparse and often outdated. tkInter's `sticky` property (essentially the tkInter version of `flex-grow` in CSS) must be manually set on all UI elements that should resize as the application window changes size, and getting even the simple UI it has now to work with that was a nightmare. tkInter also doesn't have a standard number input out of the box, so you have to use validation with a string input box, which is really weird.

tkInter is very similar to Swing for Java GUIs, and was an interesting change from working with HTML - it's much easier to rapidly prototype UI with HTML/CSS, and although both use hierarchies to organize UI, the syntax of HTML makes it much easier to understand (which made debugging UI elements' `sticky` property difficult in tkInter).

I was surprised to find tkInter wasn't installed on standard Python 3 installations for the Mac user who demoed the application, but the program was designed primarily for Windows/Linux, so I don't consider that a failure for the project.

If I developed Python UIs in the future, I would use a different library like PyQt - tkInter coming with the standard installation is great, but the documentation is really lacking to the point where it'd be more worth just installing extra third-party libraries that are easier to use.
