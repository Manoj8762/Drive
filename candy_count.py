def candy_count(prices):
    count=0
    m=20
    prices.sort()
    print(prices)
        
    for price in prices:
        if price%5==0:
            count+=1
        elif m>=price:
           count+=1
           m=m-price
    return count


print(candy_count([5,10,12,15,6,7]))
            