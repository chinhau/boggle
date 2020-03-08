
## Apple Siri Team - Coding Exercise

#### Dependencies:

> - tkinter, shutil, string, nltk

#### Description 

> - Create a board game that find words that can be formed by a sequence of adjacent letters.

> - Constraints: minimum word length = 3, no repetitive instance.


#### Execution Plan 

1.  Generate Game Board Function (2 Options)
    - Option 1: User Input - 16 characters, check all alphabetical.
    - Option 2: Auto Generate (default options)
    - Input: board size (n)

    Create the generate game board function 
    - two options: user input or auto generate (default)
    - with user input, need to verify all 16 characters are alphabetical.
    - auto generate requires some heavy-lifting when it comes to optimizing the number of words match.

2.  Create trie - hold all words
    - Create Class Trie (leaf: dictionary of characters)
    - One Time Thing.

3.  Implement DFS algorithm to find all possible words. 
    - Return all possible keywords

4.  Create GUI
    - Original Idea: Use Steve Jobs's GIF but realize we couldn't render GIF using PyGame.
    - Stick to tkinter

5.  Due to time constraint: 
    - Didn't get to implement 2 players GUI. 
