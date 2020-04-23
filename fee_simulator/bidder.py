# Define bidder agent and their decision making process
# Author: Frederico Lacs
import numpy as np

class Bidder():
    """
    An agent that is able to place bids
    """

    def __init__(self, label, valuation, weight):
        self.label = label
        self.valuation = valuation
        self.weight = weight
    
    def get_bid(self, bid_history, visible_bids, curr_timestep):
        raise AssertionError("Not implemented")


class FixedBidAgent():
    """
    Agent bids a fixed value, with a fixed weight
    """

    def __init__(self, label, bid, weight):
        self.label = label
        self.fixed_bid = bid
        self.fixedWeight = weight

    def get_bid(self, bid_history, visible_bids, curr_timestep):
        import random
        if random.random() < 0.9:
            return self.fixed_bid, self.fixedWeight


class MeanBidAgent():
    """
    Agent bids the mean of visible bids
    """

    def __init__(self, label="Mean bid", weight=0):
        self.label = label
        self.weight = weight

    def get_bid(self, bid_history, visible_bids, curr_timestep):
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

    def __init__(self, label, weight):
        self.label = label
        self.weight = weight
    
    def get_bid(self, bid_history, visible_bids, curr_timestep):
        # import web3py
        return 0, 0


class GethAgent(Bidder):
    """
    Agent bids using geth gas price
    """

    def __init__(self, label, valuation, weight, n_blocks=20, percentile=60):
        Bidder.__init__(self, label, valuation, weight)
        self.n_blocks = n_blocks
        self.percentile = percentile
    
    def get_bid(self, bid_history, visible_bids, curr_timestep):
        # if not enough blocks made, only look at available ones
        n_blocks = self.n_blocks if curr_timestep - self.n_blocks > 0 else curr_timestep

        bids = [bid.value for bid in bid_history
            if bid.payment_timestep > curr_timestep - n_blocks]

        if bids:
            value = np.percentile(bids, self.percentile)
            # only place bid if the cost is smaller than valuation
            if value < self.valuation:
                return value, self.weight
        else:
            return None
