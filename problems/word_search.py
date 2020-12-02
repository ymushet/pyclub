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
    >>> main([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB")
    True
    """
    for i, row in enumerate(board):
        for j, square in enumerate(row):
            if square == word[0]:
                res = neighbors(board, word, i, j)
                if res:
                    return True
    return False

def neighbors(board, word, i, j):
    if len(word) == 1 and board[i][j] == word[0]:
        return True

    w = word[1]
    board[i][j] = '#'
    x = len(board) - 1 # height
    y = len(board[0]) - 1 # weight

    # top
    if i - 1 >= 0 and w == board[i - 1][j]:
        res = neighbors(board, word[1:], i - 1, j)
        if res:
            return True
    # bottom
    if i + 1 <= x and w == board[i + 1][j]:
        res = neighbors(board, word[1:], i + 1, j)
        if res:
            return True
    # left
    if j - 1 >= 0 and w == board[i][j - 1]:
        res = neighbors(board, word[1:], i, j - 1)
        if res:
            return True
    # right
    if j + 1 <= y and w == board[i][j + 1]:
        res = neighbors(board, word[1:], i, j + 1)
        if res:
            return True

    return False

if __name__ == "__main__":
    doctest.testmod()
    # main([["C","A","A"],
    #       ["A","A","A"],
    #       ["B","C","D"]],"AAB")