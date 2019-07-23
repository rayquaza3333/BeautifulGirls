#Create Class Casino, and subclass Player, Dealer

#Casino Class
	#Attribute:  1/cards, 2 / score 3/decision (double down/surrender. 4/ hit_hold) 
	#Method: 1/ take_card(card_num)  2/ score_cal() 

# Dealer Class
	#Attributes: 1/ balance 
	#Inheriated attribute 1/cards, 2 / score 3/decision (double down/surrender) 4/ hit_hold) 
	#Method:  1/Show card() 2/ hit_hold() 3/ show_all
	#Inheriated Method: 1/ take_card  2/ score_cal
#Player class
	#Attribute: 1/ bet_amount 2/ balance 3/ double_down
	#Inheriated attribute 1/cards, 2/decision (double down/surrender). 3/hit_hold) 4/ score 
	#	Method:  1/Show card()_ 2/ decision(): double down/surrender , 3/bet(), 4/hit_hold()
	#Inheriated Method: 1/ take_card  2/ score_cal


class Casino():
	"""
	This is mother class for dealer and Player
	Attribute:  1/cards, 2 / score  3/ hit_hold) 
	Method: 1/ take_card(card_num)  2/ score_cal() 
	"""
	cards=['#']
	score=0
	hit_hold='#'
	def __init__(self):
		pass
	def take_card(self,card_num,total_cards):
		"""
		Take card by index from cards_left. Have global statement for autmatically pop the card out
		"""
		self.cards.append(total_cards[card_num])
	def score_cal(self,turn):  
		"""
		Các giá trị có thể gán cho self.score:
			1/ Điểm
			2/ AA Black Jack
			3/ Black Jack
		"""
		
		for i in range(1,len(self.cards)): ## Tổng điểm khi chưa tính các quân Ace			  
			if type(self.cards[i])==int:
				self.score += self.cards[i]
			elif type(self.cards[i])==str:
				if self.cards[i] !='A':
					self.score += 10

		while turn ==0:
			if self.cards.count('A')==2: #Luot dau tien, 2 quan bai. AA >> AA Black Jack
				self.score='AA Black Jack'
				break
			elif self.cards.count('A')==1 and self.score == 10: #Luot dau tien, 2 quan bai. A+10 >> AA Black Jack
				self.score = 'Black Jack'
				break
		else:
			if self.cards.count('A')==2: # Cac luot tie theo. Co 2 con Ace tro len thi moi con tinh la 1 diem.
				for i in range(0,len(self.cards)):
					if self.cards[i]=='A':
						self.score+=1
			elif self.cards.count('A')==1: #Cac luot tiep theo, 1 con Ace.
				for i in range(0,len(self.cards)):
					if self.cards[i]=='A':
						if self.score < 11:
							self.score +=11
						elif self.score ==11:
							self.score +=10		
						elif self.score >11:
							self.score +=1	
		
		
class Dealer(Casino):
	"""\
	Attributes: 1/ balance 
	Inheriated attribute 1/cards, 2 / score 3/decision (double down/surrender) 4/ hit_hold) 
	Method:  1/Show card() 2/ hit_hold()
	Inheriated Method: 1/ take_card  2/ score_cal
	"""
	balance=10000

	def __init__(self):
		pass

	def show_card(self):
		print(f"The first card of dealer is: {dealer.cards[1]}")

	def hit_hold(self):
		if dealer.score <=16:
			dealer.hit_hold ='Hit'
		else:
			dealer.hit_hold = 'Hold'
	def show_all(self):
		u= self.cards
		u.pop(0)
		print(f"Your cards are {u}")
		print(f"and your score is {self.score}")



class Player(Casino):
	"""
	Attribute: 1/ bet_amount 2/ balance 3/ double_down
	Inheriated attribute 1/cards, 2/decision (double down/surrender). 3/hit_hold) 4/ score 
	Method:  1/Show card()_ 2/ decision(): double down/surrender , 3/bet(), 4/hit_hold()
	Inheriated Method: 1/ take_card  2/ score_cal
	"""
	balance=5000
	bet_amount=0
	double_down='NA'
	surrender='#'
	def __init__(self):
		pass

	def show_card(self):
		u= self.cards
		u.pop(0)
		print(f"Your cards are {u}")
		print(f"and your score is {self.score}")

	def decision(self):

		while turn <= 2 and self.double_down != 'Yes' :		 #surrender
			if dealer.cards[1]=='A': 
				u=input("Do you want to surrender ?. This mean you give up your cards and lose half of your bet amount \n")
				try:
					u.capitalize() == 'Yes' or u.capitalize() == "No"
				except:
					print("This is not a valid input. Please try again") 
				else:
					if  u.capitalize() == 'Yes':
						self.surrender="Yes"
						break
					elif u.capitalize() == "No":
						break
					else: 
						print("You have only 2 choice: Yes and No. Please make the choice once again")
						continue			

		while turn <= 2:		 #double down		
			if self.double_down != 'Yes': 
				u=input("Do you want to double down ?. This mean you double your bet amount. Big risk big return, man :D \n")
				try:
					u.capitalize() == 'Yes' or u.capitalize() == "No"
				except:
					print("This is not a valid input. Please try again") 
				else:
					if  u.capitalize() == 'Yes':
						self.double_down='Yes'
						break
					elif u.capitalize() == "No":
						break
					else: 
						print("You have only 2 choice: Yes and No. Please make the choice once again")
						continue			

	def bet(self,dealer_balance):
		while True:
			try:
				bet = int(input("How much are you gonna bet on your winning ? \n:"))
			except:
				print("Hey man, that not seem to be an integer (which is a positive round number). \n Please try again")
				continue
			else:
				if bet >0 and bet <= self.balance and bet <= dealer_balance: #need to check to dealer.balance
					self.bet_amount == bet
					break
				elif bet <= 0:
					print("Aw, this number is too small. Please try again")
					continue
				elif bet > self.balance:
					print("Aw, this number is larger than your current balance. Please try a smaller number")
					continue
				elif bet > dealer_balance:
					print("Aw, this number is larger than Dealer current balance. Please try a smaller number")
					continue
				else:
					break

	def hit_hold():
		if self.score < 17:
			print(f"Your score is currently {self.score}, lowew than 17. You have to hit another card")
			self.hit_hold='Hit'
		if self.score >= 21:
			print(f"Your score is currently {self.score}, higher than 20. You are not allow to hit anymore")
		while self.score >= 17 and self.score < 21 :		 #Loop for input
			u=input("Do you want to keep hit another card or hold it ? \n")
			try:
				u.capitalize() == 'Hit' or u.capitalize() == "Hold"
			except:
				print("This is not a valid input. Please try again") 
			else:
				if  u.capitalize() == 'Hit':
					self.hit_hold='Hit'
					break
				elif u.capitalize() == "Hold":
					self.hit_hold="Hold"      
					break
				else: 
					print("You have only 2 choice: Hit and Hold. Please make the choice once again")
					continue			


		
