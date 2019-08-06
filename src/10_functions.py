# Write a function is_even that will return true if the passed-in number is even.

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False 

# Read a number from the keyboard

# Print out "Even!" if the number is even. Otherwise print "Odd"

def even_or_odd(n):
    if n % 2 == 0:
        return str("Even!")
    else:
        return str("Odd")

num = input("Enter a number: ")
num = int(num)
print(even_or_odd(num))

