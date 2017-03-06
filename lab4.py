total = 20
turn = 1
# player1 and player 2 take turn
while total > 0:

    print('|'*total)
    if turn == 1:
        player1 = input("1 enter the number")
        if player1 >= 1 and player1 <= 3:
            print("1 taken:{}".format(player1))
            turn = 2
            total -= player1
            if total<0:
                total = 0
                print("1 left:{}".format(total))
            else:
                print("1 left:{}".format(total))
        else:
            print("1 enter again")
    elif turn == 2:
        player2 = input("2 enter the number")
        if player2 >= 1 and player2 <= 3:
            total -= player2
            print("2 taken:{}".format(player2))
            turn = 1
            if total < 0:
                total = 0
                print("2 left:{}".format(total))
            else:
                print("2 left:{}".format(total))
        else:
            print("2 enter again")
if total <= 0 and turn == 2:
    print("player1 loses")
elif total <=0 and turn ==1:
    print("player 2 loses")
