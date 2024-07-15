start = 11
end = 75
print("Prime numbers between 11 and 75 are:")
for(i in range(start, end + 1)):
    if i > 1:
        for(j in range(2, i)):
            if(i%j==0):
                break
            else:
                print(i)