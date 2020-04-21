# Define auctioneer agent and their decision making process
# Author: Frederico Lacs
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
        return bids[:3]


class KnapsackAuctioneerAgent():
    """
    Knapsack optimisation on bids, currently with weight 1 on each bid
    """

    def __init__(self):
        pass

    def get_allocation_rule(self, bids, weightLimit):
        """
        Selects highest bids
        """
        # naive approach w/o gas:
        # sort dictionary from highest to lowest bid then select n winners
        # winningBids = sorted(bids, key=bids.get, reverse=True)[:self.slotsPerAuction]
        # return {winner: bids[winner] for winner in winningBids}

        # take into account bid weights when selecting winning bids
        return super().get_allocation_rule(bids, weightLimit)
