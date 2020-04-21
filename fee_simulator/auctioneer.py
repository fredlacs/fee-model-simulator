# Define auctioneer agent and their decision making process
# Author: Frederico Lacs
from ortools.algorithms import pywrapknapsack_solver

"""
Agent that selects winning bids in an auction
"""

class NaiveAuctioneerAgent():
    """
    Selects allocation rule naively, without optimising revenue
    """

    def __init__(self):
        pass
    
    def get_allocation_rule(self, bids, weightLimit):
        """
        Return winning bids.
        This is the allocation rule.

        Selects first 3 bids as winning bids
        """
        # naive approach w/o gas:
        # sort dictionary from highest to lowest bid then select n winners
        # winningBids = sorted(bids, key=bids.get, reverse=True)[:self.slotsPerAuction]
        # return {winner: bids[winner] for winner in winningBids}

        # take into account bid weights when selecting winning bids
        return bids[:3]


class KnapsackAuctioneerAgent():
    """
    Knapsack optimisation on bids, currently with weight 1 on each bid
    """

    def __init__(self):
        pass

    def get_allocation_rule(self, bids, weight_limit):
        """
        Selects highest bids
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
