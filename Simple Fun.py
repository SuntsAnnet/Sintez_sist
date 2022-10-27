'''
Simple Fun #261: Whose Move
https://www.codewars.com/kata/59126992f9f87fd31600009b
'''
def whoseMove(lastPlayer, win):
    if lastPlayer =='black':
        other = 'white'
    else:
        other="black"
    if win:
        return(lastPlayer)
    else:
        return(other)