# Flask application that does the following:
# 1. Display an html page on a Raspberry Pi based temperature controller (project here: https://github.com/ludwigkeyser/TempController/)
# 2. Displays the current temperature as measured by a thermocouple and thermocouple amp attached to the RPi
# 3. Toggles the temperature controller on and off via a form on the page. On means a relay board attached to the RPi is signalled to 
# "close" i.e. complete a circuit when the temperature measured by the thermocouple drops below a certain temp, and to "open" i.e. break
# the circuit when a certain temparature is reached. The circuit should be connected to a heating element of some sort, likely an incandescent globe.
# 4. TODO: Show a graph recording the recent temperature history

# Import the libraries required to read the temperature
import board
import digitalio
import adafruit_max31855

# Import the Flask libraries for displaying an html page and initiate
from flask import Flask
app = Flask(__name__)

# Set the model and parameters of the type of thermocouple used (Thermocouple Amplifier MAX31855 breakout board (MAX6675 upgrade) in my case)
spi = board.SPI()
cs = digitalio.DigitalInOut(board.D5)
max31855 = adafruit_max31855.MAX31855(spi, cs)

@app.route('/')
def main_page():
    tempNow = max31855.temperature
    return tempNow


if __name__ == '__main__':
    app.run(debug = True, host="0.0.0.0")
