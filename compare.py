import numpy as np
import matplotlib.pyplot as plt
import csv
import methods as mt
import init_graphs as ing
import statistics as stat
import csv



def compare_by_brute_force():
    # values_p_graph1, array_range1_graph1, t_graph1 = mt.Brute_Force(ing.init_Graph1(), 0, 5)
    values_p_chain, array_range1_chain, t_chain = mt.Brute_Force(ing.init_Chain(), 0, 3)
    values_p_hyb, array_range1_hyb, t_hyb = mt.Brute_Force(ing.init_Hybrid(), 7, 14)
    values_p_net, array_range1_net, t_net = mt.Brute_Force(ing.init_Net(), 0, 3)
    values_p_ring, array_range1_ring, t_ring = mt.Brute_Force(ing.init_Ring(), 0, 2)
    values_p_star, array_range1_star, t_star = mt.Brute_Force(ing.init_Star(), 6, 3)
    values_p_tree, array_range1_tree, t_tree = mt.Brute_Force(ing.init_Tree(), 0, 6)
    values_p_point, array_range1_point, t_point = mt.Brute_Force(ing.init_Point(), 0, 1)
    
    plt.figure(1)
    # plt.plot(array_range1_graph1, values_p_graph1, marker=("."), label = ("Нерегулярная стуктура"),linewidth=3, markersize=10, color = "r")
    plt.plot(array_range1_chain, values_p_chain, marker=("x"), label = ("Цепь"),linewidth=3, markersize=10, color = "orange")
    plt.plot(array_range1_hyb, values_p_hyb, marker=("*"), label = ("Гибрид"),linewidth=3, markersize=10, color = "b")
    plt.plot(array_range1_net, values_p_net, marker=("."), label = ("Сеть"),linewidth=3, markersize=10, color = "y")
    plt.plot(array_range1_ring, values_p_ring, marker=("."), label = ("Кольцо"), linewidth=3, markersize=10, color = "c")
    plt.plot(array_range1_star, values_p_star, marker=("o"), label = ("Звезда"), linewidth=3, markersize=10, color = "m")
    plt.plot(array_range1_tree, values_p_tree, marker=("."), linestyle='dashed', label = ("Дерево"), linewidth=3, markersize=10, color = "darkgreen")
    plt.plot(array_range1_point, values_p_point, marker=("o"),linestyle='dashdot', label = ("Точка-Точка"), linewidth=3, markersize= 4, color = "hotpink")
    plt.xlabel('Вероятность существование ребра')
    plt.ylabel('Надежность вычислительной сети')
    plt.grid(True)
    plt.legend()
    
    # header = ['P', 'Нерегулярная структура', 'Цепь', 'Гибридная топология','Сеть','Кольцо','Звезда','Дерево','Точка-Точка']
    # all_values = [values_p_graph1, values_p_chain, values_p_hyb, values_p_net, values_p_ring, values_p_star,values_p_tree,values_p_point]
    # with open('C:/Users/alng/Desktop/диплВ/brute_force.csv', 'w', newline='') as f:
    #     writer = csv.writer(f)

    # # write the header
    #     writer.writerow(header)
    #     for i in range (len(array_range1_chain)):
    #         tmp = []
    #         tmp.append(round(array_range1_chain[i], 3))
    #         for j in range (len(all_values)):
    #             tmp.append(round(all_values[j][i], 3))
    #         writer.writerow(tmp)
    #     tmp2 = []
    #     tmp2.append('Время, с.')
    #     tmp2.append(round(stat.mean(t_graph1), 3))
    #     tmp2.append(round(stat.mean(t_chain), 3))
    #     tmp2.append(round(stat.mean(t_hyb), 3))
    #     tmp2.append(round(stat.mean(t_net), 3))
    #     tmp2.append(round(stat.mean(t_ring), 3))
    #     tmp2.append(round(stat.mean(t_star), 3))
    #     tmp2.append(round(stat.mean(t_tree), 3))
    #     tmp2.append(round(stat.mean(t_point), 3))
    #     writer.writerow(tmp2)

    plt.show()


