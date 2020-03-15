# Define agent populations and how they are generated
# Author: Frederico Lacs

from bidder import FixedBidAgent
from auctioneer import NaiveAuctioneerAgent

def createBidderPopulation():
    return [ FixedBidAgent(5, 21000),FixedBidAgent(3, 21000), FixedBidAgent(7, 21000) ]

def createAuctioneerPopulation():
    return [ NaiveAuctioneerAgent() ]