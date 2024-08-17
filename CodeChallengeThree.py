def change(list):
    list.sort()
    minimum = 1  
    for i in list:
        if i > minimum:
            break  
        minimum += i  
    return minimum

coins = [1, 5, 1, 1, 1, 10, 15, 20, 100]
print(change(coins))

