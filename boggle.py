from string import ascii_uppercase
from random import choice

def make_grid(width, height):
    grid = { (row,col) : choice(ascii_uppercase) 
                for row in range(height) 
                    for col in range(width) }
    return grid

def neighbours_of_position(coords):
    row, col = coords
    return [
        (row-1, col-1),
        (row-1, col),
        (row-1, col+1),
        (row, col-1),
        (row, col+1),
        (row+1, col-1),
        (row+1, col),
        (row+1, col+1)
        ]

def real_grid_neighbours(grid):
    real_neighbours = {}
    for square in grid:
        neighbours = neighbours_of_position(square)
        neighbours = [ n for n in neighbours if n in grid]
        real_neighbours[square] = neighbours
    return real_neighbours

def path_to_word(grid, path):
    word = ""
    for square in path:
        word += grid[square]
    return word

def load_wordlist(file):
    stems = set()
    words = set()
    with open(file) as f:
        wordlist = f.read().split('\n')
    for word in wordlist:
        word = word.upper()
        words.add(word)
        stems_of_word = [ word[:i]  for i in range(1, len(word))]
        for stem in stems_of_word:
            stems.add(stem)
    return (words, stems)

def search(grid, words_and_stems):
    wordlist, stemlist = words_and_stems
    neighbours = real_grid_neighbours(grid)
    words = []
    def do_search(path):
        word = path_to_word(grid, path)
        if word in wordlist:
            words.append(word)
        if word not in stemlist:
            return
        for next_pos in neighbours[path[-1]]:
            if next_pos not in path:
                do_search(path + [next_pos])
    for position in grid:
        do_search([position], )
    return words

def main():
    """
    This is the function that will run the whole project
    """
    grid = make_grid(4, 4)
    words_and_stems = load_wordlist("words.txt")
    words = search(grid, words_and_stems)
    for word in words:
        print(word)
    print("Found %s words" % len(words))

if __name__ == "__main__":
    # Code in here will only execute when the file is run directly    
    main()

