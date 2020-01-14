# Define auction
# Author: Frederico Lacs

class AuctionState:
    """
    Defines state of an auction.
    What are the current bids?
    What information about the state each agent has access to?
    """

    def __init__(self, prev=None): 
        self.bids = prev.bids if prev else {}

    def getVisibleBids(self, agent):
        """
        Return information agent has access to from the state (ie other bids and their timestamps)
        Not every agent has access to the same information on the state
        """
        # TODO: remove this error and do logic for state information
        if not agent: raise NotImplementedError("No agent supplied")
        return self.bids
    
    def addBid(self, bidder, bid):
        self.bids[bidder].append(bid)


class AuctionMechanism(AuctionState):
    """
    Defines rules of how the auction mechanism works.
    Which bids win, how much should they pay?
    """

    def __init__(self, prev=None):
        AuctionState.__init__(self, prev)

    def allocationRule(self, auctioneers, bids, slots):
        """
        Selects auctioneer to execute the auction then queries
        for its allocation rule.
        Expects auctioneer to be AbstractAuctioneerAgent
        """
        return auctioneers[0].selectWinningBids(self=auctioneers[0], bids=bids, slots=slots)

    def paymentRule(self, bids):
        """
        How much winning bids should pay.
        This is determined by the protocol and auctioneers can't change.
        """
        raise NotImplementedError("Not implemented")

    def executeAuctionRound(self, auctioneers, bidders, slots):
        """
        Executes the end to end flow of a single auction and returns
        dictionary of payments for each bidder to pay
        """
        bids = [ bidder.getBid(self.getVisibleBids(bidder)) for bidder in bidders ]
        winningBids = self.allocationRule(auctioneers, bids, slots)
        return self.paymentRule(winningBids)


class FirstPriceAuction(AuctionMechanism):
    """
    First price auction mechanism
    """

    def __init__(self, prev=None):
        AuctionMechanism.__init__(self, prev)

    def paymentRule(self, bids):
        """
        Winning bids should play price set in bid
        """
        return bids


class SecondPriceAuction(AuctionMechanism):
    """
    Second price auction mechanism
    """

    def __init__(self, prev=None):
        AuctionMechanism.__init__(self, prev)

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

