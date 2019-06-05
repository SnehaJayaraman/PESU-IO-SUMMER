def binarysearch(list,low,high,n):
    if low>high:
        return -1
    else:
        mid=(low+high)//2
        if list[mid]==n:
            return mid
        elif list[mid] >n:
            return binarysearch(list,low,mid-1,n)
        else:
            return binarysearch(list,mid+1,high,n)





value=int(input("Enter the length of the list:"))
list=[]
for k in range(value):
    ele=int(input("Enter element:"))
    list.append(ele)
list.sort()
n=int(input("Enter the number to be searched:"))
res = binarysearch(list,0,len(list)-1,n)
if res==-1:
    print("Element",n,"not found")
else:
    print("Element",n,"found at position",res+1)
