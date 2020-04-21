# Define bidder agent and their decision making process
# Author: Frederico Lacs

class FixedBidAgent():
    """
    Agent bids a fixed value, with a fixed weight
    """

    def __init__(self, bid, weight):
        self.fixed_bid = bid
        self.fixedWeight = weight

    def get_bid(self, visibleBids):
        return self.fixed_bid, self.fixedWeight


class MeanBidAgent():
    """
    Agent bids the mean of visible bids
    """

    # TODO: use np's normal distribution for weight
    def __init__(self, weight):
        self.weight = weight

    def get_bid(self, visibleBids):
        # returns mean of visible bids
        bid = sum(bid.weight for bid in visibleBids) / len(visibleBids)
        return bid, self.weight
