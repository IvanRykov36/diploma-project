import numpy as np
import itertools
import networkx as nx
import time

def has_path(G, v1, v2):
    if G.has_node(v1) and G.has_node(v2):
        try:
            nx.shortest_path_length(G, v1, v2)
        except nx.NetworkXNoPath:
            return False
    else:
        return False
    return True


# полный перебор -----------------------------------------------------------------------------
def Brute_Force(G, start_v, end_v):
    start_time = time.time()
    E = G.number_of_edges()
    N = G.number_of_nodes()
    all_subgraphs = []
    time_array = []
    array_range1 = np.arange(0.0, 1.1, 0.1)
    print("edg: " + str(list(G.edges)))
    j = 0
    p_res_array = np.zeros(len(array_range1))
    start_p = time.time()
    for e in range(E + 1):
        print("e: " + str(e))
        comb = itertools.combinations(list(G.edges), e)
        comb_list = list(comb)
        if len(comb_list[0]) != 0:
            for sg in comb_list:
                SG = nx.Graph()
                for i in range(N):
                    SG.add_node(i)
                for ee in sg:
                    v1 = ee[0]
                    v2 = ee[1]
                    SG.add_edge(v1, v2)
                j += 1
                all_subgraphs.append(SG)
                if has_path(SG, start_v, end_v):
                    edg = list(SG.edges)
                    for i in range(len(array_range1)):
                        p = array_range1[i]
                        p_subgraph = p ** len(edg) * (1 - p) ** (E - len(edg))
                        p_res_array[i] += p_subgraph

    end_p = time.time()
    time_array = np.ones(len(array_range1)) * (end_p - start_p)

    return p_res_array, array_range1, time_array


# имитационное моделирование -----------------------------------------------------------------
def simlation_model(G, start_v, end_v, l_min, l_max):
    E = G.number_of_edges()
    N = G.number_of_nodes()
    eps = 0.01
    N_exp = int(9/4 * 1/eps**2)
    time_array = []
    print("N_exp:" + str(N_exp))
    array_range2 = np.arange(0, 1.1, 0.1)
    path_normal = []
    path_fast = []
    N_array = []
    edg_array = list(G.edges)
    print(str(edg_array))
    for p in array_range2:
        print("--------------------------")
        print("p = " + str(p))
        start_time = time.time()
        N_count = 0 
        num_path_fast = 0
        if p > 0:
            for i in range(N_exp):
                SG = nx.Graph()
                for j in range(N):
                    SG.add_node(j)
                y = np.random.sample(E)
                for e in range(E):
                    if y[e] < p:
                        SG.add_edge(edg_array[e][0], edg_array[e][1])
                if (np.sum(y < p) > l_min and np.sum(y < p) < l_max):
                    N_count += 1
                    if has_path(SG, start_v, end_v):
                        num_path_fast += 1
                if np.sum(y < p) >= l_max:
                    num_path_fast += 1
        time_array.append(time.time() - start_time)           
        path_fast.append(num_path_fast/N_exp)
        print("fast = " + str(num_path_fast / N_exp))
        
    return path_fast, array_range2, time_array


