
def unique_list(ls):
    result = []
    for n in ls:
        if n not in result:
            result.append(n)
    return result

my_list=[1,2,2,3,3,4,4,4,5,4,3,7,5,5,5,2,1,10]
print(unique_list(my_list))