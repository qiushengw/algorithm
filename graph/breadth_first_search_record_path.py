


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
graph={
        "anuj" : ["bob"],
        "bob" : ["bob", "you", "peggy"],
        "you" : ["bob", "claire", "alice"],
        "claire" : ["you","claire","thom"],
        "thom" : ["clarie"],
        "peggy" : ["bob", "alice"],
        "alice" : ["you", "peggy"]
}

from collections import deque

def is_seller(name):
    return "alice" in name


def backtrace(parent, start, end):
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()

    return path

def bfs_with_path(graph, start, end):    
    parent ={}
    queue=[]
    queue.append(start)
    while queue:
        node = queue.pop(0)
        if end == node:
            backtrace(parent, start, end)

        for adjacent in graph[node]:
            if node not in queue:
                parent[adjacent]=node
                queue.append(adjacent)


def bfs(graph, start, end):
    search_queue = deque()
    search_queue += graph[start]
    searched=[]    

    while search_queue:
        print(search_queue) 
        person = search_queue.popleft();
        if person in searched:
            continue
        else:
            searched.append(person)

        if is_seller(person):
            print("find seller"+person)
            return person 
        else:
            search_queue+=graph[person]

    return NONE





result=bfs_with_path(graph, "anuj", "thom")
print(result)






