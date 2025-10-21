#def occur(arr):
 #   uni=set()
 #   for num in arr:
 #       if num not in uni:
  #          count=arr.count(num)
  #          print(f" {num} : {count}")
  #          uni.add(num)
#print(occur([4,2,3,2,3,4,4,5,3,4]))
def occur(arr):
    freq={}
   
    for num in arr:
        if num in freq:
             freq[num]+=1
        else:
            freq[num]=1
    return freq
print(occur([4,2,3,2,3,4,4,5,3,4]))

                