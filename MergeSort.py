#########################################################################################
# Recursive implementation of MergeSort algorithm.
# Mark Barros - BID 013884117
# CS3310 - Design and Analysis of Algorithms
# Cal Poly Pomona: Spring 2021
#########################################################################################

# These are imported modules. ------------------------------------------------
import random
import time

# These are global variables. ------------------------------------------------
n = 100000                  # n is the number of integers in an array.
start = 0                   # start is the "time" when an iteration of
                            # mergeSort begins.
finish = 0                  # finish is the "time" when an iteration of
                            # mergeSort ends.
period = 0                  # period is the amount of time, in seconds, that
                            # mergerSort took to complete an iteration.

# This is the Merge Sort function. -------------------------------------------
def mergeSort(array):
    if len(array) > 1:
        # This finds the middle of the array.
        mid = len(array)//2
 
        # This divides the array elements
        # into two halves.
        Left = array[:mid]
        Right = array[mid:]
 
        # This sorts both halves.
        mergeSort(Left)
        mergeSort(Right)
 
        i = j = k = 0
 
        # This copies the data to temporary arrays.
        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                array[k] = Left[i]
                i += 1
            else:
                array[k] = Right[j]
                j += 1
            k += 1
 
        # This checks if any element was left.
        while i < len(Left):
            array[k] = Left[i]
            i += 1
            k += 1
 
        while j < len(Right):
            array[k] = Right[j]
            j += 1
            k += 1

# This is the driver code. ---------------------------------------------------

if __name__ == '__main__':

    while n <= 2000000:
        integerList = random.sample(range(0, n), n)

        # Uncomment the following line to print an unsorted list.
        # print(integerList) 
        
        # This performs a merge sort and times the operation.
        start = time.perf_counter_ns()
        mergeSort(integerList)
        finish = time.perf_counter_ns()

        # This calculates the elapsed time in seconds.
        period = ((finish - start) * (10**-9))

        # This outputs to the screen the number of elements that were
        # sorted and the corresponding time it took to sort them.
        print("For n = ", f'{n:9,}', " t = ", f'{period:.3}')

        # Uncomment the following line to print a sorted list.
        # print(integerList)

        n += 100000
#########################################################################################