import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(G):
    plt.figure(1)
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edge_color='r', arrows=False, arrowsize=20)
    plt.show()
    plt.clf()

def has_path(G, v1, v2):
    try:
        nx.shortest_path_length(G, v1, v2)
    except nx.NetworkXNoPath:
        return False
    return True

# топологии ------------------------------------------------
def init_Graph1():
    G = nx.Graph()
    for i in range(6):
        G.add_node(i)   
    #Граф Произвольный
    G.add_edge(0, 1)    
    G.add_edge(0, 2)
    G.add_edge(1, 2)    
    G.add_edge(1, 3)   
    G.add_edge(2, 4)
    G.add_edge(3, 4)
    G.add_edge(3, 5)
    G.add_edge(4, 5)
    # draw_graph(G)
    return G

def init_Point():
    G = nx.Graph()
    for i in range(2):
        G.add_node(i)
    #Граф Точка-Точка
    G.add_edge(0, 1)
    # draw_graph(G)
    return G
    
def init_Net():
    G = nx.Graph()
    for i in range(5):
        G.add_node(i)      
    #Граф типа Сеть
    G.add_edge(0, 1)   
    G.add_edge(0, 2)  
    G.add_edge(0, 3) 
    G.add_edge(0, 4) 
    G.add_edge(1, 2) 
    G.add_edge(1, 3)
    G.add_edge(1, 4)  
    G.add_edge(2, 3) 
    G.add_edge(2, 4) 
    G.add_edge(3, 4)
    # draw_graph(G)
    return G
       
def init_Star():
    G = nx.Graph()
    for i in range(7):
        G.add_node(i)
   #Граф типа "Звезда"
    G.add_edge(0, 6)   
    G.add_edge(1, 6)  
    G.add_edge(2, 6) 
    G.add_edge(3, 6) 
    G.add_edge(4, 6) 
    G.add_edge(5, 6)
    # draw_graph(G)
    return G
 
def init_Ring():
    G = nx.Graph()
    for i in range(4):
        G.add_node(i)
    #Граф типа "Кольцо"
    G.add_edge(0, 1)   
    G.add_edge(0, 3)  
    G.add_edge(1, 2) 
    G.add_edge(2, 3)
    # draw_graph(G)
    return G

def init_Tree():
    G = nx.Graph()
    for i in range(10):
        G.add_node(i)   
    #Граф типа "Дерево"
    G.add_edge(0, 1)   
    G.add_edge(1, 2)  
    G.add_edge(1, 3) 
    G.add_edge(2, 4) 
    G.add_edge(2, 5) 
    G.add_edge(2, 6)
    G.add_edge(3, 7)  
    G.add_edge(3, 8) 
    G.add_edge(3, 9)
    # draw_graph(G)
    return G
    
def init_Chain():
    G = nx.Graph()
    for i in range(4):
        G.add_node(i)
        
    #Граф типа "Цепь"
    G.add_edge(0, 1)   
    G.add_edge(1, 2)  
    G.add_edge(2, 3)
    # draw_graph(G)
    return G
    
def init_Hybrid():
    G = nx.Graph()
    for i in range(15):
        G.add_node(i)
    #Граф типа "Гибрид"
    G.add_edge(0, 1)   
    G.add_edge(0, 2)  
    G.add_edge(1, 2) 
    G.add_edge(0, 3) 
    G.add_edge(3, 4) 
    G.add_edge(3, 5)
    G.add_edge(3, 6)  
    G.add_edge(1, 7) 
    G.add_edge(7, 8)
    G.add_edge(7, 9) 
    G.add_edge(7, 10) 
    G.add_edge(2, 11)
    G.add_edge(11, 12)  
    G.add_edge(11, 13) 
    G.add_edge(11, 14)
    # draw_graph(G)
    return G

# ---------------------------------------------------------

def init_FullGraph():
    G = nx.MultiGraph()
    for i in range(6):
        G.add_node(i)
        
    #Граф типа Полный граф
    G.add_edge(0, 1)    
    G.add_edge(0, 2)
    G.add_edge(1, 2)    
    G.add_edge(1, 3)   
    G.add_edge(2, 3)
    G.add_edge(2, 4)
    G.add_edge(3, 4)
    G.add_edge(3, 5) 
    G.add_edge(4, 5)
    # G.add_edge(1, 3)
    G.add_edge(2, 2)
    # draw_graph(G)
    return G

def init_ShortGraph5():
    G = nx.MultiGraph()
    for i in range(6):
        G.add_node(i)
    #Граф связующее дерево
    G.add_edge(0, 1)   
    G.add_edge(1, 2)  
    G.add_edge(2, 3) 
    G.add_edge(3, 4) 
    G.add_edge(3, 5)
    # draw_graph(G)
    return G

def init_ShortGraph6():
    G = nx.MultiGraph()
    for i in range(6):
        G.add_node(i)
        
    #Граф связующее дерево
    G.add_edge(0, 1)   
    G.add_edge(1, 2)  
    G.add_edge(2, 3) 
    G.add_edge(3, 4) 
    G.add_edge(3, 5) 
    G.add_edge(4, 5) 
    # draw_graph(G)
    return G

def init_ShortGraph7():
    G = nx.MultiGraph()
    for i in range(6):
        G.add_node(i)
        
    #Граф связующее дерево
    G.add_edge(0, 1)   
    G.add_edge(1, 2)  
    G.add_edge(2, 3) 
    G.add_edge(2, 4)
    G.add_edge(3, 4) 
    G.add_edge(3, 5) 
    G.add_edge(4, 5) 
    # draw_graph(G)
    return G

