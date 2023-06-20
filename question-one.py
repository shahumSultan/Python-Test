#Task (If-Else with Function)
#Given an integer, , perform the following conditional actions:
#   - if n is odd, print "Odd"
#   - if n is even and in the inclusive range of 2 to 5, print "Even and in between range 2 to 5"
#   - if n is even and in the inclusive range of 6 to 20, print "Even and in between range 6 to 20"
#   - if n is even is greater than 20, print "Even and greater than 20"

#Input Format => a positive integer 'n'
#Constraints => 1 ­≤ n ≤ 100

######code below this line######
def NumberCheker(n):
    if ((n%2) == 0) and (n >= 2 and n <= 5):
        print("Even and in between range 2 to 5")
    elif ((n%2) == 0) and (n >= 6 and n <= 20):
        print("Even and in between range 6 to 20")
    elif ((n%2) == 0) and (n > 20):
        print("Even and greater than 20")
    else:
        print("Odd")
    

if __name__ == '__main__':
    n = int(input().strip())
    NumberCheker(n)