def compare_by_sim_model():
    # values_p_graph1, array_range1_graph1, t_graph1 = mt.simlation_model(ing.init_Graph1(), 0, 5, 3, 6)
    values_p_chain, array_range1_chain, t_chain = mt.simlation_model(ing.init_Chain(), 0, 3, 3, 3)
    values_p_hyb, array_range1_hyb, t_hyb = mt.simlation_model(ing.init_Hybrid(), 7, 14, 4, 15)
    values_p_net, array_range1_net, t_net = mt.simlation_model(ing.init_Net(), 0, 3, 1, 7)
    values_p_ring, array_range1_ring, t_ring = mt.simlation_model(ing.init_Ring(), 0, 2, 2, 4)
    values_p_star, array_range1_star, t_star = mt.simlation_model(ing.init_Star(), 6, 3, 1, 7)
    values_p_tree, array_range1_tree, t_tree = mt.simlation_model(ing.init_Tree(), 0, 6, 3, 10)
    values_p_point, array_range1_point, t_point = mt.simlation_model(ing.init_Point(), 0, 1, 1, 1)
    
    plt.figure(1)
    # plt.plot(array_range1_graph1, values_p_graph1, marker=("."), label = ("Нерегулярная структура"),linewidth=3, markersize=10, color = "r")
    plt.plot(array_range1_chain, values_p_chain, marker=("x"), label = ("Цепь"),linewidth=3, markersize=10, color = "orange")
    plt.plot(array_range1_hyb, values_p_hyb, marker=("*"), label = ("Гибрид"),linewidth=3, markersize=10, color = "b")
    plt.plot(array_range1_net, values_p_net, marker=("."), label = ("Сеть"),linewidth=3, markersize=10, color = "y")
    plt.plot(array_range1_ring, values_p_ring, marker=("."), label = ("Кольцо"), linewidth=3, markersize=10, color = "c")
    plt.plot(array_range1_star, values_p_star, marker=("o"), label = ("Звезда"), linewidth=3, markersize=10, color = "m")
    plt.plot(array_range1_tree, values_p_tree, marker=("."), linestyle='dashed', label = ("Дерево"), linewidth=3, markersize=10, color = "darkgreen")
    plt.plot(array_range1_point, values_p_point, marker=("o"),linestyle='dashdot', label = ("Точка-Точка"), linewidth=3, markersize= 4, color = "hotpink")
    plt.xlabel('Вероятность существования ребра')
    plt.ylabel('Надежность')
    plt.grid(True)
    plt.legend()
    
    # header = ['P', 'Произвольнй граф', 'Цепь', 'Гибрид','Сеть','Кольцо','Звезда','Дерево','Точка-Точка']
    # all_values = [values_p_graph1, values_p_chain, values_p_hyb, values_p_net, values_p_ring, values_p_star,values_p_tree,values_p_point]
    # with open('C:/Users/alng/Desktop/диплВ/simul_model.csv', 'w', newline='') as f:
    #     writer = csv.writer(f)

    # # write the header
    #     writer.writerow(header)
    #     for i in range (len(array_range1_chain)):
    #         tmp = []
    #         tmp.append(round(array_range1_chain[i], 3))
    #         for j in range (len(all_values)):
    #             tmp.append(round(all_values[j][i], 3))
    #         writer.writerow(tmp)
    #     tmp2 = []
    #     tmp2.append('Время')
    #     tmp2.append(round(stat.mean(t_graph1), 3))
    #     tmp2.append(round(stat.mean(t_chain), 3))
    #     tmp2.append(round(stat.mean(t_hyb), 3))
    #     tmp2.append(round(stat.mean(t_net), 3))
    #     tmp2.append(round(stat.mean(t_ring), 3))
    #     tmp2.append(round(stat.mean(t_star), 3))
    #     tmp2.append(round(stat.mean(t_tree), 3))
    #     tmp2.append(round(stat.mean(t_point), 3))
    #     writer.writerow(tmp2)

    plt.show()


def compare_by_lvm():
    print("init_Graph1")
    # values_p_graph1, array_range1_graph1, t_graph1 = mt.lvm(ing.init_Graph1(), 0, 3)
    print("init_Chain")
    values_p_chain, array_range1_chain, t_chain = mt.lvm(ing.init_Chain(), 0, 3)
    print("init_Hybrid")
    values_p_hyb, array_range1_hyb, t_hyb = mt.lvm(ing.init_Hybrid(), 7, 14)
    print("init_Net")
    values_p_net, array_range1_net, t_net = mt.lvm(ing.init_Net(), 0, 3)
    print("init_Ring")
    values_p_ring, array_range1_ring, t_ring = mt.lvm(ing.init_Ring(), 0, 2)
    print("init_Star")
    values_p_star, array_range1_star, t_star = mt.lvm(ing.init_Star(), 6, 3)
    print("init_Tree")
    values_p_tree, array_range1_tree, t_tree = mt.lvm(ing.init_Tree(), 0, 6)
    # print("init_Point")
    # values_p_point, array_range1_point, t_point = mt.lvm(ing.init_Point(), 0, 1)

    plt.figure(1)
    # plt.plot(array_range1_graph1, values_p_graph1, marker=("."), label = ("Нерегулярная структура"),linewidth=3, markersize=10, color = "r")
    plt.plot(array_range1_chain, values_p_chain, marker=("x"), label = ("Цепь"),linewidth=3, markersize=10, color = "orange")
    plt.plot(array_range1_hyb, values_p_hyb, marker=("*"), label = ("Гибрид"),linewidth=3, markersize=10, color = "b")
    plt.plot(array_range1_net, values_p_net, marker=("."), label = ("Сеть"),linewidth=3, markersize=10, color = "y")
    plt.plot(array_range1_ring, values_p_ring, marker=("."), label = ("Кольцо"), linewidth=3, markersize=10, color = "c")
    plt.plot(array_range1_star, values_p_star, marker=("o"), label = ("Звезда"), linewidth=3, markersize=10, color = "m")
    plt.plot(array_range1_tree, values_p_tree, marker=("."), linestyle='dashed', label = ("Дерево"), linewidth=3, markersize=10, color = "darkgreen")
    # plt.plot(array_range1_point, values_p_point, marker=("o"),linestyle='dashdot', label = ("Точка-Точка"), linewidth=3, markersize= 4, color = "hotpink")
    plt.xlabel('Вероятность существования вершины')
    plt.ylabel('Надежность вычислительной сети')
    plt.grid(True)
    plt.legend()

    # header = ['P', 'Нерегулярная структура', 'Цепь', 'Гибридная топология','Сеть','Кольцо','Звезда','Дерево'] #,'Точка-Точка']
    # all_values = [values_p_graph1, values_p_chain, values_p_hyb, values_p_net, values_p_ring, values_p_star,values_p_tree] #,values_p_point]
    # with open('C:/Users/alng/Desktop/диплВ/lvm.csv', 'w', newline='') as f:
    #     writer = csv.writer(f)

    # # write the header
    #     writer.writerow(header)
    #     for i in range (len(array_range1_chain)):
    #         tmp = []
    #         tmp.append(round(array_range1_chain[i], 3))
    #         for j in range (len(all_values)):
    #             tmp.append(round(all_values[j][i], 3))
    #         writer.writerow(tmp)
    #     tmp2 = []
    #     tmp2.append('Время, с.')
    #     tmp2.append(round(stat.mean(t_graph1), 3))
    #     tmp2.append(round(stat.mean(t_chain), 3))
    #     tmp2.append(round(stat.mean(t_hyb), 3))
    #     tmp2.append(round(stat.mean(t_net), 3))
    #     tmp2.append(round(stat.mean(t_ring), 3))
    #     tmp2.append(round(stat.mean(t_star), 3))
    #     tmp2.append(round(stat.mean(t_tree), 3))
    #     # tmp2.append(round(stat.mean(t_point), 3))
    #     writer.writerow(tmp2)

    plt.show()


