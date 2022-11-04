#Write your code below this line 👇
# aprime number is a number that can only be divided by 1 or itself, use modulus

def prime_checker(number):
    is_prime = True 
    for i in range(2,(number)):
        if number % i == 0:
            is_prime = False
    if is_prime == True
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
        
        



#It's a prime number.

#It's not a prime number.


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



