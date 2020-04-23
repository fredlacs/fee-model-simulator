# Define agent populations and how they are generated
# Author: Frederico Lacs

from fee_simulator.bidder import TruthfulBidAgent, GethAgent, Web3jsAgent, \
    NethereumAgent, EthGasStationAgent
from fee_simulator.auctioneer import KnapsackAuctioneerAgent
import numpy as np

def createBidderPopulation():
    """
    Generates population of bidders for simulation
    """
    # gas cost of making an eth transfer
    TX_GAS_COST = 21000

    # parameters for normal distribution
    valuation_mean = 60
    valuation_std_deviation = 10
    n_agents = 10

    # generate normal distribution of valuations
    valuations = iter(np.random.normal(valuation_mean, valuation_std_deviation, n_agents))

    # create bidder population
    bidders = [
        TruthfulBidAgent("Truthful Bid #1", next(valuations), TX_GAS_COST),
        TruthfulBidAgent("Truthful Bid #2", next(valuations), TX_GAS_COST),
        GethAgent("Geth", next(valuations), TX_GAS_COST),
        Web3jsAgent("Web3.js", next(valuations), TX_GAS_COST),
        NethereumAgent("Nethereum", next(valuations), TX_GAS_COST),
        EthGasStationAgent("EthGasStation Slow", next(valuations), TX_GAS_COST, 0),
    ]

    return bidders

def createAuctioneerPopulation():
    """
    Generates population of auctioneers for simulation
    """
    return [ KnapsackAuctioneerAgent() ]
