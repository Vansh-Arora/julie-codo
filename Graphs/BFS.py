def BFShelper(adjList,V):
    visi = [0 for i in range(V)]
    q = [0]
    top = 0
    end = 0
    visi[0] = 1
    BFS(adjList,V,visi,q,top,end)
    for i in range(1,V):
        if visi[i] == 0:
            q.append(i)
            end += 1
    return q
def BFS(adjList,v,visi,q,top,end):
    

    while top <= end:
        cur = q[top]
        top += 1
        for i in adjList[cur]:
            if visi[i] == 0:
                q.append(i)
                visi[i] = 1
                end += 1

adjList = [[1, 2], [0, 3, 4, 5, 6], [0, 6], [1], [1], [1], [1, 2], [8, 9], [7], [7], [11], [10]]
print(BFShelper(adjList,12))