def init_ShortGraph8():
    G = nx.MultiGraph()
    for i in range(6):
        G.add_node(i)
        
    #Граф связующее дерево
    G.add_edge(0, 1)   
    G.add_edge(1, 2)
    G.add_edge(1, 4)  
    G.add_edge(2, 3) 
    G.add_edge(2, 4)
    G.add_edge(3, 4) 
    G.add_edge(3, 5) 
    G.add_edge(4, 5) 
    # draw_graph(G)
    return G

def init_ShortGraph9():
    G = nx.MultiGraph()
    for i in range(6):
        G.add_node(i)
        
    #Граф связующее дерево
    G.add_edge(0, 1) 
    G.add_edge(0, 2)   
    G.add_edge(1, 2)
    G.add_edge(1, 4)  
    G.add_edge(2, 3) 
    G.add_edge(2, 4)
    G.add_edge(3, 4) 
    G.add_edge(3, 5) 
    G.add_edge(4, 5) 
    # draw_graph(G)
    return G

def init_ShortGraph10():
    G = nx.MultiGraph()
    for i in range(6):
        G.add_node(i)
        
    #Граф связующее дерево
    G.add_edge(0, 1) 
    G.add_edge(0, 2)   
    G.add_edge(1, 2)
    G.add_edge(1, 4)  
    G.add_edge(2, 3) 
    G.add_edge(2, 4)
    G.add_edge(3, 4) 
    G.add_edge(3, 5) 
    G.add_edge(4, 5) 
    G.add_edge(2, 2)
    # draw_graph(G)
    return G

def init_Graph2():
    G = nx.Graph()
    for i in range(21):
        G.add_node(i)   
    #Граф Произвольный
    G.add_edge(0, 1)    
    G.add_edge(0, 2)
    G.add_edge(0, 3)    
    G.add_edge(1, 5)   
    G.add_edge(2, 3)
    G.add_edge(2, 4)
    G.add_edge(3, 7)
    G.add_edge(4, 6)
    G.add_edge(5, 9)    
    G.add_edge(5, 8)
    G.add_edge(6, 14)    
    G.add_edge(6, 10)   
    G.add_edge(7, 10)
    G.add_edge(7, 8)
    G.add_edge(8, 9)
    G.add_edge(8, 11)    
    G.add_edge(9, 11)
    G.add_edge(9, 17)    
    G.add_edge(10, 13)   
    G.add_edge(11, 12)
    G.add_edge(12, 15)
    G.add_edge(12, 17)
    G.add_edge(9, 11)
    G.add_edge(9, 17)    
    G.add_edge(10, 13)   
    G.add_edge(11, 12)
    G.add_edge(12, 15)
    G.add_edge(12, 16)
    G.add_edge(13, 14)
    G.add_edge(14, 15)    
    G.add_edge(15, 16)   
    G.add_edge(16, 17)
    G.add_edge(16, 18)
    G.add_edge(17, 20)
    G.add_edge(18, 19)
    G.add_edge(19, 20)
    draw_graph(G)
    return G

def init_Graph3():
    G = nx.Graph()
    for i in range(14):
        G.add_node(i)   
    #Граф Произвольный
    G.add_edge(0, 1)    
    G.add_edge(0, 2)
    G.add_edge(0, 3)    
    G.add_edge(1, 5)   
    G.add_edge(2, 3)
    G.add_edge(2, 4)
    G.add_edge(3, 7)
    G.add_edge(4, 6)
    G.add_edge(5, 9)    
    G.add_edge(5, 8)
    G.add_edge(6, 13)    
    G.add_edge(6, 10)   
    G.add_edge(7, 10)
    G.add_edge(7, 8)
    G.add_edge(8, 9)
    G.add_edge(8, 11)    
    G.add_edge(9, 11)
    G.add_edge(10, 13)    
    G.add_edge(10, 12) 
    G.add_edge(11, 12)  
    draw_graph(G)
    return G

def init_Graph4():
    G = nx.Graph()
    for i in range(15):
        G.add_node(i)   
    #Граф Произвольный
    G.add_edge(0, 1)    
    G.add_edge(0, 2)
    G.add_edge(0, 3)    
    G.add_edge(1, 5)   
    G.add_edge(2, 3)
    G.add_edge(2, 4)
    G.add_edge(3, 7)
    G.add_edge(4, 6)
    G.add_edge(5, 9)    
    G.add_edge(5, 8)
    G.add_edge(6, 13)    
    G.add_edge(6, 10)   
    G.add_edge(7, 10)
    G.add_edge(7, 8)
    G.add_edge(8, 9)
    G.add_edge(8, 11)    
    G.add_edge(9, 11)
    G.add_edge(10, 13)    
    G.add_edge(10, 12) 
    G.add_edge(11, 12) 
    G.add_edge(13, 14)
    G.add_edge(12, 14)    
    # G.add_edge(12, 15) 
    # G.add_edge(14, 15)   
    draw_graph(G)
    return G

def init_Graph5():
    G = nx.Graph()
    for i in range(16):
        G.add_node(i)   
    #Граф Произвольный
    G.add_edge(0, 1)    
    G.add_edge(0, 2)
    G.add_edge(0, 3)    
    G.add_edge(0, 4)   
    G.add_edge(4, 5)
    G.add_edge(5, 6)
    G.add_edge(5, 15)
    G.add_edge(6, 7)
    G.add_edge(6, 15)
    G.add_edge(7, 15)
    G.add_edge(1, 8)
    G.add_edge(1, 9)
    G.add_edge(8, 10)    
    G.add_edge(9, 10)
    G.add_edge(2, 10)    
    G.add_edge(2, 11)   
    G.add_edge(10, 11)
    G.add_edge(2, 3)
    G.add_edge(3, 12)
    G.add_edge(12, 13)
    G.add_edge(11, 13)
    G.add_edge(11, 14)
    G.add_edge(13, 14)      
    draw_graph(G)
    return G
