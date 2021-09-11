def dynamicArray(n, queries):
    lastAnswer = 0
    arr = [[]for i in range(n)]
    lastArr = list()
    
    for query in queries:
        idx = ((query[1] ^ lastAnswer) % n)
        if query[0] == 1:
            arr[idx].append(query[2])
        else:
            lastAnswer = arr[idx][query[2] % len(arr[idx])] 
            arr.append(lastAnswer)
            lastArr.append(lastAnswer)
    return lastArr
