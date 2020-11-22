import doctest

"""
See https://leetcode.com/problems/word-search/

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

[A B C E]
[S F C S]
[A D E E]

"ABCCED" => True
"SEE" => True
"ABCBQ" => False
"""

def main(board, word):
    """
    >>> main([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], "ABCCED")
    True
    >>> main([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], "SEE")
    True
    >>> main([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], "ABCBQ")
    False
    """
    for i, row in enumerate(board):
        for j, square in enumerate(row):
            if square == word[0]:
                res = neighbors(board, word[1:], i, j)
                if res:
                    return True
    return False

def neighbors(board, word, i, j):
    if len(word) == 1:
        return True

    w = word[0]
    print(w)
    board[i][j] = '#'

    x = len(board) # height
    y = len(board[0]) # weight

    if i - 1 >= 0 and w == board[i - 1][j]:
        neighbors(board, word[1:], i - 1, j)
    # bottom
    elif i + 1 <= x and w == board[i + 1][j]:
        neighbors(board, word[1:], i + 1, j)
    # left
    elif j - 1 >= 0 and w == board[i][j - 1]:
        neighbors(board, word[1:], i, j - 1)
    # right
    elif j + 1 <= y and w == board[i][j + 1]:
        neighbors(board, word[1:], i, j + 1)

    return False

if __name__ == "__main__":
    doctest.testmod()