# Define agent populations and how they are generated
# Author: Frederico Lacs

from fee_simulator.bidder import fixed_bidAgent
from fee_simulator.auctioneer import NaiveAuctioneerAgent

def createBidderPopulation():
    return [ fixed_bidAgent(5, 21000),fixed_bidAgent(3, 21000), fixed_bidAgent(7, 21000) ]

def createAuctioneerPopulation():
    return [ NaiveAuctioneerAgent() ]
