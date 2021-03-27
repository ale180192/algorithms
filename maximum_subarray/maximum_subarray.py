from typing import Union
import sys


def get_maximum_crossing_subarray(A: tuple, low: int, mid: int, high: int) -> Union[int, int, float]:
    """
    Return the contiguos sub array using a midpoint to saparate A into 2 subarrays.
    :param A: (tuple) array where we search the max sub array.
    :param low: (int) the low index of A where we must search.
    :param mid: (int) The mid of the array.
    :param high: (int) The high index of A where we must search.
    :return: (tuple) tuple where 3 values, the first 2 values are the
    low and high index of the maximum sub array found and the 3th value is 
    the sum maximum sub array sum.
    :rtype: Union(int, int, float)
    """
    left_sum = -sys.maxsize
    sum = 0
    index_left = mid
    for i in range(mid, low - 1, -1):
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            index_left = i

    right_sum = -sys.maxsize
    sum = 0
    index_right = mid
    for j in range(mid + 1, high + 1, 1):
        sum += A[j]
        if sum > right_sum:
            right_sum = sum
            index_right = j

    return (index_left, index_right, left_sum + right_sum)



def get_maximum_subarray(A: tuple, low: int, high: int) -> Union[int, int, float]:
    """
    Return the contiguos sub array of A whose value
    have the largest sum. This function apply the method
    divide and conquer(recursive function).
    :param A: List of integers.
    :param low: The lowest index of A.
    :param high: The highest index of A.
    :return: (tuple) tuple with the low and high index of the new sub array
    that containt the largest sum. for example for the array A=[1, 3, -5, 6, 9]
    the tuple returned will be (3, 4, 15) where 3 and 4 and the index of the subarray
    A[3:4] and the 15 is the sum of the subarray A[3:4].

    Notice that the array A must be a power size of 2 to ensure that n/2 is an integer.

    :rtype: Union[int, int, float]
    """
    if low == high:
        return (low, high, A[low])

    else:
        # -1 because the mid must be a integer, on this case mid es the low index of the two
        # indexes that its found on the middle. for example for the array A=[2,3,5,6] the low mid is de idx
        # 1 with value 3
        mid = int((low + high - 1) / 2)
        left_low, left_high, left_sum = get_maximum_subarray(A, low, mid)
        right_low, right_high, right_sum = get_maximum_subarray(A, mid + 1, high)
        cross_low, cross_high, cross_sum = get_maximum_crossing_subarray(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)

        else:
            return (cross_low, cross_high, cross_sum)
    

if __name__ == "__main__":
    """
    all the list the first element is the index 0 and the last
    index is the A.length - 1
    """
    A = [1, 3, -3, -4, -3, 3, 3, 4]
    low_index, high_index = 0, len(A) -1
    idx_low, idx_high, sum = get_maximum_subarray(A, low_index, high_index)
    max_subarray = A[idx_low:idx_high]
    print(f"the maximum sub array of {A} is {max_subarray} with the idx [{idx_low}:{idx_high}] and the sum is {sum}" )