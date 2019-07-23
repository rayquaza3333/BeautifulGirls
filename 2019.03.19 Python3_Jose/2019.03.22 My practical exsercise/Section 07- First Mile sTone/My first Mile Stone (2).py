#!/usr/bin/env python
# coding: utf-8

# # Tic-tac-toe game

# In[3]:


## 0
#Display_the_play_ground_while_playing
#positioning=list(""*9)
def pixel_display(positioning):
    print(f"play ground is in the left board, positioning guide is the right board")
    print(f"Player 1's flag is {players_flag['Player 1']}")
    print(f"Player 2's flag is {players_flag['Player 2']}")
    print(f"{positionning_turn[9]}! It\'s your turn")
    print(f"""
\n{positioning[6]}  |  {positioning[7]}  |  {positioning[8]}              [7]  |  [8]  |  [9]
\n{positioning[3]}  |  {positioning[4]}  |  {positioning[5]}      :       [4]  |  [5]  |  [6]
\n{positioning[0]}  |  {positioning[1]}  |  {positioning[2]}              [1]  |  [2]  |  [3]""")
#1
# pick_flag_and_pick_player_first_turn
def pick_flag():
    '''
    No need to put any value to the argument
    '''
    while True:
        print("""Hi, you are player 1 ^.^""")
        while True:
            flag=input("""Which flag would you chose?, X or O:\n""")
            if flag.upper()=="X":
                players_flag={'Player 1':'X','Player 2':'O'}
                return players_flag
            elif flag.upper()=="O":
                players_flag={'Player 1':'O','Player 2':'X'}
                return players_flag
            else:
                print('The game has only two side to pick: X and O')
                print('Please pick again')
                continue
#2/
def first_turn():
    '''
    No need to put any value to the argument
    '''
    while positionning_turn[9]==None:
        import random
        if random.randint(1,2)==1:
            return 'Player 1'
        else:
            return 'Player 2'
#3/
def input_and_check():
    '''
    No need to put any value to the argument
    '''
    while True:
        move=input('Great, which move do you want to make?: \n')
        position_str_list=list(range(1,10))
        run=0
        for x in position_str_list:
            position_str_list[run]=str(x)
            run+=1
        if move in position_str_list:
            move=int(move)-1
            if positionning_turn[move]== 'X' or positionning_turn[move]== 'O':
                print("Aw the position has already been taken recently, don't you remember?")
                continue
            else:
                return move
        else:
            print("The input is out range from the given position. Please input again, friend!")
            continue
#4/
def move(move):
    positionning_turn[move]=players_flag[positionning_turn[9]]
    if positionning_turn[9]=='Player 1':
        positionning_turn[9]='Player 2'
    else:
        positionning_turn[9]='Player 1'
    return positionning_turn
