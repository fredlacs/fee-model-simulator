# Define auction
# Author: Frederico Lacs

class AuctionMechanism:
    """
    Defines rules of how the auction mechanism works.
    Which bids win, how much should they pay?
    """

    def __init__(self):
        pass

    def allocationRule(self, auctioneers, bids, slots):
        """
        Selects first auctioneer from list and queries for the allocation.
        Expects auctioneer to be AbstractAuctioneerAgent
        """
        return auctioneers[0].selectWinningBids(bids, slots)

    def paymentRule(self, bids):
        """
        How much winning bids should pay.
        This is determined by the protocol and auctioneers can't change.
        """
        raise NotImplementedError("Not implemented")


class AuctionState:
    """
    Defines state of current auction. What are the current bids?
    What information about the state each agent has access to?
    """

    def __init__(self, prev=None): 
        self.bids = prev.bids if prev else {}

    def getStateInformation(self, agent):
        """
        Return information agent has access to from the state (ie other bids and their timestamps)
        Not every agent has access to the same information on the state
        """
        raise NotImplementedError("Not implemented")


class FirstPriceAuction(AuctionMechanism, AuctionState):
    """
    First price auction mechanism
    """

    def __init__(self, prev=None):
        AuctionMechanism.__init__(self)
        AuctionState.__init__(self, prev)

    def paymentRule(self, bids):
        """
        Winning bids should play price set in bid
        """
        return bids


class SecondPriceAuction(AuctionMechanism, AuctionState):
    """
    Second price auction mechanism
    """

    def __init__(self, prev=None):
        AuctionMechanism.__init__(self)
        AuctionState.__init__(self, prev)

    def paymentRule(self, bids):
        """
        Winning bids should play price set in bid
        """
        # sort dictionary from highest to lowest bid
        # sortedBidders = sorted(bids, key=bids.get, reverse=True)
        # shift every bid to the one lower
        # return sortedBidders
        return super().paymentRule(bids)