def compare_Graph1():
    values_p_graph1_bf, array_range1_graph1_bf, t_graph1_bf = mt.Brute_Force(ing.init_Graph1(), 0, 5)
    values_p_graph1_sm, array_range1_graph1_sm, t_graph1_sm = mt.simlation_model(ing.init_Graph1(), 0, 5, 3, ing.init_Graph1().number_of_edges()-2+1)
    values_p_graph1_dc, array_range1_graph1_dc = mt.decomposition()
    array_range1_graph1_litvak, uppers, lowers = mt.LowerAndUpperBoundary(ing.init_Graph1(), 0, 5)

    plt.figure(1)
    plt.plot(array_range1_graph1_bf, values_p_graph1_bf, marker=("."), label = ("Полный перебор"), linewidth=3, markersize=10, color = "r")
    plt.plot(array_range1_graph1_sm, values_p_graph1_sm, marker=("x"), label = ("Имитационное моделирование"), linewidth=3, markersize=10, color = "orange")
    plt.plot(array_range1_graph1_dc, values_p_graph1_dc, marker=("x"), label = ("Декомпозиция"), linewidth=3, markersize=10, color = "blue")
    plt.plot(array_range1_graph1_litvak, uppers, marker=("x"), label = ("Верхняя граница"), linewidth=3, markersize=10, color = "pink")
    plt.plot(array_range1_graph1_litvak, lowers, marker=("x"), label = ("Нижняя граница"), linewidth=3, markersize=10, color = "m")
    plt.xlabel('Вероятность существования ребра')
    plt.ylabel('Надежность вычислительной сети')
    plt.legend()
    plt.grid()
    plt.title("Нерегулярная структура")
    plt.show()

def compare_Point():
    values_p_graph1_bf, array_range1_graph1_bf, t_graph1_bf = mt.Brute_Force(ing.init_Point(), 0, 1)
    values_p_graph1_sm, array_range1_graph1_sm, t_graph1_sm = mt.simlation_model(ing.init_Point(), 0, 1, 1, ing.init_Point().number_of_edges()-1+1)
    plt.figure(1)
    plt.plot(array_range1_graph1_bf, values_p_graph1_bf, marker=("."), label = ("Полный перебор"), linewidth=3, markersize=10, color = "r")
    plt.plot(array_range1_graph1_sm, values_p_graph1_sm, marker=("x"), label = ("Имитационное моделирование"), linewidth=3, markersize=10, color = "orange")
    plt.xlabel('Вероятность существования ребра')
    plt.ylabel('Надежность вычислительной сети')
    plt.grid()
    plt.title("Точка-Точка")
    plt.show()

def compare_Net():
    values_p_graph1_bf, array_range1_graph1_bf, t_graph1_bf = mt.Brute_Force(ing.init_Net(), 0, 3)
    values_p_graph1_sm, array_range1_graph1_sm, t_graph1_sm = mt.simlation_model(ing.init_Net(), 0, 3, 1, ing.init_Net().number_of_edges()-4+1)
    array_range1_graph1_litvak, uppers, lowers = mt.LowerAndUpperBoundary(ing.init_Net(), 0, 3)   
    
    plt.figure(1)
    plt.plot(array_range1_graph1_bf, values_p_graph1_bf, marker=("."), label = ("Полный перебор"), linewidth=3, markersize=10, color = "r")
    plt.plot(array_range1_graph1_sm, values_p_graph1_sm, marker=("x"), label = ("Имитационное моделирование"), linewidth=3, markersize=10, color = "orange")
    plt.plot(array_range1_graph1_litvak, uppers, marker=("x"), label = ("Верхняя граница"), linewidth=3, markersize=10, color = "pink")
    plt.plot(array_range1_graph1_litvak, lowers, marker=("x"), label = ("Нижняя граница"), linewidth=3, markersize=10, color = "m")
    plt.xlabel('Вероятность существования ребра')
    plt.ylabel('Надежность вычислительной сети')
    plt.legend()
    plt.grid()
    plt.title("Сеть")
    plt.show()