#5/
def battle_check(p_t):
    win_slot=[[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [6, 4, 2]]
    for x in win_slot:
        if p_t[x[0]]==p_t[x[1]]==p_t[x[2]]=='X' or p_t[x[0]]==p_t[x[1]]==p_t[x[2]]=='O' :
            if p_t[x[0]]==players_flag['Player 1']:
                print('\n'*50)
                print("Congratulation! Player 1 is our winner")
                pixel_display(positionning_turn)
                print('Player 2. You guys want to make peace or play another round?')
                return 'End'
            elif p_t[x[0]]==players_flag['Player 2']:
                print('\n'*50)
                print("Congratulation! Player 2 is our winner")
                pixel_display(positionning_turn)
                print('Player 1. You guys want to make peace or play another round?')
                return 'End'
    if  set(p_t)=={'X','O','Player 1'} or set(p_t)=={'X','O','Player 2'}:
        print('\n'*50)
        print('All the positions have been pick. No winner have been set. You guys want to make peace or play another round?')
        print('Yes or No')
        return 'End'
    else:
        return 'Continue'
#6/
def game_replay(b_c):
    if b_c=='End':
        replay=input().capitalize()
        while replay not in ['Yes','No']:
            print('Please pick Yes or No')
            replay=input().capitalize()
            continue
        if replay=='Yes':
            return 'Yes'
        elif replay=='No':
            print('Thanks for having fun today. You all are great players')
            return 'No'
    else:
        return 'Continue'
#7/ THE GAME
while True:
    positionning_turn=list("*"*9)+[None]
    players_flag=pick_flag()
    positionning_turn[9]=first_turn()
    while True:
        print('\n'*50)
        pixel_display(positionning_turn)
        positionning_turn=move(input_and_check())
        replay=game_replay(battle_check(positionning_turn))
        if replay=='Yes':
            break
        elif replay=='No':
            break
        else:
            continue
    if replay=='Yes':
        print('\n'*100)
        continue
    else:
        import sys
        sys.exit(1)


# In[ ]:


replay not in ['Yes','No']


#

# In[ ]:


aasd=['x','y',1,'PLayer']
set(aasd)


# # 0/ pixel_display

# In[ ]:


positionning_turn[1]


# In[ ]:


positionning_turn[1]!='X' or positionning_turn[1]!='O'


# In[ ]:


#Display_the_play_ground_while_playing
#positioning=list(""*9)
def pixel_display(positioning):
    print(f"""play ground is in the left board, positionning guide is the right board
    \n{positioning[6]}  |  {positioning[7]}  |  {positioning[8]}              [7]  |  [8]  |  [9]
    \n{positioning[3]}  |  {positioning[4]}  |  {positioning[5]}      :       [4]  |  [5]  |  [6]
    \n{positioning[0]}  |  {positioning[1]}  |  {positioning[2]}              [1]  |  [2]  |  [3]""")


# In[ ]:


pixel_display(list("*"*9))


# #Display_the_play_ground_while_playing
# #positioning=[1,2,3,4,5,6,7,8,9]
# def pixel_display(positioning):
#     print(f"""
#     \n{positioning[6]}  |  {positioning[7]}  |  {positioning[8]}
#     \n{positioning[3]}  |  {positioning[4]}  |  {positioning[5]}
#     \n{positioning[0]}  |  {positioning[1]}  |  {positioning[2]}""")

# # 1/ pick_flag

# In[ ]:


# pick_flag_and_pick_player_first_turn
def pick_flag():
    '''
    No need to put any value to the argument
    '''
    pick_again=True
    while pick_flag:
        print("""Hi, you are player 1 ^.^""")
        while pick_flag:
            flag=input("""Which flag would you chose?, X or O:\n""")
            if flag.upper()=="X":
                players_flag={'Player 1':'X','Player 2':'O'}
                print(players_flag)
                return players_flag
            elif flag.upper()=="O":
                players_flag={'Player 1':'O','Player 2':'X'}
                print(players_flag)
                return players_flag
            else:
                print('The game has only two side to pick: X and O')
                print('Please pick again')
                continue


# In[ ]:


a=pick_flag()


# # 2/ Random first player

# In[ ]:


def first_turn():
    '''
    No need to put any value to the argument
    '''
    while positionning_turn[9]==None:
        import random
        if random.randint(1,2)==1:
            print('Player 1 take the first turn')
            return 'Player 1'
        else:
            print('Player 2 take the first turn')
            return 'Player 2'


# In[ ]:


import random
type(random.randint(1,2))


# # 3/ Input_and_check

# In[ ]:


def input_and_check():
    '''
    No need to put any value to the argument
    '''
    while True:
        move=input('Great, which move do you want to make?')
        position_str_list=list(range(1,10))
        run=0
        for x in position_str_list:
            position_str_list[run]=str(x)
            run+=1
        if move in position_str_list:
            move=int(move)-1
            if positionning_turn[move]!= 'X' or positionning_turn[move]!= 'O':
                return move
            else:
                print("Aw the position has already been taken recently, don't you remember?")
                continue
        else:
            print("The input is out range from the given position. Please input again, friend!")
            continue



# In[ ]:


input_check()


# In[ ]:


positionning_turn[move]=players_flag[positionning_turn[9]]


# # 4/ Input_move_and_return positionning

# In[ ]:


def move(move):
    positionning_turn[move]=players_flag[positionning_turn[9]]
    if positionning_turn[9]=='Player 1':
        positionning_turn[9]='Player 2'
    else:
        positionning_turn[9]='Player 1'
    return positionning_turn


# # 5/ Battle_check

# In[ ]:


def battle_check(p_t):
    win_slot=[[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 7], [0, 4, 8], [6, 4, 2]]
    for x in win_slot:
        if p_t[x[0]]==p_t[x[2]]==p_t[x[2]]=='X' or p_t[x[0]]==p_t[x[2]]==p_t[x[2]]=='O' :
            if p_t[x[0]]==players_flag['Player 1']:
                print("Congratulation! Player 1 is our winner")
                print('Player 2. You guys want to make peace or play another round?')
                return 'End'
            elif p_t[x[0]]==players_flag['Player 2']:
                print("Congratulation! Player 2 is our winner")
                print('Player 1. You guys want to make peace or play another round?')
                return 'End'
    if  set(p_t)==('X','O','Player 1')    and set(p_t)==('X','O','Player 2'):
        print('All the positions have been pick. No winner have been set. You guys want to make peace or play another round?')
        print('Yes or No')
        return 'End'
    else:
        return 'Continue'


# # 6/ Replay

# In[ ]:


def game_replay(b_c):
    if b_c=='End':
        replay='None'
        while replay not in ['Yes','No']:
            replay=input()
            print('Please pick Yes or No')
            continue
        if replay=='Yes':
            return 'Yes'
        elif replay=='No':
            print('Thanks for having fun today. You all are great player')
            return 'No'
    else:
        return 'Continue'




# In[ ]:


positionning_turn


# In[ ]:


'asdas'.count('as')


# In[ ]:


[[1-1,2-1,3-1],[4-1,5-1,6-1],[7-1,8-1,9-1],[1-1,4-1,7-1],[2-1,5-1,8-1],              [3-1,6-1,8-1],[1-1,5-1,9-1],[7-1,5-1,3-1]]


# In[ ]:





# In[ ]:
