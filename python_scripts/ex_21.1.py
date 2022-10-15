import time

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib(n-1) + fib(n-2)

fib_num = {}
def fibm(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if n not in fib_num:
        fib_num[n] = fibm(n-1) + fibm(n-2)
    return fib_num[n]

# print(fib(47))
# start = time.time()
# print(fibm(470))
# end = time.time()
# print(end - start)

def sum_of_n(n):
    if n == 1:
        return 1
    return n + sum_of_n(n-1)

# print(sum_of_n(40))

def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n-1)

# print(power(2, 10))

def recursive_reverse(ls):
    if len(ls) == 0:
        return []

    return [ls[-1]] + recursive_reverse(ls[:-1])

def recursive_reverse2(ls):
    if len(ls) == 0:
        return []

    ls1 = []
    ls1.append(ls.pop())
    return ls1 + recursive_reverse2(ls)

my_list = [1,2,3,4]

print(recursive_reverse2(my_list))
print(my_list)



