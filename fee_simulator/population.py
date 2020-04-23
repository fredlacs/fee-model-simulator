# Define agent populations and how they are generated
# Author: Frederico Lacs

from fee_simulator.bidder import FixedBidAgent, MeanBidAgent, GethAgent
from fee_simulator.auctioneer import KnapsackAuctioneerAgent

def createBidderPopulation():
    # gas cost of making an eth transfer
    TX_GAS_COST = 21000
    bidders = [
        # MeanBidAgent(),
        FixedBidAgent("FixedBid1", 50, TX_GAS_COST),
        FixedBidAgent("FixedBid2", 80, TX_GAS_COST),
        GethAgent("Geth1", 70, TX_GAS_COST,20,60),
        GethAgent("Geth2", 40, TX_GAS_COST,20,60),
    ]

    return bidders

def createAuctioneerPopulation():
    return [ KnapsackAuctioneerAgent() ]
