def check_start_isgoal(start,end):
    if start==end:
        print("solution found",start_state)
        exit(0)

def visited_node_removal(listing):
    for i in listing:               
        if i[0]==queue_top_element[1]:
            listing.remove(i)
            break

def goal_check(lisitng,end_state,BFS_Queue):
    #goal state         
    for i in listing:
        if i[0] == end_state:                     
            print("Solution Found!",i[0])
            exit(0)
        print(i[0])
        BFS_Queue.append(i)
    print("\n")


def index_find_tile(num):           #to find the position of 0 on board
    for i in num:
        if num[i]==0:
            return i    
        else:
            continue
    return -1

def swap(strr, a, b):           #to swap for 2 positions
    strr2=strr.copy()
    temp = strr2[a]
    strr2[a] = strr2[b]
    strr2[b] = temp
    
    return strr2

def make_move(num):     #9 ki array making moves
    ind = index
    operate = num
    moved_list = []
    
    if ind==0:
        final = swap(operate, ind, 1)           #0 can go to 1 or 3
        moved_list.append([final,num])
        
        final = swap(operate, ind, 3)
        moved_list.append([final,num])
        
    elif ind==1:
        final = swap(operate, ind, 0)       #0 can go to 0, 2 or 4
        moved_list.append([final,num])
        
        final = swap(operate, ind, 2)
        moved_list.append([final,num])
        
        final = swap(operate, ind, 4)
        moved_list.append([final,num])
    
    elif ind==2:
        final = swap(operate, ind, 1)           #0 can go to 1 or 5
        moved_list.append([final,num])
        
        final = swap(operate, ind, 5)
        moved_list.append([final,num])
        
    elif ind==3:
        final = swap(operate, ind, 0)           #0 can go to 0, 4, or 6
        moved_list.append([final,num])
        
        final = swap(operate, ind, 4)
        moved_list.append([final,num])
        
        final = swap(operate, ind, 6)
        moved_list.append([final,num])
        
    elif ind==4:
        final = swap(operate, ind, 1)           #0 can go to 1, 3, 5 or 7
        moved_list.append([final,num])
        
        final = swap(operate, ind, 3)
        moved_list.append([final,num])
        
        final = swap(operate, ind, 5)
        moved_list.append([final,num])
        
        final = swap(operate, ind, 7)
        moved_list.append([final,num])
    
    elif ind==5:
        final = swap(operate, ind, 2)           #0 can go to 2, 4, 8
        moved_list.append([final,num])
        
        final = swap(operate, ind, 4)
        moved_list.append([final,num])
        
        final = swap(operate, ind, 8)
        moved_list.append([final,num])
    
    elif ind==6:
        final = swap(operate, ind, 3)           #0 can go to 3 or 7
        moved_list.append([final,num])
        
        final = swap(operate, ind, 7)
        moved_list.append([final,num])
        
    
    elif ind==7:
        final = swap(operate, ind, 4)               #0 can go to 4, 6, 8
        moved_list.append([final,num])
        
        final = swap(operate, ind, 6)
        moved_list.append([final,num])
        
        final = swap(operate, ind, 8)
        moved_list.append([final,num])
        
    
    elif ind==8:
        final = swap(operate, ind, 5)           #0 can go to 5 or 7
        moved_list.append([final,num])
        
        final = swap(operate, ind, 7)
        moved_list.append([final,num])

    return moved_list
######################################code start hu######################################
#array start state
start_state=[2,3,6,5,0,8,1,4,7]
#array end state
end_state=[1,2,3,4,5,6,7,8,0]

##########checking if the given states are already equal#########
check_start_isgoal(start_state,end_state)
#initial parent load
intial_parent_load=[1,1,1,1,1,1,1,1,1]
#empty queue for BFS
BFS_Queue = []
# add root node 
BFS_Queue.append([start_state,intial_parent_load])

#for comple queue
while BFS_Queue:
    #Dequeue from top
    queue_top_element = BFS_Queue.pop(0)                    
    print(queue_top_element)
    #find index of empty location
    index=index_find_tile(queue_top_element[0])
    if index==-1:
        print("No empty tile found")
        exit(0)
    #moves according to index 
    listing = make_move(queue_top_element[0])       

    #remove visited node like parent copy
    visited_node_removal(listing)
    #goal state else building queue
    goal_check(listing,end_state,BFS_Queue)
    