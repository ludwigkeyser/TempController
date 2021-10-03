# TempController
Python based code for a Raspberry Pi based temperature controller, used for maintaining precise temperature environments in bread baking (i.e. a proofing box) or in home beer brewing (i.e. in mashing or temp controlled fermenter)

Wednesday September 29 2021
User beware: I'm sure there are many other (possibly better) tutorials out there on building temperature controllers. I wanted to learn how to make one myself and learn a couple of new skills. As such, this is surely not the best / most effective / most elegant solution out there. It works, I use it and tweak it regularly, and you are more than welcome to use this tutorial and code as you wish. 

#TODO Describe Hardware build and components used

Code design
--------------

Key components:
 - Python 3.7.3 on a Raspbian Buster
 - Flask
 - #TODO link to relay board Python code
 - #TODO link to temp probe board code

Main Python script (automatically started by systemctl on boot)
 - Initiates components:
    - Relays off
    - Get initial temp every 1 min
    - Initiates control html page on localhost:5000/
 
  - On an HTML request on http://localhost:5000 
     - Display control page
       - On / off button
       - Submit button
       - The current temperature as measured by the thermocouple
       #TODO Implement AJAX / SiJax code to:
         - remove the need for the submit button, or so the on/off button enables and disables the relay on change events
         - update the temperature reading automatically every n seconds
         - add a trend graph over x hours showing the temp as measured
