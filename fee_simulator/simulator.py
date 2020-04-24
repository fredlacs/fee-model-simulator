# Author: Frederico Lacs

from fee_simulator.auction import Bid, FirstPriceAuction
from fee_simulator.population import createAuctioneerPopulation, createBidderPopulation

def simulate_auction(iterations):
    """
    Provides the main entry point for simulating auctions.
    Runs for the set number of iterations.
    """
    # create auction starting with genesis transaction of cost 1
    auction = FirstPriceAuction(prev={
            "bids": [ Bid("GenesisTx", 1, 21000, 0) ],
            "bid_history": [],
            "initial_weight_limit": 100000 # 0
        })
    auctioneers = createAuctioneerPopulation()
    bidders = createBidderPopulation()

    # Each iteration is one timestep of the simulation
    for timestep in range(iterations):
        print(f"Executing auction number {timestep+1}")

        # 3 ticks for agents to place bids
        for i in range(3):
            for bidder in bidders:
                bid = bidder.get_bid(auction.bid_history, auction.get_visible_bids(bidder), timestep)
                if bid is not None:
                    # bid[0] == value, bid[1] == weight
                    auction.add_bid(bidder.label, bid[0], bid[1], timestep)

        # execute auction after 3 rounds are given for bids to be placed
        for auctioneer in auctioneers:
            visible_bids = auction.get_visible_bids(auctioneer)
            current_weight_limit = auction.get_weight_limit()

            winning_bids = auctioneer.get_allocation_rule(visible_bids, current_weight_limit)
            total_weight = sum(bid.weight for bid in winning_bids)

            # protocol rejects proposed bids if weight exceeds limit allowed in protocol
            if(total_weight > current_weight_limit):
                print("The total weight of the bids exceeds the weight allowed")
                continue

            # execute auction's payment rule on winning bids
            # it updates the auctions state and history
            auction.apply_payment_rule(winning_bids, timestep)

    return auction.bid_history
