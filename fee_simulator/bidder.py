# Define bidder agent and their decision making process
# Author: Frederico Lacs
import numpy as np
import statistics

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
        if random.random() < 0.1:
            return self.fixed_bid, self.fixedWeight


class NethereumAgent(Bidder):
    """
    Agent bids using Nethereum gas price
    """

    def __init__(self, label, valuation, weight, n_blocks=100):
        Bidder.__init__(self, label, valuation, weight)
        self.n_blocks = n_blocks
    
    def get_bid(self, bid_history, visible_bids, curr_timestep):
        # if not enough blocks made, only look at available ones
        n_blocks = self.n_blocks if curr_timestep - self.n_blocks > 0 else curr_timestep

        bids = [bid.value for bid in bid_history
            if bid.payment_timestep >= curr_timestep - n_blocks]

        if bids:
            value = statistics.mean(bids)
            # only place bid if the cost is smaller than valuation
            if value < self.valuation:
                return value, self.weight
        else:
            return None


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
            if bid.payment_timestep >= curr_timestep - n_blocks]

        if bids:
            value = np.percentile(bids, self.percentile)
            # only place bid if the cost is smaller than valuation
            if value < self.valuation:
                return value, self.weight
        else:
            return None


class EthGasStationAgent(Bidder):
    """
    Agent bids using ethgasstation prediction
    """

    def __init__(self, label, valuation, weight, bid_speed, n_blocks = 200):
        Bidder.__init__(self, label, valuation, weight)
        
        if bid_speed == 0:
            self.percentile = 35 # safe low
        elif bid_speed == 1:
            self.percentile = 60 # standard
        elif bid_speed == 2:
            self.percentile = 90 # fast
        else:
            raise AssertionError("Bid speed not recognised")

        self.n_blocks = n_blocks
    
    def get_bid(self, bid_history, visible_bids, curr_timestep):
        # if not enough blocks made, only look at available ones
        n_blocks = self.n_blocks if curr_timestep - self.n_blocks > 0 else curr_timestep

        bids = [bid.value for bid in bid_history
            if bid.payment_timestep >= curr_timestep - n_blocks]

        return None


class Web3jsAgent(Bidder):
    """
    """
    def __init__(self, label, valuation, weight, n_blocks=100):
        Bidder.__init__(self, label, valuation, weight)
        self.n_blocks = n_blocks
    
    def get_bid(self, bid_history, visible_bids, curr_timestep):
        n_blocks = self.n_blocks if curr_timestep - self.n_blocks > 0 else curr_timestep

        bids = [bid.value for bid in bid_history
            if bid.payment_timestep >= curr_timestep - n_blocks]

        if bids:
            # return median of latest bids
            value = statistics.median(bids)
            # only place bid if the cost is smaller than valuation
            if value < self.valuation:
                return value, self.weight
        else:
            return None

