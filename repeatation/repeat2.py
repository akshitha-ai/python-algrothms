def containsDuplicate(nums):
    seen=set()
    for num in nums:
        if num in seen:
            return True
         seen.add(num)
         return False
        
        arr1=[1,2,3,4]
        arr2=[1,2,3,1,5]
        arr3=[1,2,3,4,1,5,2,3,4,7,5]

        print(containsDuplicate(arr1))
        print(containsDuplicate(arr2))
        print(containsDuplicate(arr3))
        
        
        