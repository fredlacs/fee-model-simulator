from fee_simulator.bidder import TruthfulBidAgent, Web3jsAgent, NethereumAgent, \
    GethAgent, EthGasStationAgent, Web3jsAgent
from fee_simulator.auction import Bid


bid_history = [
    Bid("agent1", 1300, 21000, 0, 0),
    Bid("agent2", 800, 21000, 0, 0),
    Bid("agent2", 750, 21000, 0, 0),
]

visible_bids = [
    Bid("agent3", 1300, 21000, 0),
    Bid("agent4", 2000, 21000, 0),
    Bid("agent4", 2100, 21000, 0),
]


def test_truthful_bid():
    agent = TruthfulBidAgent("test", 10, 100, bid_prob=1)
    value, weight = agent.get_bid(bid_history, visible_bids, 1)
    assert value == 10


def test_web3js_bid():
    agent = Web3jsAgent("test", 20000, 100)
    value, weight = agent.get_bid(bid_history, visible_bids, 1)
    assert value == 800

def test_nethereum_bid():
    agent = NethereumAgent("test", 20000, 21000)
    value, weight = agent.get_bid(bid_history, visible_bids, 1)
    assert value == 950

def test_geth_bid():
    agent = GethAgent("test", 20000, 21000)
    value, weight = agent.get_bid(bid_history, visible_bids, 1)
    assert value ==  900.0

def test_egs_bid():
    agent = EthGasStationAgent("test", 20000, 21000, 0)
    value, weight = agent.get_bid(bid_history, visible_bids, 1)
    assert value == 785.0
