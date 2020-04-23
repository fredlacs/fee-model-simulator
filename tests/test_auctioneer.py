from fee_simulator.auctioneer import KnapsackAuctioneerAgent
from fee_simulator.auction import Bid


def test_knapsack():
    auctioneer = KnapsackAuctioneerAgent()

    bids = [
        Bid("agent3", 1300, 21000, 0),
        Bid("agent5", 1200, 21000, 0),
        Bid("agent7", 1500, 21000, 0),
    ]

    winning_bids = auctioneer.get_allocation_rule(bids, 40000)
    assert len(winning_bids) == 1
    assert winning_bids[0].bidder == "agent7"
