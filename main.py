import nltk
import trie
import tkinter
import landing_page as lp
from nltk.corpus import words
import landing_page as lp
from setup import generate_board
from search_dfs import dfs, recursion
nltk.download('words')


def main():
    '''Main function.'''
    root = tkinter.Tk()
    window = lp.LandingPage(root)
    t = trie.Trie()
    dictionary = set(words.words())
    t.insert_words(dictionary)
    root.mainloop()
    num, board_size, input_string = window.retrieve_val()
    board = generate_board(num, board_size, input_string)
    # user define manually
    # dictionary = ['susan', 'susanie', 'sin', 'apple', 'orange', 'an']
    output = dfs(num, board, t)
    print("There are {} number of possible word choices".format(len(output)))
    # allow user to inspect output if interested.
    print(output, "\n")


if __name__ == "__main__":
    main()