def compare_Star():
    values_p_graph1_bf, array_range1_graph1_bf, t_graph1_bf = mt.Brute_Force(ing.init_Star(), 6, 3)
    values_p_graph1_sm, array_range1_graph1_sm, t_graph1_sm = mt.simlation_model(ing.init_Star(), 6, 3, 1, ing.init_Star().number_of_edges()-1+1)
    plt.figure(1)
    plt.plot(array_range1_graph1_bf, values_p_graph1_bf, marker=("."), label = ("Полный перебор"), linewidth=3, markersize=10, color = "r")
    plt.plot(array_range1_graph1_sm, values_p_graph1_sm, marker=("x"), label = ("Имитационное моделирование"), linewidth=3, markersize=10, color = "orange")
    plt.xlabel('Вероятность существования ребра')
    plt.ylabel('Надежность вычислительной сети')
    plt.grid()
    plt.title("Звезда")
    plt.show()

def compare_Ring():
    values_p_graph1_bf, array_range1_graph1_bf, t_graph1_bf = mt.Brute_Force(ing.init_Ring(), 0, 2)
    values_p_graph1_sm, array_range1_graph1_sm, t_graph1_sm = mt.simlation_model(ing.init_Ring(), 0, 2, 2, ing.init_Ring().number_of_edges()-2+1)
    plt.figure(1)
    plt.plot(array_range1_graph1_bf, values_p_graph1_bf, marker=("."), label = ("Полный перебор"), linewidth=3, markersize=10, color = "r")
    plt.plot(array_range1_graph1_sm, values_p_graph1_sm, marker=("x"), label = ("Имитационное моделирование"), linewidth=3, markersize=10, color = "orange")
    plt.xlabel('Вероятность существования ребра')
    plt.ylabel('Надежность вычислительной сети')
    plt.grid()
    plt.title("Кольцо")
    plt.show()

def compare_Tree():
    values_p_graph1_bf, array_range1_graph1_bf, t_graph1_bf = mt.Brute_Force(ing.init_Tree(), 0, 6)
    values_p_graph1_sm, array_range1_graph1_sm, t_graph1_sm = mt.simlation_model(ing.init_Tree(), 0, 6, 3, ing.init_Tree().number_of_edges()-1+1)
    plt.figure(1)
    plt.plot(array_range1_graph1_bf, values_p_graph1_bf, marker=("."), label = ("Полный перебор"), linewidth=3, markersize=10, color = "r")
    plt.plot(array_range1_graph1_sm, values_p_graph1_sm, marker=("x"), label = ("Имитационное моделирование"), linewidth=3, markersize=10, color = "orange")
    plt.xlabel('Вероятность существования ребра')
    plt.ylabel('Надежность вычислительной сети')
    plt.grid()
    plt.title("Дерево")
    plt.show()

def compare_Chain():
    values_p_graph1_bf, array_range1_graph1_bf, t_graph1_bf = mt.Brute_Force(ing.init_Chain(), 0, 3)
    values_p_graph1_sm, array_range1_graph1_sm, t_graph1_sm = mt.simlation_model(ing.init_Chain(), 0, 3, 3, ing.init_Chain().number_of_edges()-1+1)
    plt.figure(1)
    plt.plot(array_range1_graph1_bf, values_p_graph1_bf, marker=("."), label = ("Полный перебор"), linewidth=3, markersize=10, color = "r")
    plt.plot(array_range1_graph1_sm, values_p_graph1_sm, marker=("x"), label = ("Имитационное моделирование"), linewidth=3, markersize=10, color = "orange")
    plt.xlabel('Вероятность существования ребра')
    plt.ylabel('Надежность вычислительной сети')
    plt.grid()
    plt.title("Цепь")
    plt.show()

def compare_Hybrid():
    values_p_graph1_bf, array_range1_graph1_bf, t_graph1_bf = mt.Brute_Force(ing.init_Hybrid(), 7, 14)
    values_p_graph1_sm, array_range1_graph1_sm, t_graph1_sm = mt.simlation_model(ing.init_Hybrid(), 7, 14, 4, ing.init_Hybrid().number_of_edges()-1+1)
    plt.figure(1)
    plt.plot(array_range1_graph1_bf, values_p_graph1_bf, marker=("."), label = ("Полный перебор"), linewidth=3, markersize=10, color = "r")
    plt.plot(array_range1_graph1_sm, values_p_graph1_sm, marker=("x"), label = ("Имитационное моделирование"), linewidth=3, markersize=10, color = "orange")
    plt.xlabel('Вероятность существования ребра')
    plt.ylabel('Надежность вычислительной сети')
    plt.grid()
    plt.title("Гибрид")
    plt.show()
    
def compare_Graph2():
    values_p_graph2_bf, array_range1_graph2_bf, t_graph1_bf = mt.Brute_Force(ing.init_Graph2(), 0, 20)
    values_p_graph2_sm, array_range1_graph2_sm, t_graph1_sm = mt.simlation_model(ing.init_Graph2(), 0, 20, 5, ing.init_Graph2().number_of_edges()-2+1)
    array_range1_graph2_litvak, uppers, lowers = mt.LowerAndUpperBoundary(ing.init_Graph2(), 0, 20)
        
    plt.figure(1)
    plt.plot(array_range1_graph2_bf, values_p_graph2_bf, marker=("."), label = ("Полный перебор"), linewidth=3, markersize=10, color = "r")
    plt.plot(array_range1_graph2_sm, values_p_graph2_sm, marker=("x"), label = ("Имитационное моделирование"), linewidth=3, markersize=10, color = "orange")
    plt.plot(array_range1_graph2_litvak, uppers, marker=("x"), label = ("Верхняя граница"), linewidth=3, markersize=10, color = "pink")
    plt.plot(array_range1_graph2_litvak, lowers, marker=("x"), label = ("Нижняя граница"), linewidth=3, markersize=10, color = "m")
    plt.xlabel('Вероятность существования ребра')
    plt.ylabel('Надежность вычислительной сети')
    plt.legend()
    plt.grid()
    plt.title("Сложный граф")
    plt.show()    
    