# метод литвака-ушакова ----------------------------------------------------------------------
def LowerAndUpperBoundary(G, v1, v2):
    vstart = 0
    vend = 100
    array_range = np.arange(0, 1.1, 0.1)
    
    minpaths2 = list(nx.all_simple_paths(G, source=v1, target=v2))
    minpaths3 = []
    for i in range(len(minpaths2) - 1):
        Flag = False
        for j in range(i+1, len(minpaths2)):
            if i != j:
                per = list(set(minpaths2[i]) & set(minpaths2[j]))
                if len(per) == 2:
                    minpaths3.append([minpaths2[i],minpaths2[j]])
                    Flag = True
        if not Flag:
            minpaths3.append([minpaths2[i]])
    print("All_Pathes: " + str(minpaths3))

    edgespaths = []
    the = []
    for i in range(len(minpaths2)):
        edgespaths.append([])
        for j in range(len(minpaths2[i]) - 1):
            edgespaths[i].append((minpaths2[i][j], minpaths2[i][j + 1]))
    curpath = edgespaths[0]
    E = G.number_of_edges()
    cutz = []
    minlen = 999
    rescutz = []
    for e in range(E + 1):
        print("e: " + str(e))
        print("E: " + str(E))
        comb = itertools.combinations(list(G.edges), e)
        comb_list = list(comb)
        print("len: " + str(len(comb_list)))
        if len(comb_list[0]) != 0:
            for i in range(len(comb_list)):
                Gcur = G.copy()
                for j in range(len(comb_list[i])):
                    Gcur.remove_edge(comb_list[i][j][0],comb_list[i][j][1])
                if not has_path(Gcur, v1, v2):
                    if len(list(comb_list[i])) < minlen:
                        minlen = len(list(comb_list[i]))
                    cutz.append(list(comb_list[i]))
    #print("c " + str(cutz))

    minlencutz = []
    random = []
    for m in range(minlen, E):
        minlencutz = []
        rescutz = []
        for i in range(len(cutz)):
            if len(cutz[i]) == m:
                minlencutz.append(cutz[i])
                rescutz.append(cutz[i])
        for i in range(len(cutz)):
            per = []
            for j in range(len(minlencutz)):
                sper = list(set(cutz[i]) & set(minlencutz[j]))
                per.append(len(sper))
            if len(per) != 0:
                maxper = max(per)
                if maxper < m:
                    rescutz.append(cutz[i])
        cutz = rescutz.copy()
        random.append(rescutz)
    array = []
    l = - 1
    while len(random[l]) == 0:
        l -= 1
    random = random[l]
    print("\nAll_Minimal_Cuts: " + str(random))
    while len(random) != 0:
        i = len(random) - 1
        a = random[i]
        array.append([])
        array3 = []
        for j in range(i - 1, -1, -1):
            abc = list(set(a) & set(random[j]))
            abc2 = []
            for k in range(len(array[-1])):
                abc2.append(len(list(set(array[-1][k]) & set(random[j]))))
            if (len(abc) == 0 and len(abc2) == 0) or (len(abc2) != 0 and max(abc2) == 0 and len(abc) == 0):
                array[-1].append(random[j])
            else: 
                array3.append(random[j])
        array[-1].append(a)
        random = array3.copy()
        #print("random " + str(random))
    print("\nAll_Groups_of_Minimal_Cuts: " + str(array))


    uppers = []
    lowers = []
    for p in range(len(array_range)):
        q = 1 - array_range[p]
        arraypaths = []
        arraycuts = []
        for i in range(len(array)):
            if len(array[i]) == 1:
                arraycuts.append(1 - q**(len(np.unique(array[i][0]))))
                #arraycuts.append(1 - q**(len(np.unique(array[i][0])) - 1))
            else:
                mul = 1
                mul2 = 1
                for j in range(len(array[i])):
                    mul2 *= (1 - q**(len(np.unique(array[i][j]))))
                    #mul2 *= (1 - q**(len(np.unique(array[i][j])) - 1))
                arraycuts.append(mul2)
        uppers.append(min(arraycuts))
        print("\nUpperBound: " + str(min(arraycuts)))

        for i in range(len(minpaths3)):
            if len(minpaths3[i]) == 1:
                arraypaths.append(array_range[p]**(len(minpaths3[i][0])))
            else:
                mul = 1
                mul2 = 1
                for j in range(len(minpaths3[i])):
                    mul *= (1 - array_range[p]**(len(minpaths3[i][j])))
                arraypaths.append(1 - mul)
        lowers.append(max(arraypaths))
        print("LowerBound: " + str(max(arraypaths)))

    return array_range, uppers, lowers


# логико-вероятностный метод -----------------------------------------------------------------
def all_simple_paths(G, v1, v2):
    list_asp = []
    for asp in nx.all_simple_paths(G, v1, v2):
        list_asp.append(asp)
        # print(asp)
    return list_asp
    
