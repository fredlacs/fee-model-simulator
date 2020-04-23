# Define agent populations and how they are generated
# Author: Frederico Lacs

from fee_simulator.bidder import FixedBidAgent, GethAgent, Web3jsAgent, NethereumAgent
from fee_simulator.auctioneer import KnapsackAuctioneerAgent
import numpy as np

def createBidderPopulation():
    # gas cost of making an eth transfer
    TX_GAS_COST = 21000

    valuation_mean = 60
    valuation_std_deviation = 10
    n_agents = 10

    # set valuation normal distribution
    valuations = iter(np.random.normal(valuation_mean, valuation_std_deviation, n_agents))

    bidders = [
        FixedBidAgent("FixedBid1", next(valuations), TX_GAS_COST),
        FixedBidAgent("FixedBid2", next(valuations), TX_GAS_COST),
        GethAgent("Geth2", next(valuations), TX_GAS_COST),
        Web3jsAgent("js1", next(valuations), TX_GAS_COST),
        NethereumAgent("neth1", next(valuations), TX_GAS_COST)
    ]

    return bidders

def createAuctioneerPopulation():
    return [ KnapsackAuctioneerAgent() ]
