# Define auctioneer agent and their decision making process
# Author: Frederico Lacs

class AbstractAuctioneerAgent:
    """
    Agent that decides on the winning bids
    """

    def __init__(self):
        raise NotImplementedError("Not implemented")

    def selectWinningBids(self, bids, slots):
        """
        Return winning bids.
        This is the allocation rule.
        """
        raise NotImplementedError("Not implemented")


class NaiveAuctioneerAgent(AbstractAuctioneerAgent):
    """
    Selects allocation rule naively, without optimising revenue
    """

    def __init__(self):
        # AbstractAuctioneerAgent.__init__(self)
        pass
    
    def selectWinningBids(self, bids, slots):
        """
        Selects first n bids as winning bids
        """
        return bids[:slots]


class KnapsackAuctioneerAgent(AbstractAuctioneerAgent):
    """
    Knapsack optimisation on bids, currently with weight 1 on each bid
    """

    def __init__(self):
        AbstractAuctioneerAgent.__init__(self)

    def selectWinningBids(self, bids, slots):
        """
        Selects highest bids
        """
        # naive approach w/o gas:
        # sort dictionary from highest to lowest bid then select n winners
        # winningBids = sorted(bids, key=bids.get, reverse=True)[:self.slotsPerAuction]
        # return {winner: bids[winner] for winner in winningBids}

        # take into account bid weights when selecting winning bids
        return super().selectWinningBids(bids, slots)
