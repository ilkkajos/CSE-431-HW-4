from Hybrid import merge_sort, insertion_sort, hybrid_sort
from matplotlib import pyplot  # To Install: type 'pip install matplotlib' into the Terminal
import numpy  # To Install: type 'pip install numpy' into the Terminal
import time
import random


def plot():
    """
    Plots the time to run three sorting algorithms:
        - Student written merge sort
        - Student written insertion sort
    """
    random.seed(331)

    merge_sort_times = []
    insertion_sort_times = []
    hybrid_sort_times = []

    n = []

    for i in range(1, 11):
        """
        Student can change this to sort different length lists
        
        NOTE: small lists (i.e. lists with length < 100) will have a sort
        time of 0. Do not recommend.  
        """
        n_val = i * 10
        n.append(n_val)
        data_set = [random.randint(0, 100000) for _ in range(n_val)]

        """
        Do NOT change anything below unless you are confident in pyplot
        """

        # Sort the data using merge sort
        data_copy = data_set[:]
        merge_start_time = time.time()
        merge_sort(data_copy)
        merge_end_time = time.time()
        merge_sort_times.append(numpy.float(merge_end_time - merge_start_time))

        # Sort the data using insertion sort
        data_copy = data_set[:]
        insert_start_time = time.time()
        insertion_sort(data_copy)
        insert_end_time = time.time()
        insertion_sort_times.append(numpy.float(insert_end_time - insert_start_time))

        data_copy = data_set[:]
        hybrid_start_time = time.time()
        hybrid_sort(data_copy, threshold=100)
        hybrid_end_time = time.time()
        hybrid_sort_times.append(numpy.float(hybrid_end_time - hybrid_start_time))



    pyplot.title('Time to Sort ')
    pyplot.xlabel('Elements to be Sorted')
    pyplot.ylabel('Time to Run')

    merge, = pyplot.plot(n, merge_sort_times, 'b', label='Merge Sort')
    insertion, = pyplot.plot(n, insertion_sort_times, 'g', label='Insertion Sort')
    hybrid, = pyplot.plot(n, hybrid_sort_times,'r', label ='Hybrid Sort')
    pyplot.legend(handles=[insertion, merge, hybrid], frameon=False, title='Sorting Algorithms')

    pyplot.show()


plot()
