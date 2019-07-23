#the position store:
def tic_tac_toe():
    positioning={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
    winner='Not yet'
    def pick_flag(flag):
        pick_again=True
        while pick_again:
            if flag=="X":
                player_flag={'Player 1':'X','Player 2':'O'}
                pick_again=False
            elif flag=="O"
                player_flag={'Player 1':'O','Player 2':'X'}
                pick_again=False
            else:
                print('The game has only two side to pick: X and O')
                print('Please pick again')
                continue
            return player_flag    
        flag=input("""Hi, you are player 1, which flag 
            would you chose?, X or O:""")

        def pixel_display(position):
            a=positioning[1]
            b=positioning[2]
            c=positioning[3]
            d=positioning[4]
            e=positioning[5]
            f=positioning[6]
            g=positioning[7]
            h=positioning[8]
            i=positioning[9]
            print(f"""
                {g} | {g} | {i}
                ----------
                {d} | {e} | {f}
                ----------
                {a} | {b} | {c}""")