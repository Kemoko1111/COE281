#Checking Usernames
current_users = ['Dean','Boide','Kingsley','Chris','Sam']
new_users = ['Dean','Kingsley','kwesi','kwame','morris']
for user in new_users:
	if user in current_users:
		print(f"The person will need to enter a new username")
	else:
		print(f"The username is available")


#FizzBuzz
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
	    
    elif num % 3 == 0:
        print("Fizz")
	    
    elif num % 5 == 0:
        print("Buzz")
	    
    else:
        print(num)
