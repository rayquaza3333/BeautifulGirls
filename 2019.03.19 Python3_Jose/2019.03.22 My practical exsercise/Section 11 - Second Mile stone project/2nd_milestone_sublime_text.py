	#1 First, We set up things to play here.
	#2  Let say something:
	#3 :Check if ether side have won	
	#4 First Turn start.
from function_sublime import shuffle
from function_sublime import check_black_jack
from function_sublime import compare
from function_sublime import total_cards_create
from class_sublime import Casino
from class_sublime import Player
from class_sublime import Dealer
while True:
	
#1 First,Let say something:

	print("""

	Hi, welcome to Pham Hoang Casino.
	You are going to play again one of my best employee: The Dealer.
	He could be nightmare to all pro player all over the world. So please be carefull ;)

	Here let me explain some basic Rule of this game:
		1/ At first You and Dealer will have the start Balance.

		2/ You put a bet amount on your win.

		3/ You will receive the cards. Goal is to have higher score without Bust -Mean Above 21 score.

		4/ You can not hold your card if your score is below 17.

		5/ If you or Dealer have Black Jack, the Game stop imediately. 
		Bet amount belong the whom have Black Jack
		
		6/ You can chose to surrender, stop the round and secure half of your bet amount. Or you also can 
		chose double down which mean double up your bet amount.

	Ok, that's it. Losing money teach you tough, earn money give you happiness.
	I wish you my best blessing.

			""") 

#2  We set up things to play here. If the game ended and Player chose to replay. New loop starts from here
	replay='None'
	total_cards=total_cards_create()
	player=Player() #sub class of Casino class
	dealer=Dealer() #sub class of Casino class
	turn=0 	
	late_surrender='no'

#3 :Check if ether side have won. 

	while True: 

#End of each win, the loop come back to here
		#Revise cards after each round:

		cards_left=['#'].append(list(range(0,53)))
	
	#This block is to check if ether side have won the whole game.

		while player.balance == 0 or dealer.balance == 0: #End game condition
			if player.balance == 0: #Player lose
				print("Sorry but you run out of your money. We have to stop here. Do you want to play another game?")
				replay=input()
				try:
					replay.capitalize() == 'Yes' or replay.capitalize() == "No"
				except:
					print("This is not a valid input. Please try again") 
					continue
				else:
					if  replay.capitalize() == 'Yes':
						replay = 'Yes'
						break
					elif replay.capitalize() == "No":
						replay = "No"
						break
			else: 					#Dealer lose
				print("Oh you are God of Casino. You beaten our nightmare. His wallet is now empty")
				replay=input()
				try:
					replay.capitalize() == 'Yes' or replay.capitalize() == "No"
				except:
					print("This is not a valid input. Please try again") 
					continue
				else:
					if  replay.capitalize() == 'Yes':
						replay = 'Yes'
						break
					elif replay.capitalize() == "No":
						replay = "No"
						break

#Block of code inside this else is game play. The below code can only end by continue. This break when the turn end.	
#If none of end game block above was execute. Things go on from here.				

		else: 
		#4 First Turn start.

		#give cards to player
			print("A new round has began")
			player.take_card(shuffle(cards_left))
			player.take_card(shuffle(cards_left))
			dealer.take_card(shuffle(cards_left))
			dealer.take_card(shuffle(cards_left))
			player.bet()	
			player.score_cal()
			player.show_card()
			dealer.score_cal()	
			dealer.show_card()
			player.decision()

			#Update bet status

			if player.surrender == 'Yes':
				print("OK, players have surrendered. Dealer take half of the bet amount")	
				player.balance -= player.bet_amount/2
				dealer.balance += player.bet_amount/2
				dealer.show_all()
				player.surrender = 'No'
				continue
			elif player.double_down == 'Yes':
				player.bet_amount+=player.bet_amount
				player.double_down='No'
			else:
				pass

			#check black Jack

			a,b = check_balack_jack(player.score,dealer.score)
			if a == 'Black Jack':
				if b == 'Push':
					continue
				if b == 'Dealer':
					player.balance -= player.bet_amount
					dealer.balance += player.bet_amount
					continue
				if b == 'Player':
					player.balance += player.bet_amount
					dealer.balance -= player.bet_amount
					continue


			while True:
 				#second round here?
				print(f"So, no Black Jack found. We move to turn {turn + 1} ")
				if turn != 0: #To avoid repeating below block which was excute once at the beginning
						player.score_cal()
						player.show_card()
						dealer.score_cal()	
						dealer.show_card()
						player.decision()
				if player.surrender == 'Yes':
					print("OK, players have surrendered. Dealer take half of the bet amount")	
					player.balance -= player.bet_amount/2
					dealer.balance += player.bet_amount/2
					dealer.show_all()	
					player.surrender = 'No'
					late_surrender='Yes'
					break					
				elif player.double_down == 'Yes':
					player.bet_amount+=player.bet_amount
				else: 
					pass
				dealer.hit_hold()
				player.hit_hold()

				if dealer.hit_hold == player.hit_hold == 'Hold':
					a,b = compare(player.score,dealer.score)
					if b == "Player":
						player.balance += player.bet_amount
						dealer.balance -= player.bet_amount
						break
					else:
						player.balance -= player.bet_amount
						dealer.balance += player.bet_amount
						break
				else:
					if dealer.hit_hold== 'Hit':
						dealer.take_card(shuffle(cards_left))
					if player.hit_hold== 'Hit':
						player.take_card(shuffle(cards_left))
					continue


		#this decide to replay another round or not	by late surrender/ 2 holds
		if late_surrender == 'Yes' or dealer.hit_hold == player.hit_hold == 'Hold':
			late_surrender = 'No'
			dealer.hit_hold = 'Na'
			player.hit_hold = 'Na'
			continue		

	#If ether side won the whole game. The above code was excuted. Below is to let the game know to replay or not.
		if replay == 'None':
			pass
		elif replay == 'Yes':
			continue
		elif replay == "No":
			print("Thank you for visiting our casino. Looking forward to seeing you soon")
			break

		 						

	



	


	
	

	