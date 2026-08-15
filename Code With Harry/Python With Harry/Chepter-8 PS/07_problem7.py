# Strip means Remove Word From Exsting String Using Strip() Function.
# Remove Word in Exstin String in List

def rem(l,word):
    
    n=[]
    for item in l:
        if not(item == word):
            n.append(item.strip(word))

    return n

l = ["Vaibhav","Shiv","Parvati","av"]

word = input("Enter Word For Removing String in List:")

rem = rem(l,word)

print("Remove Word is:",rem)