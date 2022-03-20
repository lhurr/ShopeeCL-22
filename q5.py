from itertools import combinations
num_of_rods = int(input(""))

length = input("")
import numpy as np 
def remover(first,second):
 # second = second[:]
  first = first[:]
  for element in second:
    first.remove(element)
  return first

arr_length =list(map( int,  length.split(sep=" ")))
print(arr_length)
largest =  []

#nparrlen = np.array(arr_length )
for i in range( 1 , len(arr_length) +1):
    for combination in combinations(arr_length  , i):
        print('combination' ,combination )
        complement = remover(arr_length , combination)
        print('complement' , complement )
        print('sum complement' , sum(complement) )
        print("sum combination " , sum(combination))
        if sum(complement)  == sum(combination):
            print('here')
            largest.append(sum(complement))
        print()

print(largest)
if len(largest) == 0:
    print(0)
else:
    print(max(largest))
