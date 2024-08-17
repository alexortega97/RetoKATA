def toOrder(lst):
    upperLimit = int(str(4) * 2)
    squareArray = [x**2 for x in lst]
    numberFilter = [x for x in squareArray if 0 <= x <= upperLimit]
    
    n = len(numberFilter)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if numberFilter[j] < numberFilter[min_idx]:
                min_idx = j
        numberFilter[i], numberFilter[min_idx] = numberFilter[min_idx], numberFilter[i]
    print(numberFilter)
    

inputArray = [-4,5,1,3,2,0,-6,7,8,2]

toOrder(inputArray)

