def sumSplit(left,right=[],difference=0):
    sumLeft,sumRight = sum(left),sum(right)

    if sumLeft<sumRight or len(left)<len(right): return

    if sumLeft-sumRight == difference:
        return left, right, difference
    for i,value in enumerate(left):
        solution = sumSplit(left[:i]+left[i+1:],right+[value], difference)
        if solution: return solution

    if right or difference > 0: return 

    for targetDiff in range(1, sumLeft-min(left)+1):
        solution = sumSplit(left, right, targetDiff)
        if solution: return solution 

num_of_rods = int(input(""))

length = input("")
arr_length = list(map(int,length.split(sep=" ")))
left,right,difference = sumSplit(arr_length)
if difference ==0:
  print(sum(left))
else:
  print(0)
#   Time out error :(
