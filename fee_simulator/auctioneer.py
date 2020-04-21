# Define auctioneer agent and their decision making process
# Author: Frederico Lacs
from ortools.algorithms import pywrapknapsack_solver

"""
Agent that selects winning bids in an auction
"""

class KnapsackAuctioneerAgent():
    """
    Knapsack optimisation on bids
    """

    def __init__(self):
        pass

    def get_allocation_rule(self, bids, weight_limit):
        """
        Selects highest bids using branch and bound optimisation technique
        """
        values = []
        weights = [[]]
        capacities = [ weight_limit ]

        for bid in bids:
            values.append(bid.value)
            # appends to the inner list
            weights[0].append(bid.weight)

        # https://developers.google.com/optimization/bin/knapsack
        # https://developers.google.com/optimization/reference/python/algorithms/pywrapknapsack_solver
        solver = pywrapknapsack_solver.KnapsackSolver(
            pywrapknapsack_solver.KnapsackSolver.
            KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackBids')

        solver.Init(values, weights, capacities)
        computed_value = solver.Solve()

        # # returns list of optimally packed indices
        selected_indices = [x for x in range(0, len(weights[0]))
                  if solver.BestSolutionContains(x)]

        # the indices are converted into their corresponding bids then returned
        return [bids[i] for i in selected_indices]
