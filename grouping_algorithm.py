UNEVEN_PENALTY = 5

class Cost:
    def __init__(self, num_connections, uneven_cost):
        self.num_connections = num_connections
        self.uneven_cost = uneven_cost

class AlgorithmSolution:
    def __init__(self, group_a, group_b, cost: Cost):
        self.group_a = group_a
        self.group_b = group_b
        self.cost = cost

def split_into_groups(adjacency_matrix, size):
    """
    Splits a matrix into two groups with minimal connection between groups.
    """
    print('Using naive algorithm to split matrix into two groups with minimal connections.')
    print('Press CTRL-D at any point to stop.\n')

    component_group_A = []
    component_group_B = []
    current_solution_groups = []
    current_cost: Cost = None
    current_solution: AlgorithmSolution = None
    iteration = 0

    # Initially, separate graph into two non-optimized groups
    for i in range(0, size):
        if len(component_group_A) >= (int(size / 2)):
            component_group_B.append(i)
        else:
            component_group_A.append(i)
    
    current_solution_groups = [component_group_A, component_group_B]

    # Get the cost and create Solution object 
    current_cost = calculate_cost(adjacency_matrix, current_solution_groups)
    current_solution = AlgorithmSolution(current_solution_groups[0], current_solution_groups[1], current_cost)

    print("Iteration {}".format(iteration))
    print("Cost due to unevenness: {}\nNumber of connections: {}\n".format(current_cost.uneven_cost, current_cost.num_connections))

def calculate_cost(adjacency_matrix, node_groups):
    num_connections = 0

    for i in node_groups[0]:
        for j in node_groups[1]:
            if adjacency_matrix[i][j] != 0:
                num_connections += 1

    uneven_cost = UNEVEN_PENALTY * abs(len(node_groups[0]) - len(node_groups[1]))
    return Cost(num_connections, uneven_cost)
