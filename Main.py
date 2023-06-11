from stockfish import Stockfish
from flask import *
import time
import pyuac

# Variables
app = Flask(__name__)
dict = []
stockfish = Stockfish(
    path=r"C:\\Users\\Vigne\\Downloads\\stockfish_15.1_win_x64_popcnt\\stockfish_15.1_win_x64_popcnt\\stockfish-windows-2022-x86-64-modern.exe")


# Contempt
# Min Split Depth
# Threads
# Ponder
# Hash
# Multi PV
# Skill Level
# Move Overhead
# Minimum Thinking Time
# Slow Mover
# UCI_Chess960
# UCI_LIMIT_STRENGTH
# UCI_Elo
# depth
# FEN


from flask import jsonify

# Error handlers
@app.errorhandler(400)
def bad_request_error(error):
    return jsonify({'error': 'Bad request'}), 400

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Methods
@app.route('/', methods=['GET'])
def home_page():
    return "Welcome to the Home Page!. Read the documentation for more info!\nGithub: " \
           "https://github.com/vigneshsaravanakumar404/Stockfish_API"


@app.route('/engine/elo/', methods=['GET'])
def new_engine_elo_page():
    try:
        contempt = str(request.args.get('contempt'))
        min_split_depth = str(request.args.get('min-split-depth'))
        ponder = str(request.args.get('ponder'))
        minimum_thinking_time = str(request.args.get('minimum-thinking-time'))
        uci_chess960 = str(request.args.get('uci-chess960'))
        uci_limit_strength = str(request.args.get('uci-limit-strength'))
        fen = str(request.args.get('fen'))

        elo = int(request.args.get('uci_elo')) or 1350

        dict.append(['Contempt', contempt])
        dict.append(['Min Split Depth', min_split_depth])
        dict.append(['Ponder', ponder])
        dict.append(['Minimum Thinking Time', minimum_thinking_time])
        dict.append(['UCI_Chess960', uci_chess960])
        dict.append(['UCI_LimitStrength', uci_limit_strength])

        parameters = {}
        for item in dict:
            if item[1] != "None":
                parameters[item[0]] = item[1]

        # Set default value for fen if it is not provided
        if fen is None:
            fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

        stockfish.update_engine_parameters(parameters)
        stockfish.set_fen_position(fen)
        stockfish.set_elo_rating(int(elo))

        return stockfish.get_best_move()

    except Exception as e:
        app.logger.error(str(e))
        return jsonify({'error': 'Erroneous input'}), 400


@app.route('/engine/level/', methods=['GET'])
def engine_level_page():
    try:
        contempt = str(request.args.get('contempt'))
        min_split_depth = str(request.args.get('min-split-depth'))
        ponder = str(request.args.get('ponder'))
        minimum_thinking_time = str(request.args.get('minimum-thinking-time'))
        uci_chess960 = str(request.args.get('uci-chess960'))
        uci_limit_strength = str(request.args.get('uci-limit-strength'))
        fen = str(request.args.get('fen'))

        skillLevel = int(request.args.get('skill-level')) or 1350

        dict.append(['Contempt', contempt])
        dict.append(['Min Split Depth', min_split_depth])
        dict.append(['Ponder', ponder])
        dict.append(['Minimum Thinking Time', minimum_thinking_time])
        dict.append(['UCI_Chess960', uci_chess960])
        dict.append(['UCI_LimitStrength', uci_limit_strength])

        parameters = {}
        for item in dict:
            if item[1] != "None":
                parameters[item[0]] = item[1]

        # Set default value for fen if it is not provided
        if fen is None:
            fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

        stockfish.update_engine_parameters(parameters)
        stockfish.set_fen_position(fen)
        stockfish.set_skill_level(int(skillLevel))

        return stockfish.get_best_move()

    except Exception as e:
        app.logger.error(str(e))
        return jsonify({'error': 'Erroneous input'}), 400


@app.route('/is-fen-valid/', methods=['GET'])
def is_fen_valid_page():
    try:
        fen = str(request.args.get('fen'))
        return str(stockfish.is_fen_valid(fen))

    except Exception as e:
        app.logger.error(str(e))
        return jsonify({'error': 'Erroneous input'}), 400


@app.route('/is-move-correct/', methods=['GET'])
def is_move_correct_page():
    try:
        fen = str(request.args.get('fen'))
        move = str(request.args.get('move'))
        stockfish.set_fen_position(fen)
        return str(stockfish.is_move_correct(move))

    except Exception as e:
        app.logger.error(str(e))
        return jsonify({'error': 'Erroneous input'}), 400


@app.route('/get-top-moves/', methods=['GET'])
def get_top_moves_page():
    try:
        fen = str(request.args.get('fen'))
        number = int(request.args.get('number'))
        stockfish.set_fen_position(fen)
        return str(stockfish.get_top_moves(number))

    except Exception as e:
        app.logger.error(str(e))
        return jsonify({'error': 'Erroneous input'}), 400


@app.route('/get-evaluation/', methods=['GET'])
def get_evaluation_page():
    try:
        fen = str(request.args.get('fen'))
        stockfish.set_fen_position(fen)
        return str(stockfish.get_evaluation())

    except Exception as e:
        app.logger.error(str(e))
        return jsonify({'error': 'Erroneous input'}), 400


def main():
    print(time.asctime(time.localtime(time.time())) + ": Starting server...")
    app.run(port=7777)
    print(time.asctime(time.localtime(time.time())) + ": Server started!")


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
