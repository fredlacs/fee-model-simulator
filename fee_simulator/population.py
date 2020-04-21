# Define agent populations and how they are generated
# Author: Frederico Lacs

from fee_simulator.bidder import FixedBidAgent
from fee_simulator.auctioneer import KnapsackAuctioneerAgent

def createBidderPopulation():
    return [ FixedBidAgent(5, 21000),FixedBidAgent(3, 21000), FixedBidAgent(7, 21000) ]

def createAuctioneerPopulation():
    return [ KnapsackAuctioneerAgent() ]
