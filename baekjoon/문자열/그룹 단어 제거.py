
tc = int(input())
count = tc

for k in range(tc) :
    word = input()
    for j in range(0, len(word)-1) :
        if (word[j] == word[j+1]) :
            pass
        elif word[j] in word[j+1:] :
            count -= 1
            break 
    
print(count)