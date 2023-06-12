# Stockfish API Wrapper
Simple Stockfish API wrapper. Allows users to access powerful chess engine 
functionality, retrieve moves and evaluations from FEN and complete use of all Stockfish 
methods from native c++ code. Provides a convenient way to access Stockfish from anywhere. The 
API Wrapper is used in my Mobile Application Development Course final, [Chess](https://github.com/vigneshsaravanakumar404/Chess). 



## Screenshots

#### Flask server running on localhost

![img_3.png](img_3.png)

#### Flask server mirroed on Ngrok
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


#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.




## Acknowledgements
- [Ngrok](https://ngrok.com/)
- [SVG Graphics Explanation](https://developer.mozilla.org/en-US/docs/Web/SVG)
- [Stockfish 3.28.0 Pypi](https://pypi.org/project/stockfish/)
- [Python API Explanation](https://www.youtube.com/watch?v=5ZMpbdK0uqU&t=7s&ab_channel=Indently)
- [Awesome README](https://github.com/matiassingers/awesome-readme)


# Images for later


