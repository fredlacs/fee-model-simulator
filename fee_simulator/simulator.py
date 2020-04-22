#!/usr/bin/env python3
# Author: Frederico Lacs

from fee_simulator.auction import Bid, FirstPriceAuction
from fee_simulator.population import createAuctioneerPopulation, createBidderPopulation
import csv, click
import matplotlib.pyplot as plt


@click.command()
@click.option("--outputfile", default="results.csv", help="Simulation output filename", type=str)
@click.option('--graph', is_flag=True, help="Plot graph with simulation results")
@click.argument("iterations", type=int)
def run_auctions(outputfile, graph, iterations):
    # create auction starting with genesis transaction of cost 1
    auction = FirstPriceAuction(prev={
            "bids": [ Bid("GenesisTx", 1, 21000, 0) ],
            "bid_history": [],
            "initial_weight_limit": 11000000
        })
    auctioneers = createAuctioneerPopulation()
    bidders = createBidderPopulation()

    # Each iteration is one timestep of the simulation
    for timestep in range(iterations):
        print(f"Executing auction number {timestep+1}")

        # 3 ticks for agents to place bids
        for bidder in bidders:
            bid, weight = bidder.get_bid(auction.get_visible_bids(bidder))
            if bid: auction.add_bid(bidder.label, bid, weight, timestep)

        for bidder in bidders:
            bid, weight = bidder.get_bid(auction.get_visible_bids(bidder))
            if bid: auction.add_bid(bidder.label, bid, weight, timestep)
        
        for bidder in bidders:
            bid, weight = bidder.get_bid(auction.get_visible_bids(bidder))
            if bid: auction.add_bid(bidder.label, bid, weight, timestep)

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
    

    # export results to csv format
    csvfile = open(outputfile, 'w', newline='')
    writer = csv.writer(csvfile, dialect='excel')
    writer.writerow(["Bidder", "BidValue", "BidWeight", "CreationTimestep", "TimestepPaid"])

    for bid in auction.bid_history:
        entry = [bid.bidder, bid.value, bid.weight, bid.creation_timestep, bid.payment.timestep]
        writer.writerow(entry)

    # display data visualisation if --graph flag is used on cli
    if graph:
        plt.title('Auction simulation results')
        plt.xlabel('Simulation Timestep')
        plt.ylabel('Price Paid per Transaction by Agent')

        for label in [bidder.label for bidder in bidders]:
            x = []
            y = []

            for bid in auction.bid_history:
                if label == bid.bidder:
                    x.append(bid.payment.timestep)
                    y.append(bid.payment.price)
            
            # add results for current label to graph plot
            plt.plot(x, y, label=label)

        plt.legend(loc='best')
        plt.show()

if __name__ == '__main__':
    run_auctions()
