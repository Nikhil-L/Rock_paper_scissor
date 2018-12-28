import sys
import random
 
print("0.Terminate\n1.Rock\n2.Scissor\n3.Paper\n")
choice = input("Enter your choice : ")
choice = int(choice)
print("\n")
while(input):
	if(choice == 0):
		print("You terminated the game!!")
		sys.exit()
	
	else:
		generate = random.randint(1,3)
		if(generate == 1):
			print("Computer got Rock\n")
			
		elif(generate == 2):
			print("Computer got Scissor\n")
			
		else:
			print("Computer got Paper\n")
			
		if(choice == 1):
			print("YOu got Rock\n")
			
		elif(choice == 2):
			print("YOu got Scissor\n")
			
		else:
			print("You got Paper\n")
			
		
	if((generate == 1 and choice == 2)or(generate == 2 and choice == 3)or(generate == 3 and choice == 1)):
		print("Computer won!!!\n")
		
	if(choice == generate):
		print("Draw\n")
		
	if((generate == 2 and choice == 1)or(generate == 3 and choice == 2)or(generate == 1 and choice == 3)):
		print("You Won!!!\n")
		
	choice = input("\n\nEnter your choice : ")
	choice = int(choice) 
		
			
		

