def fibonacci(previous, current):
    box1 = current
    box2 = previous + current
    #return current, previous + current
    return box1, box2


def fibonacciRange(start, iterations):
    previousNumber = start
    actualNumber = previousNumber + 1
    print (previousNumber)
    print (actualNumber)
    for i in range(iterations):
        previousNumber, actualNumber = fibonacci(previousNumber, actualNumber)
        print (actualNumber)

        
fibonacciRange(100, 100)
