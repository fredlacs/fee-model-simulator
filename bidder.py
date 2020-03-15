# Define bidder agent and their decision making process
# Author: Frederico Lacs

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
