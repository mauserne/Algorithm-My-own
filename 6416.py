import sys

count = 0

while True:
    count += 1
    hash = {}
    treefailed = False
    print('count',count)
    while True:
        arr = input().split('  ')
        if arr == ['']:
            continue
        if arr == ['-1 -1']:
            sys.exit()
        print(arr)
        for i in arr:
            if i == '0 0':
                break
            print(i,'qpqpqp')
            u, v = i.split()

            if not u in hash:
                hash[u] = [False, []]
            if not v in hash:
                hash[v] = [True, []]
            else:
                if hash[v][0] == True:
                    # failed
                    treefailed = True
                else:
                    hash[v][0] = True
            
            hash[u][1].append(v)

        else:
            continue
        
        if treefailed:
            print('Case {cnt} is not a tree.'.format(cnt = count))
        else:
            print('Case {cnt} is a tree.'.format(cnt = count))
        break
