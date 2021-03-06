'''
    A module for time measurement of algorithms.
'''
import time
from tqdm import tqdm
import create_graph
import kruskal_algorithm
import prim_algorithm


def measure_avarage_time(algorithm, num_of_iterations: int, nodes_count: int, completeness: float):
    """
    Returns an average time taken for one iteration of algorithm to perform.
    Args:
        algorithm (_type_): an algorithm.
        num_of_iterations (int): number of iterations to perform.
        nodes_count (int): a number of nodes in graph.
        completeness (float): a completeness of a graph.
    Returns:
        float: average time.
    """
    time_taken = 0
    for _ in tqdm(range(num_of_iterations)):
        graph = create_graph.gnp_random_connected_graph(
            nodes_count, completeness, False)
        start = time.time()
        algorithm(graph)
        end = time.time()
        time_taken += end - start
    return time_taken / num_of_iterations


def show_difference():
    """
    Performs two of the algorithms and shows a difference in time between them.
    Gets all the data from standart input.
    Returns number of iterations and completeness of a graph.
    """
    print('Pls, enter the number of iterations to perform:')
    while True:
        try:
            num_of_iterations = int(input('>>> '))
            break
        except ValueError:
            print("You've made a mistake. Please, enter a correct value:")

    print("Now enter the number of graph nodes and it's competeness (separated by space):")
    while True:
        try:
            nodes_count, completeness = input('>>> ').split()
            nodes_count = int(nodes_count)
            completeness = float(completeness)
            assert 0 <= completeness <= 1
            break
        except (ValueError, AssertionError):
            print("You've made a mistake. Please, enter a correct value:")

    print('Executing Kruskal algorithm:')
    av_time1 = measure_avarage_time(
        kruskal_algorithm.kruskal_algorithm, num_of_iterations, nodes_count, completeness)
    print(f'Average time per iteration: {av_time1}')
    print('Executing Prim algorithm:')
    av_time2 = measure_avarage_time(
        prim_algorithm.prim_algorithm, num_of_iterations, nodes_count, completeness)
    print(f'Average time per iteration: {av_time2}')
    return num_of_iterations, completeness


def plot_statistics(iterations:int = 15, completeness:int = 0.5):
    """
    Plots two graphs if user wants to and returns None otherwise.
    Red and blue curves represent two 'average time'-functions of Prim
    and Kruskal algorithms, respectively.
    Args:
        iterations (int, optional): number of iterations to perform. Defaults to 15.
        completeness (int, optional): a completeness of a graph. Defaults to 0.5.
    Returns nothing.
    """
    print('Would you like to plot a graph with a statistics using pre-entered data?(Y/n)')
    answer = input('>>> ')[0]
    if answer in 'Nn':
        return None
    print('Graphing...')
    import matplotlib.pyplot as plt
    x_axes = list(range(50, 300, 50))
    # Kruskal
    kruskal_axes = [measure_avarage_time(kruskal_algorithm.kruskal_algorithm, iterations, nodes_count, completeness)
              for nodes_count in x_axes]
    plt.plot(x_axes, kruskal_axes, label = "Kruskal")
    prim_axes = [measure_avarage_time(prim_algorithm.prim_algorithm, iterations, nodes_count, completeness)
              for nodes_count in x_axes]
    plt.plot(x_axes, prim_axes, label = "Prim")

    plt.xlabel('x - number of nodes')
    plt.ylabel('y - average time')
    
    plt.title(f'A graph comparison of two algorithms ({iterations} iterations, {completeness} completeness)')

    plt.legend()
    plt.show()


def main():
    num_of_iterations, completeness = show_difference()
    plot_statistics(num_of_iterations, completeness)

if __name__ == '__main__':
    main()
