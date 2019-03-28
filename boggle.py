import itertools
# Input: dictionary[] = {"GEEKS", "FOR", "QUIZ", "GO"};
#        boggle[][]   = {{'G','I','Z'},
#                        {'U','E','K'},
#                        {'Q','S','E'}};

# first, read the board and make a map of char -> indexes
# then for each word,  roll through it, seeing if you can construct it
# i guess the interesting thing is remembering subwords. a trie for e.g. cat catch catchers

# dic is set of words, board is array of char arrays, assume non-jagged
# return all words on board
def find_words(dic, board):

    # are points adjacent on board?
    def adjacent(p1, p2):
        return abs(p1[0] - p2[0]) < 2 and abs(p1[1] - p2[1]) < 2 and p1 != p2

    paths_trie = {} # for trie: char -> (path_to_get_here, suffixes)
    char_locs = {} # char -> [(x, y), ..] locations.  

    for ix, row in enumerate(board):
        for iy, char in enumerate(row):
            char_locs.setdefault(char, []).append((ix, iy))

    # Recursion down the path_trie, eating up the string, updating trie if we're on a new word
    def contains(word, paths, path_trie):
        char = word[0] # assume non-empty word
        tail = word[1:]
        # we don't have this char on the board
        if not char in char_locs: 
            return False # 

        # we have not been this way before, populate trie if we can reach this char.
        if not char in path_trie:
            new_paths = [path + [p] for (path, p) in itertools.product(paths or [[]], char_locs[char]) if not p in path and (len(path) == 0 or adjacent(path[-1], p))]
            if len(new_paths) == 0:
                return False
            else:
                path_trie[char] = (new_paths, {})
        # proceed
        return len(tail) == 0 or contains(tail, *path_trie[char])

    return [word for word in dic if contains(word, None, paths_trie)]

#words = ["gob", "go", "it", "b", "g", "gog"]
#board = [["g", "t"],["b", "o"]]

words = ["SEEKS", "GEEKS", "FOR", "QUIZ", "GO", "SEEK"]
board = [['G','I','Z'], ['U','E','K'], ['Q','S','E']]
print(find_words(words, board))
                
