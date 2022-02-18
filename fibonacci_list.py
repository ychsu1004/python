def calc_fib(x):
    
    fib_list = list()
    
    if x == 0:
        fib_list.append(0)
        return fib_list
    elif x == 1:
        fib_list.append(0)
        fib_list.append(1)
        return fib_list
    else:
        fib_list.append(0)
        fib_list.append(1)
         
    for i in range(2, x): 
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
        
    return fib_list

fib = int(input("input a number:"))
lists = calc_fib(fib)
print(lists)