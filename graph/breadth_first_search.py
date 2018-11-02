


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


def is_seller(name):
    return "alice" in name



from collections import deque
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





result=bfs(graph, "anuj", "thom")






