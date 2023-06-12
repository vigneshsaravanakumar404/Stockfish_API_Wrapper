# Stockfish API Wrapper
Simple Stockfish API wrapper. Allows users to access powerful chess engine 
functionality, retrieve moves and evaluations from FEN and complete use of all Stockfish 
methods from native c++ code. Provides a convenient way to access Stockfish from anywhere. The 
API Wrapper is used in my Mobile Application Development Course final, [Chess](https://github.com/vigneshsaravanakumar404/Chess). 


## Installation

Clone the project and Stockfish 15.1
```bash
  git clone https://github.com/vigneshsaravanakumar404/Stockfish_API_Wrapper.git
  git clone https://github.com/official-stockfish/Stockfish.git
```

Install dependencies

```bash
  pip install 
  pip stockfish 
  pip Flask 
  pip pyuac
```
Change stockfish path from
``` 
    STOCKFISH_PATH = "C:/Users/vigne/PycharmProjects/Stockfish_API_Wrapper/Stockfish/src/stockfish.exe"
```
to your stockfish path in app.py

Run the program and start Ngrok tunnel
```bash
  python app.py
  ngrok http 5000
```

## API Reference

#### Get best move based on elo

```http
  GET /api/bestmove/
```

| Parameter               | Type      | Description                                      |
|:------------------------|:----------|:-------------------------------------------------|
| `elo`                   | `int`     | **Required** Elo Stockfish will play at          |
| `contempt`              | `int`     | Aggression of Stockfish                          |
| `min-split-depth`       | `int`     | Minimum depth Stockfish will search to           |
| `ponder`                | `boolean` | Allow the engine to think during opponent's turn |
| `threads`               | `int`     | Number of threads Stockfish will use             |
| `multipv`               | `int`     | Number of best moves to return                   |
| `fen`                   | `string`  | **Required** FEN of board position               |
| `minimum-thinking-time` | `int`     | Minimum thinking time                            |
| `uci-chess960`          | `boolean` | Set Chess960                                     |
| `uci-limit-strength`    | `boolean` | Limit max Stockfish level                        |


#### Get best move based on level

```http
    GET /api/bestmove/
```
| Parameter               | Type      | Description                                      |
|:------------------------|:----------|:-------------------------------------------------|
| `skill-level`           | `int`     | **Required** Elo Stockfish will play at          |
| `contempt`              | `int`     | Aggression of Stockfish                          |
| `min-split-depth`       | `int`     | Minimum depth Stockfish will search to           |
| `ponder`                | `boolean` | Allow the engine to think during opponent's turn |
| `threads`               | `int`     | Number of threads Stockfish will use             |
| `multipv`               | `int`     | Number of best moves to return                   |
| `fen`                   | `string`  | **Required** FEN of board position               |
| `minimum-thinking-time` | `int`     | Minimum thinking time                            |
| `uci-chess960`          | `boolean` | Set Chess960                                     |
| `uci-limit-strength`    | `boolean` | Limit max Stockfish level                        |

#### Check if FEN is valid

```http
    GET /is-fen-valid/
```
| Parameter               | Type      | Description                        |
|:------------------------|:----------|:-----------------------------------|
| `fen`                   | `string`  | **Required** FEN of board position |

####  Check if move is valid

```http
    GET /is-move-correct/
```
| Parameter               | Type      | Description                        |
|:------------------------|:----------|:-----------------------------------|
| `fen`                   | `string`  | **Required** FEN of board position |
| `move`                  | `string`  | **Required** Move to check         |

#### Get evaluation of position

```http
    GET /get-evaluation/
```
| Parameter               | Type      | Description                        |
|:------------------------|:----------|:-----------------------------------|
| `fen`                   | `string`  | **Required** FEN of board position |

#### Get top moves

```http
    GET /get-top-moves/
```
| Parameter | Type     | Description                        |
|:----------|:---------|:-----------------------------------|
| `fen`     | `string` | **Required** FEN of board position |
| `number`  | `int`    | **Required** Number of moves       |

## Screenshots

#### Flask server running on localhost

![img_3.png](img_3.png)

#### Flask server tunnelled on Ngrok
![img_1.png](img_1.png)

#### Sample output for request of top 5 best moves in standard chess position
![img.png](img.png)


## Tech Stack
<div>
    <img src="https://raw.githubusercontent.com/tandpfun/skill-icons/59059d9d1a2c092696dc66e00931cc1181a4ce1f/icons/Python-Dark.svg" width="64" height="64" alt="Python">
    <img src="https://images.igdb.com/igdb/image/upload/t_cover_big_2x/ugtrhiksvdkmjekcbesf.jpg" width="64" height="64" alt="Stockfish">
    <img src="https://raw.githubusercontent.com/tandpfun/skill-icons/59059d9d1a2c092696dc66e00931cc1181a4ce1f/icons/Flask-Dark.svg" width="64" height="64" alt="Flask">
    <img src="https://raw.githubusercontent.com/vigneshsaravanakumar404/skill-icons/main/icons/Idea-Dark.svg" width="64" height="64" alt="IntelliJ IDEA">
</div>

## References
- [Ngrok](https://ngrok.com/)
- [SVG Graphics Explanation](https://developer.mozilla.org/en-US/docs/Web/SVG)
- [Stockfish 3.28.0 Pypi](https://pypi.org/project/stockfish/)
- [Python API Explanation](https://www.youtube.com/watch?v=5ZMpbdK0uqU&t=7s&ab_channel=Indently)
- [Awesome README](https://github.com/matiassingers/awesome-readme)



