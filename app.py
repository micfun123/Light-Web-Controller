from flask import Flask, render_template, request, jsonify
import time
import board
import neopixel

app = Flask(__name__)

pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 50

ORDER = neopixel.RGB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)


@app.route('/')
def index():
    pixels.fill((0, 0, 0))
    return render_template('index.html')


@app.route('/colours', methods=['POST'])
def colours():
    data = request.json
    colour = data.get('colourdata')
    print(colour)
    colour = colour.lstrip('#')
    colour = tuple(int(colour[i:i+2], 16) for i in (0, 2, 4))
    pixels.fill(colour)
    print(colour)
    return jsonify({"message":"colour recived"})



if __name__ == '__main__':
    app.run(debug=True)