# List Comprehensions

myList = [1,5,3,8,9]

#squareList = []
# for item in myList:
#     squareList.append(item*item)

squareList = [item*item for item in myList]

print(squareList)