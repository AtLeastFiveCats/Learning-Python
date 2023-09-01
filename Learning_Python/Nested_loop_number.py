numbers = [1, 1, 1, 4]

for x_count in (numbers): #x_count changes the numbers from a list to an integer
    output = '' #output is an empty variable, everytime the loop interates from the top it resets itself.
    for count in range(x_count): #count is only here for a nested loop
        output += 'x' #output will add x to itself every time the loop repeats
    print(output) 