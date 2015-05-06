 
a=[i for i in range(0,1001)]
b=int(input("请输入要查找的数这个数应该在0-1000之间:")) 
low = 0   
high = len(a)   
while(low <= high): 
    mid = (low + high)//2  
    midval = a[mid]
    if midval < b:
          low = mid + 1   
    elif midval > b:
         high = mid - 1  
    else:
        print(mid)
        break
    
    	

    
    
        
