from stockfish import Stockfish
from flask import *
import json
import time
import pyuac

# Methods

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
    return ""


@app.route('/user/', methods=['GET'])
def request_page():
    user_query = str(request.args.get('user'))
    data_set = {'Output': user_query, 'Time': time.time()}
    json_dump = json.dumps(data_set)

    print(user_query)  # Print user_query to the console

    return json_dump


def main():
    app.run(port=7777)

    # Stock Fish cmds
    # stockfish = Stockfish(path=r"C:\Users\Vigne\Downloads\stockfish_15.1_win_x64_popcnt\stockfish_15.1_win_x64_popcnt\stockfish-windows-2022-x86-64-modern.exe", depth=18, parameters={"Threads": 2, "Minimum Thinking Time": 30})
    # stockfish.set_fen_position("r1bqkbnr/pppp1ppp/2n5/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 0 1")
    # print(stockfish.get_best_move())

    input("Press enter to close the window. >")


# Run as admin
if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        pyuac.runAsAdmin()
    else:
        main()

    # How to start
"""Fire it up: ngrok http 7777"""

# how to access from computer
"""

import requests
url = "https://c6a4-173-63-234-100.ngrok-free.app/"
headers = {
    "ngrok-skip-browser-warning": "true"
}

response = requests.get(url, headers=headers)
# Do something with the response
print(response.text)

"""

# Json output code
"""

data_set = {'Page': 'Home', 'Message': 'Welcome to the home page!', 'Time': time.time()}
    json_dump = json.dumps(data_set)

"""
