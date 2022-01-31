# library for argument parsing in python
import argparse
from DepthFirstSearch import Vertex,Graph


def getdata(edges_filename):
    edges_file = open(edges_filename)
    start_List=[]
    end_List=[]
    track_List=[]
    for line in edges_file:
        start,end,point=line.split(":")
        start=str(start)
        end=str(end)
        point=int(point)
        start_List.append(start)
        end_List.append(end)
        track_List.append(point)
    return start_List,end_List,track_List

def get_card_data(cards_filename):
    edges_file = open(cards_filename)
    start_List=[]
    end_List=[]
    track_List=[]

    for line in edges_file:
        start,end,point=line.split(":")
        start=str(start)
        end=str(end)
        point=int(point)
        start_List.append(start)
        end_List.append(end)
        track_List.append(point)
    return start_List,end_List,track_List


def cal_point(track_List):
    total_point=0
    for i in range (len(track_List)):
        if track_List[i]==1:
            total_point+=1
        if track_List[i]==2:
            total_point+=2
        if track_List[i]==3:
            total_point+=4
        if track_List[i]==4:
            total_point+=7
        if track_List[i]==5:
            total_point+=10
        if track_List[i]==6:
            total_point+=15
    return total_point


def DFS(map_dic, start,end,key_list):
# check if start_point =end_point
    if start ==end:
        return True 
# check if start_point in the map
    if start in map_dic.keys():
        # keep track the input's index and make its value =true,
        # means we already visited this point 
        sindex=key_list.index(start)
        key_list[sindex]=True
# check every neighbor of start_point
        for i in map_dic[start]:
# if it is not visited ,do 
            if i in key_list and i !=True:
# if end is found in its neighbor location, return true 
                if i == end:
                    return True 
# if it is not, do dfs in its neighbor
                found=DFS(map_dic,i,end,key_list)
                # if found ,then return true 
                if found ==True:
                    return True 
        # not found return false 
        return False 
    
    return False 

def cal_card_score(card_start,card_end,point_list,total_point,map_dic,key_list):
    
    for i in range (len(card_start)):
    # reset key_list every iteration
        key_list=list(map_dic.keys())
        check=DFS(map_dic,card_start[i],card_end[i],key_list)
        if check ==True:
            
            total_point= total_point+point_list[i]

        else:
            total_point= total_point-point_list[i]

    return total_point
        

        


                

# main function, code is executed here if the script is run
if __name__ == '__main__':
    # load argument parser
    parser = argparse.ArgumentParser()
    # arguments for data sources
    parser.add_argument('-e', '--edges', type=str, default='edge.txt', help='Name of file that contains edges')
    parser.add_argument('-c', '--cards', type=str, default='card.txt', help='Name of file that contains cards')
    # parse arguments from command line
    args = parser.parse_args()
    
    # load edges filename into variable
    edges_filename = args.edges

    # load card filename into variable
    cards_filename = args.cards
    

    start_List,end_List,track_List=getdata(edges_filename)
    
    card_start,card_end,point_list=get_card_data(cards_filename)

    total_point=cal_point(track_List)
    # print(card_start)



    
    t_list=start_List+end_List
    a_list=[]
    for i in (t_list):
        if i  not in  a_list:
            a_list.append(i)
    
    g = Graph()
    for i in (a_list):
        g.add_vertex(Vertex(i))
    for i in range(len(start_List)):
        g.add_edge(start_List[i], end_List[i])

    map_dic=g.get_dic()
    key_list=list(map_dic.keys())

    # print(key_list)
    
    
    # if DFS(map_dic,'Winnipeg','Little Rock',key_list):
    #     print('yes')
    # else:
    #     print('no')




    final_points= cal_card_score (card_start,card_end,point_list,total_point,map_dic,key_list)
    print(final_points)
    

    
    # g.print_graph()
 
    





    

    

