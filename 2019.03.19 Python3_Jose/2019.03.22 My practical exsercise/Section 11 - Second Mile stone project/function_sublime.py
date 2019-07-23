#Create some function to use:
	#1/ shuffle()
	#2/ check_black_jack(player,dealer)
	#3/ compare(player,dealer)
	#4/ total_cards_create()

#shuffler()

def shuffle(cards_left):
	import random
	take_card_num=random.randint(1,len(cards_left)-1)
	return take_card_num

#check_black_jack(player,dealer) 
#Remenber to give condition: turn = 0

def check_black_jack(player,dealer):
	"""
	Return :
	1/ AA Black Jack for player/dealer
		1.1/ 'AA Black Jack' vs 'AA Black Jack' : Push
		1.2/ 'AA Black Jack' vs other: 'AA Black Jack' win
	2/ Black Jack for player/dealer
		2.1 'Black Jack' vs 'Black Jack': Push
		2.2 'Black Jack' vs other: 'Black Jack' win
	"""	
	#Case AA Black Jack
	if player == 'AA Black Jack' or dealer =='AA Black Jack': 
		if player == dealer == 'AA Black Jack':						#2 AA Black Jack
			print("This a a Push. Bet amount return to player")
			return 'Black Jack','Push'

		elif player == 'AA Black Jack':						#1 AA Black Jack
			print("Player have a AA Black Jack. Dealer lose the 
				bet amount")
			return 'Black Jack','Dealer'

		elif dealer == 'AA Black Jack':						#1 AA Black Jack
			print("Dealer have a AA Black Jack. Player lose the bet amount")
			return 'Black Jack','PLayer'
	#Case Black Jack
	elif player == 'Black Jack' or dealer =='Black Jack': 
		if player == dealer == 'Black Jack':        		#2 AA Black Jack
			print("This a a Push. Bet amount return to player")
			return 'Black Jack','Push'

		elif player == 'Black Jack':						#1 Black Jack
			print("Player have a Black Jack. Dealer lose the bet amount")
			return 'Black Jack','Dealer'

		elif dealer == 'Black Jack':						#1 Black Jack
			print("Dealer have a Black Jack. Player lose the bet amount")
			return 'Black Jack','PLayer'

	else:
			return 'None','None' # continure without any Black Jack win

#compare(player,dealer)
#Remenber to give condition: turn > 0\

def compare(player, dealer):
	"""
	1/ if both are >= 17 and <=21 : the higher score win
	2/ if both are >21: The one who is lower score win
	3/ If one is >21: The one who is lower than 21 win
	"""
	while dealer.hit_hold == player.hit_hold == hold:
		if player == dealer:
			print("This is a Push, no one win. Bet Amount return to Player")
			return 'Normal','Push'
		elif player > 21 and dealer > 21: #Both Bust
			if player < dealer:
				print("Player and Dealer have Bust, Player win due to lower score")
				return 'Bust',"Player"
			else: 
				print("Player and Dealer have Bust, Dealer win due to lower score")
				return 'Bust','Dealer'
		elif player > 21 or dealer > 21: # One Bust
			if player <= 21:
				print("Dealer have Bust, Player win due to lower score")
				return 'Bust',"Player"
			else: 
				print("Player have Bust, Dealer win due to lower score")
				return 'Bust','Dealer'
		else: 							# None Bust
			if player > dealer: 
				print("Player win due to higher score")
				return 'Normal','PLayer'
			else:
				print("Dealer win due to higher score")
				return 'Normal','Dealer'	

#total_cards_create()

def total_cards_create():
	u=['#']
	for i in ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']:
		u.append(i)
		u.append(i)    
		u.append(i)        
		u.append(i)        
	return u
