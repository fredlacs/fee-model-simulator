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


class FixedBidAgent(AbstractBidderAgent):
    """
    Agent bids a fixed value, with a fixed weight
    """

    def __init__(self, bid, weight):
        self.fixedBid = bid
        self.fixedWeight = weight

    def getBid(self, visibleBids):
        return self.fixedBid, self.fixedWeight


class MeanBidAgent(AbstractBidderAgent):
    """
    Agent bids the mean of visible bids
    """

    # TODO: use np's normal distribution for weight
    def __init__(self, weight):
        self.weight = weight

    def getBid(self, visibleBids):
        # returns mean of visible bids
        bid = sum(visibleBids) / len(visibleBids)
        return bid, self.weight


