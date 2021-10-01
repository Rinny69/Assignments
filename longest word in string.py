def longestWordLength(string):  
    length = 0   
    w = ''       
    for word in string.split(): 
        if(len(word) > length): 
            length = len(word) 
            w = word
    return (length, w)  
  
string = input("Enter the string: ")
l, w = longestWordLength(string)
print("Longest word is ", w, " and its length is ", l)


