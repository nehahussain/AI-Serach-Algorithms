with open('E:/6th Semester/AI/K173628-A1/ff.txt','r') as f:
    matrix = [[int(num) for num in line.split(',')] for line in f]
    

with open('E:/6th Semester/AI/K173628-A1/heuristics.txt','r') as h:
    heu = [[int(num) for num in line.split(',')] for line in h]

rows=len(matrix)
cols=len(matrix[0])

def alp(x):
    dict ={
        0:"A",
        1:"B",
        2:"C",
        3:"D",
        4:"E",
        5:"F",
        6:"G",
        7:"H",
        8:"I",
        9:"L",
        10:"M",
        11:"N",
        12:"O",
        13:"P",
        14:"R",
        15:"S",
        16:"T",
        17:"U",
        18:"V",
        19:"Z",
    }
    return(dict[x])

def returnalpha(p):
    dict ={
        0:"A",
        1:"B",
        2:"C",
        3:"D",
        4:"E",
        5:"F",
        6:"G",
        7:"H",
        8:"I",
        9:"L",
        10:"M",
        11:"N",
        12:"O",
        13:"P",
        14:"R",
        15:"S",
        16:"T",
        17:"U",
        18:"V",
        19:"Z",
    }
    pp=[]
    for rr in range(len(p)):
        pp.append(dict[p[rr]])
    return pp

def takeSecond(elem):
    return elem[1]


def returncost(pp,ss,gg):
    pathh=[gg]
    while gg!=ss:
        gg=pp[gg]
        pathh.insert(0,gg)
    costt=0
    for t in range(len(pathh)):
        try:
            costt+=matrix[pathh[t]][pathh[t+1]]
        except:
            pass
    
    return costt

def calculatepathcost(p):
    cost=0
    for i in range(len(p)):
        try:
            cost+=matrix[p[i]][p[i+1]]
        except:
            pass
    
    print("Path cost : ",cost)
    return cost

def printpath(p,s,g):
    k=0
    src=s
    gl=g
    path=[g]
    while g!=s:
        g=p[g]
        path.insert(0,g)
    print("Path from ",alp(src)," to ",alp(gl),"    : ",returnalpha(path))
    k=calculatepathcost(path)
    return k


def bfs(source,goal):
    bfscost=0
    parent = {}
    visited = []
    queue = []
    flag=0
    queue.append(source)
    visited.append(source)
    while queue:
        i=queue[0]
        x=0
        for x in range (cols):
            if matrix[i][x] != 0 and x not in visited:  
                visited.append(x)
                queue.append(x)
                bfscost+=matrix[i][x]
                parent[x]=i

            if goal in visited:
                flag=1
                break

        if flag==1:
            break    

        queue.pop(0)

    print("********** Breadth First Search **********")
    print ("Path traversed : ",returnalpha(visited))
    global bp
    bp=printpath(parent,source,goal)

def iddfs(source,goal):
    print("********** Iterative Deepening Dept First Search **********")
    parent = {}
    visited = []
    stack = []
    flag=0
    i=source
    level=0
    while flag!=1:
        flag=0
        stack.clear()
        visited.clear()
        parent.clear()
        stack.append(source)
        visited.append(source)
        while stack:
            x=0
            check=0
            if level==0:
                break

            for x in range (cols):
                if matrix[i][x] != 0 and x not in visited:  
                    check=1
                    visited.append(x)
                    stack.append(x)
                    parent[x]=i
                    break

                if goal in visited:
                    flag=1
                    break

            if flag==1:
                break    

            i=stack[-1]
            # print(stack)
            if check==0 or (len(stack)-1)==level:
                check=0
                stack.pop()
                try:
                    i=stack[-1]
                except:
                    pass

        level=level+1
        print ("Path traversed level ",level-1," : ",returnalpha(visited))
    global iddfsp
    iddfsp=printpath(parent,source,goal)

def UniformCostSearch(source,goal):
    print("********** Uniform Cost Search **********")
    ucs=[]
    parent = {}
    visited = []
    queue = []
    queue.append((source,0))
    visited.append(source)
    while queue:
        goalcost=0
        i=queue[0][0]
        x=0
        bfscost=0
        ucs.append(i)
        for x in range (cols):
            if matrix[i][x] != 0 and x not in visited:
                visited.append(x)
                parent[x]=i
                bfscost=returncost(parent,source,x)
                queue.append((x,bfscost))
            if goal in visited:
                if goalcost>=bfscost:
                    goalcost=bfscost
                    # ucs.pop()
                    # ucs.append(x)
                    queue.pop()
                    visited.pop()
                break
        
        queue.sort(key=takeSecond)    
        queue.pop(0)
    print ("Path traversed : ",returnalpha(ucs))
    global upp
    upp=printpath(parent,source,goal)


def GreedyBFS(source,goal):
    print("********** Greedy Best First Search **********")
    ucs=[]
    flag=0
    parent = {}
    visited = []
    queue = []
    queue.append((source,heu[source]))
    visited.append(source)
    while queue:
        i=queue[0][0]
        x=0
        ucs.append(i)
        for x in range (cols):
            if matrix[i][x] != 0 and x not in visited:
                visited.append(x)
                parent[x]=i
                queue.append((x,heu[x]))
            if goal in visited:
                flag=1
                break
        
        if flag==1:
            break

        queue.pop(0)
        queue.sort(key=takeSecond)    
    # print ("Path traversed : ",ucs)
    global gp
    gp=printpath(parent,source,goal)

print("\n")
bfs(0,1)
print("\n")
iddfs(0,1)
print("\n")
UniformCostSearch(0,1)
print("\n")
GreedyBFS(0,1)
print("\n")
print("******** Path Cost in Ascending order obtained from : ")
numbers = [upp,bp,iddfsp,gp]
numbers.sort()
for r in range(len(numbers)):
    if (numbers[r]==upp):
        print("Uniform Cost Search : ",numbers[r])
        upp="-"
    elif (numbers[r]==bp):
        print("Breadth First Search : ",numbers[r])
        bp="-"
    elif (numbers[r]==iddfsp):
        print("Ierative Deepening Depth first Search : ",numbers[r])
        iddfsp="-"
    elif (numbers[r]==gp):
        print("Greedy Best First Search : ",numbers[r])
        gp="-"