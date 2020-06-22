# Uses python3
# Week 2, 1 Fibonacci Number

def calc_fib(n):
    if (n <= 1):
        return n
    elif (n <= 3):
        return n-1
    return 3*calc_fib(n - 3) + 2*calc_fib(n - 4)

#def Tes (i):
    #import time
    #start_time = time.time()
n = int(input())#i
    #print (i)
print (calc_fib(n))
    #print("--- %s seconds ---" % (time.time() - start_time))

#for i in range (1, 46):
    #Tes (i)