def compare_Graph5():
    # values_p_graph5_bf, array_range1_graph5_bf, t_graph1_bf = mt.Brute_Force(ing.init_Graph5(), 0, 15)
    values_p_graph5_sm, array_range1_graph5_sm, t_graph1_sm = mt.simlation_model(ing.init_Graph5(), 0, 15, 3, ing.init_Graph5().number_of_edges()-3+1)
    array_range1_graph5_litvak, uppers, lowers = mt.LowerAndUpperBoundary(ing.init_Graph5(), 0, 15)
        
    plt.figure(1)
    # plt.plot(array_range1_graph5_bf, values_p_graph5_bf, marker=("."), label = ("Полный перебор"), linewidth=3, markersize=10, color = "r")
    plt.plot(array_range1_graph5_sm, values_p_graph5_sm, marker=("x"), label = ("Имитационное моделирование"), linewidth=3, markersize=10, color = "orange")
    plt.plot(array_range1_graph5_litvak, uppers, marker=("x"), label = ("Верхняя граница"), linewidth=3, markersize=10, color = "pink")
    plt.plot(array_range1_graph5_litvak, lowers, marker=("x"), label = ("Нижняя граница"), linewidth=3, markersize=10, color = "m")
    plt.xlabel('Вероятность существования ребра')
    plt.ylabel('Надежность вычислительной сети')
    plt.legend()
    plt.grid()
    plt.title("Сложный граф")
    plt.show()    

def compare_Graph3():
    values_p_graph3_bf, array_range1_graph3_bf, t_graph1_bf = mt.Brute_Force(ing.init_Graph3(), 0, 13)
    values_p_graph3_sm, array_range1_graph3_sm, t_graph1_sm = mt.simlation_model(ing.init_Graph3(), 0, 13, 4, ing.init_Graph3().number_of_edges()-2+1)
    values_p_lower = np.zeros(11)
    values_p_upper = np.zeros(11)
    for i in range(len(array_range1_graph3_bf)):
        values_p_upper[i], values_p_lower[i] = mt.LowerAndUpperBoundary(array_range1_graph3_bf[i],ing.init_Graph3(), 0, 13)
        
    plt.figure(1)
    plt.plot(array_range1_graph3_bf, values_p_graph3_bf, marker=("."), label = ("Полный перебор"), linewidth=3, markersize=10, color = "r")
    plt.plot(array_range1_graph3_sm, values_p_graph3_sm, marker=("x"), label = ("Имитационное моделирование"), linewidth=3, markersize=10, color = "orange")
    plt.plot(array_range1_graph3_bf, values_p_upper, marker=("x"), label = ("Верхняя граница"), linewidth=3, markersize=10, color = "pink")
    plt.plot(array_range1_graph3_bf, values_p_lower, marker=("x"), label = ("Нижняя граница"), linewidth=3, markersize=10, color = "m")
    plt.xlabel('Вероятность существования ребра')
    plt.ylabel('Надежность вычислительной сети')
    plt.legend()
    plt.grid()
    plt.title("Сложный граф")
    plt.show()  

def compare_Graph4():
    values_p_graph4_bf, array_range1_graph4_bf, t_graph1_bf = mt.Brute_Force(ing.init_Graph4(), 0, 14)
    values_p_graph4_sm, array_range1_graph4_sm, t_graph1_sm = mt.simlation_model(ing.init_Graph4(), 0, 14, 5, ing.init_Graph4().number_of_edges()-2+1)
    values_p_lower = np.zeros(11)
    values_p_upper = np.zeros(11)
    for i in range(len(array_range1_graph4_sm)):
        values_p_upper[i], values_p_lower[i] = mt.LowerAndUpperBoundary(array_range1_graph4_sm[i],ing.init_Graph4(), 0, 14)
        
    plt.figure(1)
    # plt.plot(array_range1_graph4_bf, values_p_graph4_bf, marker=("."), label = ("Полный перебор"), linewidth=3, markersize=10, color = "r")
    plt.plot(array_range1_graph4_sm, values_p_graph4_sm, marker=("x"), label = ("Имитационное моделирование"), linewidth=3, markersize=10, color = "orange")
    plt.plot(array_range1_graph4_sm, values_p_upper, marker=("x"), label = ("Верхняя граница"), linewidth=3, markersize=10, color = "pink")
    plt.plot(array_range1_graph4_sm, values_p_lower, marker=("x"), label = ("Нижняя граница"), linewidth=3, markersize=10, color = "m")
    plt.xlabel('Вероятность существования ребра')
    plt.ylabel('Надежность вычислительной сети')
    plt.legend()
    plt.grid()
    plt.title("Сложный граф")
    plt.show()   
    


