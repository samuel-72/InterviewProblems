def min_cost_climbing_stairs(cost):
    """
    :type cost: List[int]
    :rtype: int
    """
    n = len(cost)
    val = [0] * n
    val[0] = cost[0]
    val[1] = cost[1]
    for i in range(2, n):
        val[i] = min(cost[i] + val[i - 1], cost[i] + val[i - 2])
    return val[n - 1] if val[n - 1] < val[n - 2] else val[n - 2]

def test_min_cost_climbing_stairs():
    assert min_cost_climbing_stairs([10, 15, 20]) == 15
    assert min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
    
def main():
    test_min_cost_climbing_stairs()
    
if __name__ == "__main__":
    main()
