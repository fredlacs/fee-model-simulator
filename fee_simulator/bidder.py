# Define bidder agent and their decision making process
# Author: Frederico Lacs

class FixedBidAgent():
    """
    Agent bids a fixed value, with a fixed weight
    """

    def __init__(self, label, bid, weight):
        self.label = label
        self.fixed_bid = bid
        self.fixedWeight = weight

    def get_bid(self, bid_history, visible_bids):
        import random
        if random.random() < 0.9:
            return self.fixed_bid, self.fixedWeight



class MeanBidAgent():
    """
    Agent bids the mean of visible bids
    """

    def __init__(self, label, weight):
        self.label = label
        self.weight = weight

    def get_bid(self, bid_history, visible_bids):
        # returns mean of visible bids
        if visible_bids:
            # generator expression more memory efficient than list comprehension
            bid = sum(bid.value for bid in visible_bids) / len(visible_bids)
            return bid, self.weight
        else:
            return None

class Web3PyAgent():
    """
    Agent bids using web3
    """

    def __init__(self, label, weight=21000):
        self.label = label
        self.weight = weight
    
    def get_bid(self, visible_bids):
        # import web3py
        return 0, 0