def compare_by_edges(p):
    k = int(p * 10)
    arr = []
    values_p, array_range1, time_array = mt.Brute_Force(ing.init_ShortGraph5(), 0, 5)
    arr.append(values_p[k])
    values_p, array_range1, time_array = mt.Brute_Force(ing.init_ShortGraph6(), 0, 5)
    arr.append(values_p[k])
    values_p, array_range1, time_array = mt.Brute_Force(ing.init_ShortGraph7(), 0, 5)
    arr.append(values_p[k])
    values_p, array_range1, time_array = mt.Brute_Force(ing.init_ShortGraph8(), 0, 5)
    arr.append(values_p[k])
    values_p, array_range1, time_array = mt.Brute_Force(ing.init_ShortGraph9(), 0, 5)
    arr.append(values_p[k])
    values_p, array_range1, time_array = mt.Brute_Force(ing.init_ShortGraph10(), 0, 5)
    arr.append(values_p[k])
    values_p, array_range1, time_array = mt.Brute_Force(ing.init_FullGraph(), 0, 5)
    arr.append(values_p[k])
    arr_edge = np.arange(5, 12, 1)

    plt.figure(1)
    plt.subplot(1, 1, 1)
    plt.plot(arr_edge, arr, marker=("."),linewidth=3, markersize=10, color = "g")
    plt.xlabel('Количество ребер')
    plt.ylabel('Надежность вычислительной сети')
    plt.grid(True)
    plt.legend()
    plt.title("p = " + str(p))

    plt.show()
    return arr

def compare_by_edges_all():
    arr_edge = np.arange(5, 12, 1)
    arr03 = compare_by_edges(0.3)
    arr06 = compare_by_edges(0.6)
    arr09 = compare_by_edges(0.9)
    plt.figure(1)
    plt.subplot(1, 1, 1)
    plt.plot(arr_edge, arr03, label="p = 0.3", marker=("."), linewidth=3, markersize=5, color = "r")
    plt.plot(arr_edge, arr06, label="p = 0.6", marker=("."), linewidth=3, markersize=5, color = "g")
    plt.plot(arr_edge, arr09, label="p = 0.9", marker=("."), linewidth=3, markersize=5, color = "b")
    plt.xlabel('Количество ребер')
    plt.ylabel('Надежность вычислительной сети')
    plt.grid(True)
    plt.legend()
    plt.title("")

    plt.show()


def compare_Graph1_nodes_type():
    values_p_graph1_smn, array_range1_graph1_smn = mt.simul_model_nodes(ing.init_Graph1(), 0, 5)
    values_p_graph1_lvm, array_range1_graph1_lvm, t_graph1 = mt.lvm(ing.init_Graph1(), 0, 5)
    values_p_graph1_bf, array_range1_graph1__bf = mt.brute_force_nodes_type(ing.init_Graph1(), 0, 5)
    plt.figure(1)
    plt.plot(array_range1_graph1_smn, values_p_graph1_smn, marker=("x"), label = ("Имитационное моделирование"), linewidth=3, markersize=10, color = "r")
    plt.plot(array_range1_graph1_lvm, values_p_graph1_lvm, marker=("x"), label = ("Логико-вероятностный метод"), linewidth=3, markersize=10, color = "g")
    plt.plot(array_range1_graph1__bf, values_p_graph1_bf, marker=("x"), label = ("Полный перебор"), linewidth=3, markersize=10, color = "m")
    plt.xlabel('Вероятность существования вершины')
    plt.ylabel('Надежность вычислительной сети')
    plt.grid()
    plt.legend()
    plt.title("Нерегулярная структура")
    plt.show()

def compare_Point_nodes_type():
    values_p_graph1_smn, array_range1_graph1_smn = mt.simul_model_nodes(ing.init_Point(), 0, 1)
    # values_p_graph1_lvm, array_range1_graph1_lvm, t_graph1 = mt.lvm(ing.init_Point(), 0, 5)
    values_p_graph1_bf, array_range1_graph1_bf = mt.brute_force_nodes_type(ing.init_Point(), 0, 1)
    plt.figure(1)
    plt.plot(array_range1_graph1_smn, values_p_graph1_smn, marker=("x"), label = ("Имитационное моделирование"), linewidth=3, markersize=10, color = "r")
    # plt.plot(array_range1_graph1_lvm, values_p_graph1_lvm, marker=("x"), label = ("Логико-вероятностный метод"), linewidth=3, markersize=10, color = "g")
    plt.plot(array_range1_graph1_bf, values_p_graph1_bf, marker=("x"), label = ("Полный перебор"), linewidth=3, markersize=10, color = "m")
    plt.xlabel('Вероятность существования ребра')
    plt.ylabel('Надежность вычислительной сети')
    plt.grid()
    plt.legend()
    plt.title("Точка-точка")
    plt.show()

def compare_Net_nodes_type():
    values_p_graph1_smn, array_range1_graph1_smn = mt.simul_model_nodes(ing.init_Net(), 0, 3)
    values_p_graph1_lvm, array_range1_graph1_lvm, t_graph1 = mt.lvm(ing.init_Net(), 0, 3)
    values_p_graph1_bf, array_range1_graph1_bf = mt.brute_force_nodes_type(ing.init_Net(), 0, 3)
    plt.figure(1)
    plt.plot(array_range1_graph1_smn, values_p_graph1_smn, marker=("x"), label = ("Имитационное моделирование"), linewidth=3, markersize=10, color = "r")
    plt.plot(array_range1_graph1_lvm, values_p_graph1_smn,marker=("."), label = ("Логико-вероятностный метод"),  markerfacecolor=('black'), linewidth=3, markersize=10, color = "g")
    plt.plot(array_range1_graph1_bf, values_p_graph1_bf, marker=("x"), label = ("Полный перебор"), linewidth=3, markersize=10, color = "m")
    plt.xlabel('Вероятность существования вершины')
    plt.ylabel('Надежность вычислительной сети')
    plt.grid()
    plt.legend()
    plt.title("Сеть")
    plt.show()

