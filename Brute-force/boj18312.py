N, K = input().split()

result = 0
for i in range(int(N)+1):
    if i < 10:
        i = '0'+str(i)
    else:
        i = str(i)
    for j in range(60):
        if j < 10:
            j = '0'+str(j)
        else:
            j = str(j)
        for k in range(60):
            if k < 10:
                k = '0'+str(k)
            else:
                k = str(k)
                
            if K in i+j+k:
                result += 1

print(result)