'''
Find pairs whose sum equals to n 



'''

lst = [1, 2, 3, 4, 5, 6, 7]
n = 7 

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] + lst[j] == n and i<j:
            pair = lst[i], lst[j] 
            print(pair) 


#

def get_unique_list(lst, n):

    unique_pairs=set() 
    
    for i in range(len(lst)):
        num1 = lst[i]
        num2 = n-lst[i] 
        rem_list = lst[i+1: ] 
        if num2 in rem_list:
            pair = (num1, num2) 
            pair = tuple(sorted(pair)) 
            unique_pairs.add(pair) 
    return unique_pairs  



lst = [5, 3, 7, 9, 5]
n = 12 
res = get_unique_list(lst, n)

for pair in res:
    print(pair)
    


