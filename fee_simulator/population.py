# Define agent populations and how they are generated
# Author: Frederico Lacs

from fee_simulator.bidder import FixedBidAgent, MeanBidAgent
from fee_simulator.auctioneer import KnapsackAuctioneerAgent

def createBidderPopulation():
    # gas cost of making an eth transfer
    TX_GAS_COST = 21000
    bidders = [
        FixedBidAgent("FixBid1", 5, TX_GAS_COST),
        FixedBidAgent("FixBid2", 3, TX_GAS_COST),
        FixedBidAgent("FixBid3", 8, TX_GAS_COST),
        MeanBidAgent("MeanBid1", TX_GAS_COST)
    ]

    return bidders

def createAuctioneerPopulation():
    return [ KnapsackAuctioneerAgent() ]
