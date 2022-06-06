"""_Using continue in a loop_:
        0. Use the continue statement to return to the beginning of the loop.
        1. This should be based on the result of a conditional test.
        2. Useful when not trying to break out of loop entirely without executing the code.
"""

#Consider a loop that counts from 1 to 10 but prints only odd numbers.
current_number = 0                  #Set current number to 0
while current_number < 10:          
    current_number += 1             #increment our current_number by 1
    if current_number % 2 == 0:     #check if divisible by 2
        continue                    #return to the beggining of the loop if statement is true
    
    print(current_number)
    
"""_Avoiding infinite loops_:
        0. Every programmer accidentally writes an infinite while loop.
        1. If stuck in an infinite loop, press CTRL-C or just close the terminal window.
        2. Try testing every while loop and make sure it stops when ypu expect it to.
"""