# Define agents and their decision making process
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


class RandomAuctioneerAgent(AbstractAuctioneerAgent):
    """
    Selects allocation rule randomly
    """

    def __init__(self):
        AbstractAuctioneerAgent.__init__(self)
    
    def selectWinningBids(self, bids, slots):
        """
        Selects first n slots as winning bids
        """
        return bids[:slots]


class KnapsackAuctioneerAgent(AbstractAuctioneerAgent):
    """
    Knapsack optimisation on bids, currently with weight 1 on each bid
    """

    def __init__(self):
        AbstractAuctioneerAgent.__init__(self)

    def selectWinningBids(self, bids, slots):
        # sort dictionary from highest to lowest bid then select n winners
        # winningBids = sorted(bids, key=bids.get, reverse=True)[:self.slotsPerAuction]
        # return {winner: bids[winner] for winner in winningBids}
        return super().selectWinningBids(bids, slots)


class AbstractBidderAgent:
    """
    Agent that participates in auction
    """

    def __init__(self):
        raise NotImplementedError("Not implemented")

    def getBid(self, visibleBids):
        """
        Agent does not want to bid return false
        Else return value of bid
        """
        raise NotImplementedError("Not implemented")

    # def id(self):
    #     return id(self)


class FixedBidAgent(AbstractBidderAgent):
    """
    Agent bids a fixed value 50% of the time
    """

    def __init__(self, bid):
        self.fixedBid = bid

    def getBid(self, visibleBids):
        from random import random
        return self.fixedBid # if random() < 0.5 else False


class MeanBidAgent(AbstractBidderAgent):
    """
    Agent bids the mean of visible bids
    """
    def __init__(self):
        pass

    def getBid(self, visibleBids):
        # returns mean of visible bids
        return sum(visibleBids) / len(visibleBids)


