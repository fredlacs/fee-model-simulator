# Define auction
# Author: Frederico Lacs

class Bid:
    def __init__(self, bidder, value, weight, creationTimestep):
        # Storing as a tuple may be more efficient?
        # 2d arrays will scale better when running many simulations

        # agent who placed the bid, an Ethereum externally owned account
        self.bidder = bidder
        # the transaction fee paid by bidder (gasprice * gas used)
        self.value = value
        # amount of gas used by the transaction
        self.weight = weight
        # timestep in which bid was created
        self.creationTimestep = creationTimestep
        # if payment, payment == (timestep from win, payment price)
        self.payment = False


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
        self.bidHistory = prev["bidHistory"] if prev else []
        # weight limit of bids allowed per auction
        self.weightLimit = prev["weightLimit"] if prev else 11000000

    def getVisibleBids(self, agent):
        """
        Return information agent has access to from the state (ie other bids and their timestamps)
        Not every agent has access to the same information on the state
        """
        # TODO: logic for state information
        return self.bids

    def addBid(self, bidder, bid, weight, creationTimestep):
        # Double check this is a pass by reference
        self.bids.append(Bid(bidder, bid, weight, creationTimestep))

    def removeWinningBids(self, winningBids):
        self.bids = [item for item in self.bids if item not in winningBids]



class FirstPriceAuction(AuctionState):
    """
    First price auction payment rule
    """

    def __init__(self, prev=None):
        AuctionState.__init__(self, prev)

    def paymentRule(self, winningBids):
        """
        Closes the auction and returns dictionary
        of payments for each winning bidder to pay
        """
        # winning bids pay the value they set in First Price Auctions
        # so the values don't need to be changed
        return winningBids


class SecondPriceAuction(AuctionState):
    """
    Second price auction payment rule
    """

    def __init__(self, prev=None):
        AuctionState.__init__(self, prev)

    def paymentRule(self, bids):
        """
        Winning bids should play price set in bid
        """
        # sort dictionary from highest to lowest bid
        # sortedBidders = sorted(bids, key=bids.get, reverse=True)
        # shift every bid to the one lower
        # use iter's __next__
        # return sortedBidders
        return super().paymentRule(bids)

