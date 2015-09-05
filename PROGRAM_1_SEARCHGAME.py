user_in = 'y'
name = input("Hello, what is your name?\n")
print("Hello "+name+", let's play a game\nThink of any integer between 1 and 100 inclusive, i will try to guess it")
while(user_in == 'y'):
	flag = 1; itr = 0						##ITR IS USED TO COUNT NUMBER OF TRIES AND FLAG IS JUST USED AS A KEY TO SWITCH TO LOGIC BASED ON USER INPUT
	low = 0; high = 100; mid = int((low + high)/2);
	while(flag):
		user_in = input("Is it "+str(mid)+"?y/n? ")
		if(user_in == 'y'):
			print("Yippee!!! I got it in "+str(itr + 1)+" tries")
			flag = 0
			user_in = input("Do you want to play more? y/n? ")
		elif (user_in == 'n'):
			user_in = input("Is it greater than "+str(mid)+"?y/n? ")
			if (user_in == 'y'):
				if(low < 98): 				##LOGIC USED TO TAKE CARE OF 100 IF DESIRED BY GAMER
					low = mid
					mid = int((low + high)/2)
					flag = 1
				else:
					mid = 100
			elif (user_in == 'n'):
				high = mid
				mid = int((low + high)/2)
				flag = 1
		itr = itr + 1
else:
	print("Bye.....Bye.....")