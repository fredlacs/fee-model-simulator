# Define agent populations and how they are generated
# Author: Frederico Lacs

from fee_simulator.bidder import FixedBidAgent, GethAgent, Web3jsAgent, NethereumAgent
from fee_simulator.auctioneer import KnapsackAuctioneerAgent

def createBidderPopulation():
    # gas cost of making an eth transfer
    TX_GAS_COST = 21000
    bidders = [
        FixedBidAgent("FixedBid1", 50, TX_GAS_COST),
        FixedBidAgent("FixedBid2", 80, TX_GAS_COST),
        GethAgent("Geth2", 90, TX_GAS_COST),
        Web3jsAgent("js1", 90, TX_GAS_COST),
        NethereumAgent("neth1", 90, TX_GAS_COST)
    ]

    return bidders

def createAuctioneerPopulation():
    return [ KnapsackAuctioneerAgent() ]
