from fee_simulator.knapsack import knapsack_dp

def test_knapsack_values():
    values = [2,3,4]
    weights = [1,1,1]
    n_items = 3
    capacity = 1
    picks = knapsack_dp(values,weights,n_items,capacity)
    assert picks == [2]

    values = [100,10,101,20,40,40]
    weights = [90,11,100,20,20,30]
    n_items = 6
    capacity = 100
    picks = knapsack_dp(values,weights,n_items,capacity)
    assert picks == [1, 3, 4, 5]

    values = [100,10,101,20,35,35]
    weights = [90,11,100,20,20,30]
    n_items = 6
    capacity = 100
    picks = knapsack_dp(values,weights,n_items,capacity)
    assert picks == [2]
