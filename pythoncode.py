#number guessing game
'''let's play'''
import random
secretnumber = random.randint(1,100)
guess = 0
tries = 0
n = 6
#this is to keep track of the current guess
indexer = {0:'first',1:'second',2:'third',3:'fourth',4:'fifth',5:'sixth'}
'''few lines of introduction for the gamer'''
print("""Welcome to the number guessing games. you will going to have six tries,
	in which you have to guess the number. 
	so let's start the games.
	all the best!!""")
#now we are going to enter in a game loop
while guess != secretnumber and tries <n:
	 guess = int(input("what is your " + indexer[tries]+ " guess?\n"))
	 if guess > secretnumber and tries < n-1:
	 	print("your guess number is too high.")
	 elif guess < secretnumber and tries < n-1:
	 	print("your guess number is to low.")
tries = tries + 1
#now we are going to write a loop in which we are goint to take a conditon in which we have guess a number weather is right or wrong.
if guess == secretnumber:
	print("""wow!! you guess is correct. holy cow!!""")
elif guess != secretnumber and tries == n:
	 		print("""better luck next time. You are out of tries. the secret number was """,secretnumber)
