import flask
from flask import request, Response
from crossword import BestPuzzle

app = flask.Flask(__name__) 

@app.route('/generate_puzzle', methods=['POST'])
def generate_puzzle():
    data = request.json
    words = data.get('names', [])
    grid_width = data.get('width', 11)
    grid_height = data.get('height', 14)
    
    best_puzzle=BestPuzzle(words=words, grid_width=grid_width, grid_height=grid_height)
    best_puzzle.select_best_puzzle()
    print(best_puzzle.best_puzzle_text)
    return Response(best_puzzle.best_puzzle_text, mimetype='text/plain')

if __name__ == '__main__':
    app.run()