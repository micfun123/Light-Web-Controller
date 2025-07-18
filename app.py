from flask import Flask, render_template, request, jsonify
import time
import board
import neopixel

app = Flask(__name__)
# The number of NeoPixels
num_pixels = 50
ORDER = neopixel.GRB


pixels = neopixel.NeoPixel(board.D18, 30, brightness=0.5, auto_write=False, pixel_order=neopixel.RGB)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/colours', methods=['POST'])
def colours():
    data = request.json
    colour = data.get('colourdata')
    print(colour)
    colour = colour.lstrip('#')
    colour = tuple(int(colour[i:i+2], 16) for i in (0, 2, 4))
    pixels.fill(colour)
    pixels.show()
    print(colour)
    return jsonify({"message":"colour recived"})



if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 8080,debug=False)