def compare_Star_nodes_type():
    values_p_graph1_smn, array_range1_graph1_smn = mt.simul_model_nodes(ing.init_Star(), 6, 3)
    values_p_graph1_lvm, array_range1_graph1_lvm, t_graph1 = mt.lvm(ing.init_Star(), 6, 3)
    values_p_graph1_bf, array_range1_graph1_bf = mt.brute_force_nodes_type(ing.init_Star(), 6, 3)
    plt.figure(1)
    # plt.plot(array_range1_graph1_smn, values_p_graph1_smn, marker=("x"), label = ("Имитационное моделирование"), linewidth=3, markersize=10, color = "r")
    plt.plot(array_range1_graph1_lvm, values_p_graph1_lvm, marker=("x"), label = ("Логико-вероятностный метод"), linewidth=3, markersize=10, color = "g")
    # plt.plot(array_range1_graph1_bf, values_p_graph1_bf, marker=("x"), label = ("Полный перебор"), linewidth=3, markersize=10, color = "m")
    plt.xlabel('Вероятность существования вершины')
    plt.ylabel('Надежность вычислительной сети')
    plt.grid()
    plt.legend()
    plt.title("Звезда")
    plt.show()

def compare_Ring_nodes_type():
    values_p_graph1_smn, array_range1_graph1_smn = mt.simul_model_nodes(ing.init_Ring(), 0, 2)
    values_p_graph1_lvm, array_range1_graph1_lvm, t_graph1 = mt.lvm(ing.init_Ring(), 0, 2)
    values_p_graph1_bf, array_range1_graph1_bf = mt.brute_force_nodes_type(ing.init_Ring(), 0, 2)
    plt.figure(1)
    plt.plot(array_range1_graph1_smn, values_p_graph1_smn, marker=("x"), label = ("Имитационное моделирование"), linewidth=3, markersize=10, color = "r")
    plt.plot(array_range1_graph1_lvm, values_p_graph1_lvm, marker=("x"), label = ("Логико-вероятностный метод"), linewidth=3, markersize=10, color = "g")
    plt.plot(array_range1_graph1_bf, values_p_graph1_bf, marker=("x"), label = ("Полный перебор"), linewidth=3, markersize=10, color = "m")
    plt.xlabel('Вероятность существования вершины')
    plt.ylabel('Надежность вычислительной сети')
    plt.grid()
    plt.legend()
    plt.title("Кольцо")
    plt.show()

def compare_Tree_nodes_type():
    values_p_graph1_smn, array_range1_graph1_smn = mt.simul_model_nodes(ing.init_Tree(), 0, 6)
    values_p_graph1_lvm, array_range1_graph1_lvm, t_graph1 = mt.lvm(ing.init_Tree(), 0, 6)
    values_p_graph1_bf, array_range1_graph1_bf = mt.brute_force_nodes_type(ing.init_Tree(), 0, 6)
    plt.figure(1)
    plt.plot(array_range1_graph1_smn, values_p_graph1_smn, marker=("x"), label = ("Имитационное моделирование"), linewidth=3, markersize=10, color = "r")
    plt.plot(array_range1_graph1_lvm, values_p_graph1_lvm, marker=("x"), label = ("Логико-вероятностный метод"), linewidth=3, markersize=10, color = "g")
    plt.plot(array_range1_graph1_bf, values_p_graph1_bf, marker=("x"), label = ("Полный перебор"), linewidth=3, markersize=10, color = "m")
    plt.xlabel('Вероятность существования вершины')
    plt.ylabel('Надежность вычислительной сети')
    plt.grid()
    plt.legend()
    plt.title("Дерево")
    plt.show()

def compare_Chain_nodes_type():
    values_p_graph1_smn, array_range1_graph1_smn = mt.simul_model_nodes(ing.init_Chain(), 0, 3)
    values_p_graph1_lvm, array_range1_graph1_lvm, t_graph1 = mt.lvm(ing.init_Chain(), 0, 3)
    values_p_graph1_bf, array_range1_graph1_bf = mt.brute_force_nodes_type(ing.init_Chain(), 0, 3)
    plt.figure(1)
    plt.plot(array_range1_graph1_smn, values_p_graph1_smn, marker=("x"), label = ("Имитационное моделирование"), linewidth=3, markersize=10, color = "r")
    plt.plot(array_range1_graph1_lvm, values_p_graph1_lvm, marker=("x"), label = ("Логико-вероятностный метод"), linewidth=3, markersize=10, color = "g")
    plt.plot(array_range1_graph1_bf, values_p_graph1_bf, marker=("x"), label = ("Полный перебор"), linewidth=3, markersize=10, color = "m")
    plt.xlabel('Вероятность существования вершины')
    plt.ylabel('Надежность вычислительной сети')
    plt.grid()
    plt.legend()
    plt.title("Цепь")
    plt.show()

