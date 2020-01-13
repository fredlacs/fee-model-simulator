#!/usr/bin/env python3
# Define an auction and interface of classes that interact with it
# Author: Frederico Lacs

class Agent:
    """
    Agent that participates in auction
    """

    def __init__(self):
        raise NotImplementedError("Not implemented")

    def getBid(self, visibleBids):
        """
        Agent does not want to bid return false
        Else return value of bid
        """
        raise NotImplementedError("Not implemented")


class AuctionMechanism:
    """
    Defines rules of how the auction mechanism works.
    Which bids win, how much should they pay?
    """

    def allocationRule(self, bids):
        """
        Which bids are winning
        """
        raise NotImplementedError("Not implemented")

    def paymentRule(self, bids):
        """
        How much winning bids should pay
        """
        raise NotImplementedError("Not implemented")


class AuctionState:
    """
    Defines state of current auction. What are the current bids?
    What information about the state each agent has access to?
    """

    def __init__(self, prev=None):
        if(prev):
            self.bids = prev.bids
        else:
            self.bids = {}

    def getStateInformation(self, agent):
        """
        Return information agent has access to from the state (ie other bids and their timestamps)
        Not every agent has access to the same information on the state
        """
        raise NotImplementedError("Not implemented")
