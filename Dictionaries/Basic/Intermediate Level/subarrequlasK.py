'''
arr = [1, 2, 3]
k = 3

o/p: 

[1, 2]
[3] 

'''

def subarray_sum(arr, k):
    for i in range(len(arr)):
        total = 0
        
        for j in range(i, len(arr)):
            total += arr[j]
            
            if total == k:
                print(arr[i:j+1])


arr = [1, 2, 3]
k = 3

subarray_sum(arr, k)

# 

def subarray_sum(arr, k):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            total = 0 

            for x in range(i, j+1):
                total+= arr[x] 

            if total == k:
                print(arr[i: j+1]) 

                

arr = [1, 2, 3] 
k =3 

subarray_sum(arr, k) 


#
def subarray_sum(arr, k):
    prefix_sum = 0
    
    # stores prefix_sum : list of indices
    d = {0: [-1]}

    for i in range(len(arr)):
        prefix_sum += arr[i]

        target = prefix_sum - k

        if target in d:
            for start in d[target]:
                print(arr[start + 1 : i + 1])

        if prefix_sum in d:
            d[prefix_sum].append(i)
        else:
            d[prefix_sum] = [i]


arr = [1, 2, 3]
k = 3

subarray_sum(arr, k)




