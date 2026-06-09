#  Check subsequence or not 

full_string = "abcde"
half_string = "abc" 

new=""

for i in range(len(full_string)):
    if full_string[i] in half_string:
        new+=full_string[i]
if new==half_string:
    print("Yes")
else:
    print("No")

    
####
full_string=input()
subsequence=input()

subseq_index=0   
subseq_len=len(subsequence)

for char in full_string:
    if char==subsequence[subseq_index]:
        subseq_index+=1  
        if subseq_index==subseq_len:
            break  
if subseq_index==subseq_len:
    print("Yes")
else:
    print("No") 



