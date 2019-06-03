import time
start_time = time.time()

# def fib(number):
#     if(number == 0 or number == 1):
#         return 1
#     else:
#         return fib(number-1)+fib(number-2)
# fib_sum = 0
# i = 0
# while(fib_sum < 4000000):
#     temp = fib(i)
#     if(temp % 2 == 0):
#         fib_sum += temp
#     i += 1

fib1 = 1
fib2 = 1
result = 0
summed = 0
 
while (result < 4000000):
    if ((result % 2) == 0):
        summed += result
 
    result = fib1 + fib2
    fib2 = fib1
    fib1 = result

print(summed,"--- %s seconds ---" % (time.time() - start_time))
