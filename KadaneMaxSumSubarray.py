def max_sum_subarray(arr):
    max_so_far = max_sum = arr[0]
    n = len(arr)
    for i in range(1,n):
        max_so_far = max(arr[i], max_so_far + arr[i])
        max_sum = max(max_sum, max_so_far)
    return max_sum
    
def test_max_sum_subarray():
    assert max_sum_subarray([-2, -3, 4, -1, -2, 1, 5, -3])==7, "Kadane Max Sum Subarray is wrong"
    
print max_sum_subarray([-2, -3, 4, -1, -2, 1, 5, -3])
test_max_sum_subarray()
