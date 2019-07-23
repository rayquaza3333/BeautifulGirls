class Casino():
	cards=[]
	score=0
	balance=0
	def __init__(self):
		pass
	def score_cal(self):
		"""
		Các giá trị có thể gán cho self.score:
			1/ Điểm
			2/ AA Black Jack
			3/ Black Jack
		"""
		
		for i in range(0,len(self.cards)): ## Tổng điểm khi chưa tính các quân Ace			  
			if type(self.cards[i])==int:
				self.score += self.cards[i]
			elif type(self.cards[i])==str:
				if self.cards[i] !='A':
					self.score += 10

		while len(self.cards)==2:
			if self.cards.count('A')==2: #Luot dau tien, 2 quan bai. AA >> AA Black Jack
				self.score ='AA Black Jack'
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

class Player():
	balance=5000
	bet_amount= 0 
	def __init__(self):
		pass

	def bet(self):
		while True:
			try:
				amount=int(input("How much are you willing to bet? Please input a number: \n"))
			except:
				print("Oh, this is not a number, please input again")
				continue
			else:
				print("OK, I got your bet")
				break
		self.bet_amount = amount
		




import unittest
class test1(unittest.TestCase):
	def test1(self):
		a=Player()
		a.bet()
		self.assertEqual(a.bet_amount,20)
if __name__ == "__main__":
	unittest.main()