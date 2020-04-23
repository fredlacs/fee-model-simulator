# Define auction
# Author: Frederico Lacs

from collections import namedtuple
Payment = namedtuple("Payment", ["timestep", "price"])


class Bid:
    def __init__(self, bidder, value, weight, creation_timestep, payment_timestep=None):
        # TODO: exploring if storing as a tuple may be more efficient
        # 2d arrays will scale better when running many simulations
        if value < 0: raise AssertionError("Bids can't have a negative value")

        # agent who placed the bid, an Ethereum externally owned account
        self.bidder = bidder
        # the gas price set on an Ethereum transaction
        self.value = value
        # amount of gas used by the transaction
        self.weight = weight
        # timestep in which bid was created
        self.creation_timestep = creation_timestep
        # variable is set to timestep when auction executes this payment 
        self.payment_timestep = payment_timestep

        """Interesting to keep track of paid value if different payment rules 
        are implemented in a First Price Auction, paid value == bid value"""
        # self.payment_value = payment_value


class AuctionState:
    """
    Defines state of an auction.
    What are the current bids?
    What information about the state each agent has access to?
    """

    def __init__(self, prev=None): 
        # TODO: store in a numpy array?
        # bids to current open auction
        self.bids = prev["bids"] if prev else []
        # bids that already won an auction
        self.bid_history = prev["bid_history"] if prev else []
        # weight limit of bids allowed per auction
        self.initial_weight_limit = prev["initial_weight_limit"] if prev else 11000000

    def get_visible_bids(self, agent):
        """
        Return information agent has access to from the state (ie other bids and their timestamps)
        Not every agent has access to the same information on the state
        """
        # TODO: logic for state information
        return self.bids

    def add_bid(self, bidder, bid, weight, creation_timestep):
        # Double check this is a pass by reference
        self.bids.append(Bid(bidder, bid, weight, creation_timestep))
    
    
    def get_weight_limit(self):
        # this value may change over time
        current_weight_limit = self.initial_weight_limit
        return current_weight_limit



class FirstPriceAuction(AuctionState):
    """
    First price auction payment rule
    """

    def __init__(self, prev=None):
        AuctionState.__init__(self, prev)

    def apply_payment_rule(self, winning_bids, current_timestep):
        """
        Closes the auction and executes payments for each winning bidder
        """
        # winning bids pay the value they set in First Price Auctions
        # so the values don't need to be changed
        for bid in winning_bids:
            bid.payment_timestep = current_timestep
        
        # remove winning bids from mempool
        self.bids = [item for item in self.bids if item not in winning_bids]
        # add bids to auction history
        self.bid_history.extend(winning_bids)


# class SecondPriceAuction(AuctionState):
#     """
#     Second price auction payment rule
#     """

#     def __init__(self, prev=None):
#         AuctionState.__init__(self, prev)

#     def apply_payment_rule(self, bids):
#         """
#         Winning bids should play price set in bid
#         """
#         # sort dictionary from highest to lowest bid
#         # sortedBidders = sorted(bids, key=bids.get, reverse=True)
#         # shift every bid to the one lower
#         # use iter's __next__
#         # return sortedBidders
#         return super().apply_payment_rule(bids)