def max_element(G, list_asp):
    numbers_of_max_elements = np.zeros(G.number_of_edges() + 1)
    for i in range(len(list_asp)):
        for j in range(len(list_asp[i])):
            numbers_of_max_elements[list_asp[i][j]] += 1
    index_max_el = np.argmax(numbers_of_max_elements[1:len(numbers_of_max_elements) - 1]) + 1
    value_of_repeates_max_el = np.max(numbers_of_max_elements[1:len(numbers_of_max_elements) - 1])
    # print("numbers_of_max_elements = " + str(numbers_of_max_elements))
    # print("index_max_el_from_def_max_el = " + str(index_max_el))
    # print("value_of_repeates_max_el = " + str(value_of_repeates_max_el))
    return numbers_of_max_elements #index_max_el,value_of_repeates_max_el

def zero(G, list_asp, numbers_of_max_elements):
    paths_without_max_el_zero = []
    index_max_el = np.argmax(numbers_of_max_elements[1:len(numbers_of_max_elements) - 1]) + 1
    value_of_repeates_max_el = np.max(numbers_of_max_elements[1:len(numbers_of_max_elements) - 1])
    all_indexes_of_max_elements_zero = []
    current_paths = list_asp
    paths_without_first_el = []
    #max_elements = []
    while value_of_repeates_max_el != 1:
        for i in range(len(current_paths)):
            if index_max_el not in current_paths[i]:
                paths_without_max_el_zero.append(current_paths[i])
        k = 0
        if len(paths_without_max_el_zero) != 0:
            if len(all_indexes_of_max_elements_zero) == 0:
                paths_without_first_el.append(paths_without_max_el_zero)
                # print("paths_without_first_el = " + str(paths_without_first_el))
            all_indexes_of_max_elements_zero.append(index_max_el)
            
        if len(paths_without_max_el_zero) == 0:
            for i in range(len(numbers_of_max_elements)):
                if numbers_of_max_elements[i] < value_of_repeates_max_el and numbers_of_max_elements[i] != 0:
                    break
            index_max_el = i
            value_of_repeates_max_el = numbers_of_max_elements[i]
            # print("index_of_max_element: " + str(i))
            continue
                
        numbers_of_max_elements = max_element(G, paths_without_max_el_zero)
        index_max_el = np.argmax(numbers_of_max_elements[1:len(numbers_of_max_elements) - 1]) + 1
        value_of_repeates_max_el = np.max(numbers_of_max_elements[1:len(numbers_of_max_elements) - 1])
        if value_of_repeates_max_el != 1:
            current_paths = paths_without_max_el_zero
            # print("current = " + str(current_paths))
            paths_without_max_el_zero = []
        # print("paths_without_max_el_zero = " + str(paths_without_max_el_zero))
        # print("all_indexes_of_max_elements_zero = " + str(all_indexes_of_max_elements_zero))
        
    
    return paths_without_max_el_zero, all_indexes_of_max_elements_zero, paths_without_first_el

def one(G, list_asp, numbers_of_max_elements):
    paths_with_max_el_one = []
    numbers_of_max_elements = max_element(G, paths_with_max_el_one)
    index_max_el = np.argmax(numbers_of_max_elements[1:len(numbers_of_max_elements) - 1]) + 1
    value_of_repeates_max_el = np.max(numbers_of_max_elements[1:len(numbers_of_max_elements) - 1])
    all_indexes_of_max_elements_one = []
    all_indexes_of_max_elements_one.append(index_max_el)
    current_paths = list_asp
    while value_of_repeates_max_el != 1:
        for i in range(len(current_paths)):
            if index_max_el in current_paths[i]:
                #ind = current_paths[i].index(index_max_el)
                current_paths[i].remove(index_max_el)
                if current_paths[i] not in paths_with_max_el_one:
                    paths_with_max_el_one.append(current_paths[i])
            else:
                if current_paths[i] not in paths_with_max_el_one:
                    paths_with_max_el_one.append(current_paths[i])
        # print("all_max_elements_one = " + str(all_indexes_of_max_elements_one))
        # print("paths_with_max_el_one = " + str(paths_with_max_el_one))
        k = 0
        for j in range(len(paths_with_max_el_one)):
            if len(paths_with_max_el_one[j]) == 2:
                k += 1
        if k == len(paths_with_max_el_one):
            break
        # if len(paths_with_max_el_one[0]) < 3:
        #     break
        numbers_of_max_elements = max_element(G, paths_with_max_el_one)
        index_max_el = np.argmax(numbers_of_max_elements[1:len(numbers_of_max_elements) - 1]) + 1
        value_of_repeates_max_el = np.max(numbers_of_max_elements[1:len(numbers_of_max_elements) - 1])
        if value_of_repeates_max_el > 1:
            current_paths = paths_with_max_el_one
            all_indexes_of_max_elements_one.append(index_max_el)
            paths_with_max_el_one = []
        elif value_of_repeates_max_el == 0:
            break
    return 

