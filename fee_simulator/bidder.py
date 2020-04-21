# Define bidder agent and their decision making process
# Author: Frederico Lacs

class FixedBidAgent():
    """
    Agent bids a fixed value, with a fixed weight
    """

    def __init__(self, bid, weight):
        self.fixedBid = bid
        self.fixedWeight = weight

    def getBid(self, visibleBids):
        return self.fixedBid, self.fixedWeight


class MeanBidAgent():
    """
    Agent bids the mean of visible bids
    """

    # TODO: use np's normal distribution for weight
    def __init__(self, weight):
        self.weight = weight

    def getBid(self, visibleBids):
        # returns mean of visible bids
        bid = sum(bid.weight for bid in visibleBids) / len(visibleBids)
        return bid, self.weight
