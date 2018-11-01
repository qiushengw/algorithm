


'''
use hashtable to save below links
 
         anuj    bob       you     claire  thom  peggy   alice
anuj        1       1       0       0       0       0       0        
bob         1       1       1       0       0       1       0
you         0       1       1       1       0       0       1
clarire     0       0       1       1       1       0       0
thom        0       0       0       1       1       0       0
peggy       0       1       0       0       0       1       1
alice       0       0       1       0       0       1       1


'''
graph={}
graph["anuj"] = ["bob"]
graph["bob"] = ["bob", "you", "peggy"]
graph["you"] = ["bob", "claire", "alice"]
graph["clarire"]=["you","claire","thom"]
graph["thom"]=["clarie"]
graph["peggy"]=["bob", "alice"]
graph["alice"]=["you", "peggy"]

from collections import deque
def bfs(graph, start, end):
    search_queue = deque()
    search_queue += graph[start]
    
    
    path=[start]
    
    while search_queue:
        person = search_queue.popleft();
        if person == end:
            

    queue=[]
    leve1list = graph[start]
    if end in leve1list:
        path.append(end)
    else:
        queue.append(leve1list)