def secondone(G, list_asp, all_indexes_of_max_elements_zero, paths_without_first_el):
    paths_with_max_el_one = []
    all_indexes_of_max_elements_one = []
    current_paths = list_asp.copy()
    for i in range(len(all_indexes_of_max_elements_zero)):
        curr_el = all_indexes_of_max_elements_zero[i]
        for j in range(len(current_paths)):
            if curr_el in current_paths[j]:
                current_paths[j].remove(curr_el)
                if i == 0:
                    paths_with_max_el_one.append(current_paths[j])
            else:
                if i == 0:
                    paths_with_max_el_one.append(current_paths[j])
        current_paths = paths_with_max_el_one.copy()
    #     print("cur1 = " + str(current_paths))
    # print("current_path = " + str(current_paths))
    # print("paths_with_max_el_one = " + str(paths_with_max_el_one))      
    return

def secondtwo(G, list_asp, all_indexes_of_max_elements_zero, paths_without_first_el, P):
    current_paths = list_asp.copy()
    array_of_elements = []
    function = []
    all_sum = 0
    # P = 0.9
    for i in range(len(all_indexes_of_max_elements_zero) + 1):
        if i < len(all_indexes_of_max_elements_zero):
            curr_el = all_indexes_of_max_elements_zero[i]
            array_of_elements.append(curr_el)
            paths_for_p = []
            for j in range(0, len(array_of_elements)):
                if j == len(array_of_elements) - 1:
                    if j != 0: 
                        temp_path = paths_for_p.copy()
                        for p in range(len(paths_for_p)):
                            if array_of_elements[j] in paths_for_p[p]:
                                temp_path.remove(paths_for_p[p])
                    else:
                        temp_path = current_paths.copy()
                        for p in range(len(current_paths)):
                            if array_of_elements[j] in current_paths[p]:
                                temp_path.remove(current_paths[p])
                    paths_for_p = temp_path.copy()
                else:     
                    if j != 0:
                        for p in range(len(paths_for_p)):
                            if array_of_elements[j] in paths_for_p[p]:
                                paths_for_p[p].remove(array_of_elements[j])
                    else:
                        for p in range(len(current_paths)):
                            if array_of_elements[j] in current_paths[p]:
                                temp_path = current_paths[p].copy()
                                temp_path.remove(array_of_elements[j])
                                paths_for_p.append(temp_path)
                            else:
                                paths_for_p.append(current_paths[p])
            function.append(paths_for_p)
            summary = 0
            multiply = 1
            for k in range(len(function[i])):
                #summary += P**(len(function[i][k]) - 2)
                #multiply *= P**(len(function[i][k]) - 2)
                multiply *= (1 - P**(len(function[i][k]) - 2))
            #summary -= multiply
            summary *= P**(i)*(1 - P)
            all_sum += ((1 - multiply)*(P**(i)*(1 - P)))
            #all_sum += summary
            # print("summary = " + str(summary))
            # print("nazvanie_massivchika " + str(function[i]))
        else:
            paths_for_p = []
            for j in range(0, len(array_of_elements)):
                if j != 0:
                    for p in range(len(paths_for_p)):
                        if array_of_elements[j] in paths_for_p[p]:
                            paths_for_p[p].remove(array_of_elements[j])
                else:
                    for p in range(len(current_paths)):
                        if array_of_elements[j] in current_paths[p]:
                            temp_path = current_paths[p].copy()
                            temp_path.remove(array_of_elements[j])
                            paths_for_p.append(temp_path)
                        else:
                            paths_for_p.append(current_paths[p])
            function.append(paths_for_p)
            summary = 0
            multiply = 1
            for k in range(len(function[i])):
                # summary += P**(len(function[i][k]) - 2)
                multiply *= (1 - (1-P)**(len(function[i][k]) - 1))
            multiply *= P**(i)
            # all_sum += summary
            all_sum += multiply
            # print("summary2 = " + str(multiply))
            # print("nazvanie_massivchika2 " + str(function[i])) 
    all_sum = all_sum*(P**2) #+ (0.07)
    # print("all_sum = " + str(all_sum))
    return all_sum