def compare_Hybrid_nodes_type():
    values_p_graph1_smn, array_range1_graph1_smn = mt.simul_model_nodes(ing.init_Hybrid(), 7, 14)
    values_p_graph1_lvm, array_range1_graph1_lvm, t_graph1 = mt.lvm(ing.init_Hybrid(), 7, 14)
    values_p_graph1_bf, array_range1_graph1_bf = mt.brute_force_nodes_type(ing.init_Hybrid(), 7, 14)
    plt.figure(1)
    plt.plot(array_range1_graph1_smn, values_p_graph1_smn, marker=("x"), label = ("Имитационное моделирование"), linewidth=3, markersize=10, color = "r")
    plt.plot(array_range1_graph1_lvm, values_p_graph1_lvm, marker=("x"), label = ("Логико-вероятностный метод"), linewidth=3, markersize=10, color = "g")
    plt.plot(array_range1_graph1_bf, values_p_graph1_bf, marker=("x"), label = ("Полный перебор"), linewidth=3, markersize=10, color = "m")
    plt.xlabel('Вероятность существования вершины')
    plt.ylabel('Надежность вычислительной сети')
    plt.grid()
    plt.legend()
    plt.title("Гибрид")
    plt.show()


def compare_by_sim_model_nodes_type():
    values_p_graph1, array_range1_graph1 = mt.simul_model_nodes(ing.init_Graph1(), 0, 5)
    values_p_chain, array_range1_chain = mt.simul_model_nodes(ing.init_Chain(), 0, 3)
    values_p_hyb, array_range1_hyb = mt.simul_model_nodes(ing.init_Hybrid(), 7, 14)
    values_p_net, array_range1_net = mt.simul_model_nodes(ing.init_Net(), 0, 3)
    values_p_ring, array_range1_ring = mt.simul_model_nodes(ing.init_Ring(), 0, 2)
    values_p_star, array_range1_star = mt.simul_model_nodes(ing.init_Star(), 6, 3)
    values_p_tree, array_range1_tree = mt.simul_model_nodes(ing.init_Tree(), 0, 6)
    values_p_point, array_range1_point = mt.simul_model_nodes(ing.init_Point(), 0, 1)
    
    plt.figure(1)
    plt.plot(array_range1_graph1, values_p_graph1, marker=("."), label = ("Произвольнй граф"),linewidth=3, markersize=8, color = "r")
    plt.plot(array_range1_chain, values_p_chain, marker=("x"), label = ("Цепь"),linewidth=3, markersize=8, color = "orange")
    plt.plot(array_range1_hyb, values_p_hyb, marker=("*"), label = ("Гибрид"),linewidth=3, markersize=8, color = "b")
    plt.plot(array_range1_net, values_p_net, marker=("."), label = ("Сеть"),linewidth=3, markersize=8, color = "y")
    plt.plot(array_range1_ring, values_p_ring, marker=("."), label = ("Кольцо"), linewidth=3, markersize=8, color = "c")
    plt.plot(array_range1_star, values_p_star, marker=("o"), label = ("Звезда"), linewidth=3, markersize=8, color = "m")
    plt.plot(array_range1_tree, values_p_tree, marker=("."), linestyle='dashed', label = ("Дерево"), linewidth=3, markersize=8, color = "darkgreen")
    plt.plot(array_range1_point, values_p_point, marker=("o"),linestyle='dashdot', label = ("Точка-Точка"), linewidth=3, markersize= 8, color = "hotpink")
    plt.xlabel('Вероятность существования ребра')
    plt.ylabel('Надежность')
    plt.grid(True)
    plt.legend()
    
    # header = ['P', 'Произвольнй граф', 'Цепь', 'Гибрид','Сеть','Кольцо','Звезда','Дерево','Точка-Точка']
    # all_values = [values_p_graph1, values_p_chain, values_p_hyb, values_p_net, values_p_ring, values_p_star,values_p_tree,values_p_point]
    # with open('C:/Users/alng/Desktop/диплВ/simul_model.csv', 'w', newline='') as f:
    #     writer = csv.writer(f)

    # # write the header
    #     writer.writerow(header)
    #     for i in range (len(array_range1_chain)):
    #         tmp = []
    #         tmp.append(round(array_range1_chain[i], 3))
    #         for j in range (len(all_values)):
    #             tmp.append(round(all_values[j][i], 3))
    #         writer.writerow(tmp)
    #     tmp2 = []
    #     tmp2.append('Время')
    #     tmp2.append(round(stat.mean(t_graph1), 3))
    #     tmp2.append(round(stat.mean(t_chain), 3))
    #     tmp2.append(round(stat.mean(t_hyb), 3))
    #     tmp2.append(round(stat.mean(t_net), 3))
    #     tmp2.append(round(stat.mean(t_ring), 3))
    #     tmp2.append(round(stat.mean(t_star), 3))
    #     tmp2.append(round(stat.mean(t_tree), 3))
    #     tmp2.append(round(stat.mean(t_point), 3))
    #     writer.writerow(tmp2)

    plt.show()

def Full_and_Short_graphs():
    values_p_f, array_range1_f, t_full = mt.Brute_Force(ing.init_FullGraph(), 0, 5)
    values_p_s, array_range1_s, t_short = mt.Brute_Force(ing.init_ShortGraph10(), 0, 5)
    
    plt.figure(1)
    plt.subplot(1, 1, 1)
    plt.plot(array_range1_f, values_p_f, marker=("."), label = ("Исходный граф"),linewidth=3, markersize=10, color = "r")
    plt.plot(array_range1_s, values_p_s, marker=("x"), label = ("Связующее дерево + 5 ребер"),linewidth=3, markersize=10, color = "g")
    plt.xlabel('Вероятность существование ребра')
    plt.ylabel('Надежность вычислительной сети')
    plt.grid(True)
    plt.legend()
    
    print("Фулл граф: " + str(round(stat.mean(t_full), 3)))
    print("Не фулл граф: " + str(round(stat.mean(t_short), 3)))
    
    plt.show()