# Define bidder agent and their decision making process
# Author: Frederico Lacs
import numpy as np
import statistics, random

class Bidder():
    """
    An agent that is able to place bids
    """

    def __init__(self, label, valuation, weight, bid_prob=1):
        self.label = label
        self.valuation = valuation
        self.weight = weight
        self.bid_prob = bid_prob

    def should_bid(self):
        return True if random.random() < self.bid_prob else False

    def get_bid(self, bid_history, visible_bids, curr_timestep):
        raise AssertionError("Not implemented")


class TruthfulBidAgent(Bidder):
    """
    Agent bids its valuation
    """

    def __init__(self, label, valuation, weight, bid_prob=0.1):
        Bidder.__init__(self, label, valuation, weight, bid_prob=bid_prob)

    def get_bid(self, bid_history, visible_bids, curr_timestep):
        if self.should_bid():
            return self.valuation, self.weight


class NethereumAgent(Bidder):
    """
   Agent bids using Nethereum gas price prediction
    """

    def __init__(self, label, valuation, weight, n_blocks=100):
        Bidder.__init__(self, label, valuation, weight)
        self.n_blocks = n_blocks
    
    def get_bid(self, bid_history, visible_bids, curr_timestep):
        if self.should_bid():
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
    Agent bids using Geth gas price prediction
    """

    def __init__(self, label, valuation, weight, n_blocks=20, percentile=60):
        Bidder.__init__(self, label, valuation, weight)
        self.n_blocks = n_blocks
        self.percentile = percentile
    
    def get_bid(self, bid_history, visible_bids, curr_timestep):
        if self.should_bid():
            # if not enough blocks made, only look at available ones
            n_blocks = self.n_blocks if curr_timestep - self.n_blocks > 0 else curr_timestep

            bids = [bid.value for bid in bid_history
                if bid.payment_timestep >= curr_timestep - n_blocks]

            if bids:
                value = np.percentile(bids, self.percentile)
                # only place bid if the cost is smaller than valuation
                if value < self.valuation:
                    return value, self.weight


class EthGasStationAgent(Bidder):
    """
    Agent bids using EthGasStation gas price prediction
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
        if self.should_bid():
            # if not enough blocks made, only look at available ones
            n_blocks = self.n_blocks if curr_timestep - self.n_blocks > 0 else curr_timestep

            bids = [bid.value for bid in bid_history
                if bid.payment_timestep >= curr_timestep - n_blocks]

            if bids:
                value = np.percentile(bids, self.percentile)
                if(self.percentile == 90):
                    print("heeeree")
                    print(value)
                    print(self.valuation)
                # only place bid if the cost is smaller than valuation
                if value < self.valuation:
                    return value, self.weight


class Web3jsAgent(Bidder):
    """
    Agent bids using web3js gas price prediction
    """
    def __init__(self, label, valuation, weight, n_blocks=100):
        Bidder.__init__(self, label, valuation, weight)
        self.n_blocks = n_blocks
    
    def get_bid(self, bid_history, visible_bids, curr_timestep):
        if self.should_bid():
            # if not enough blocks made, only look at available ones
            n_blocks = self.n_blocks if curr_timestep - self.n_blocks > 0 else curr_timestep

            bids = [bid.value for bid in bid_history
                if bid.payment_timestep >= curr_timestep - n_blocks]

            if bids:
                # return median of latest bids
                value = statistics.median(bids)
                # only place bid if the cost is smaller than valuation
                if value < self.valuation:
                    return value, self.weight