def lvm(G, start_v, end_v):
    time_array = []
    start_tmp = time.time()
    list_asp = all_simple_paths(G, start_v, end_v)
    array_range1 = np.arange(0, 1.1, 0.1)
    values_p = []
    numbers_of_max_elements = max_element(G, list_asp)
    # zero(list_asp, numbers_of_max_elements)
    #one(list_asp, numbers_of_max_elements)
    paths_without_max_el_zero, all_indexes_of_max_elements_zero, paths_without_first_el = zero(G, list_asp, numbers_of_max_elements)
    time_tmp = time.time() - start_tmp
    #secondone(G, list_asp, all_indexes_of_max_elements_zero, paths_without_first_el)
    #secondtwo(G, list_asp, all_indexes_of_max_elements_zero, paths_without_first_el)
    #lvm(list_asp)
    for p in array_range1:
        start_time = time.time()
        values_p.append(secondtwo(G, list_asp, all_indexes_of_max_elements_zero, paths_without_first_el, p))
        time_array.append(time_tmp + time.time() - start_time)

    return values_p, array_range1, time_array


# декомпозиция ------------------------------------------------------------------------------
def decomposition():
    array_range1 = np.arange(0, 1.1, 0.1)
    values_p = []
    for p in array_range1:
        p1 = p**3 + p**3 - p**6
        p2 = (p**2 + p**2 - p**4)*(p + p - p**2)
        p3 = (p + p - p**2)*(p**2 + p**2 - p**4)
        p4 = (p + p - p**2)**3
        res = p4*p**2 + p3*(1-p)*p + p2*p*(1-p) + p1*(1-p)**2
        values_p.append(res)

    return values_p, array_range1


# ------------------------------------------------------------------------------
def simul_model_nodes(G, start_v, end_v):
    E = G.number_of_edges()
    N = G.number_of_nodes()
    eps = 0.01
    N_exp = int(9/4 * 1/eps**2)
    array_range2 = np.arange(0, 1.1, 0.1)
    values_p = []
    for p in array_range2:
        print("--------------------------")
        print("p = " + str(p))
        path_exist = 0
        if p > 0:
            for i in range(N_exp):
                SG = nx.Graph()
                SG = G.copy()
                y = np.random.sample(N)
                for j in range(len(y)):
                    if y[j] > p:
                        SG.remove_node(j)
                if has_path(SG, start_v, end_v):
                    path_exist += 1
        values_p.append(path_exist/N_exp)

    return values_p, array_range2


# ------------------------------------------------------------------------------
def brute_force_nodes_type(G, start_v, end_v):
    E = G.number_of_edges()
    N = G.number_of_nodes()
    values_p = []
    array_range1 = np.arange(0.0, 1.1, 0.1)
    SG_array = []
    SG_array.append(G)
    # print(SG_array[0].nodes)
    for n in range(N + 1):
        comb = itertools.combinations(list(G.nodes), n)
        comb_list = list(comb)
        if len(comb_list[0]) != 0:
            for sg in comb_list:
                SG = nx.Graph()
                SG = G.copy()
                for i in sg:
                    SG.remove_node(i)
                SG_array.append(SG)
                # print(SG.nodes)
    
    for p in array_range1:
        print("------------\np = " + str(p))
        p_g = 0
        for i in range(len(SG_array)):
            if has_path(SG_array[i], start_v, end_v):
                p_g += p ** (SG_array[i].number_of_nodes()) * (1-p)**(N - SG_array[i].number_of_nodes())
        values_p.append(p_g)

    return values_p, array_range1
