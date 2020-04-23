#!/usr/bin/env python3
# Author: Frederico Lacs

from fee_simulator.auction import Bid, FirstPriceAuction
from fee_simulator.population import createAuctioneerPopulation, createBidderPopulation
import csv, click
import matplotlib.pyplot as plt


@click.command()
@click.option("--outputfile", default="results.csv", help="Simulation output filename", type=str)
@click.option('--graph_each', is_flag=True, help="Plot graph with simulation results labeling each agent")
@click.option('--graph_avg', is_flag=True, help="Plot graph with simulation results and avg bid price")
@click.argument("iterations", type=int)
def run_auctions(outputfile, graph_each, graph_avg, iterations):
    """
    Provides the main entry point for simulating auctions.
    Runs for the set number of iterations, outputting the results as a csv file.

    Optionally allows the results to be visualised in tables.
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
    

    # export results to csv format
    csvfile = open(outputfile, 'w', newline='')
    writer = csv.writer(csvfile, dialect='excel')
    writer.writerow(["Bidder", "BidValue", "BidWeight", "CreationTimestep", "TimestepPaid"])

    for bid in auction.bid_history:
        entry = [bid.bidder, bid.value, bid.weight, bid.creation_timestep, bid.payment_timestep]
        writer.writerow(entry)

    # display data visualisation if --graphEach flag is used on cli
    if graph_each:
        plt.title('Auction simulation results')
        plt.xlabel('Simulation Timestep')
        plt.ylabel('Price Paid per Transaction by Agent')

        for label in (bidder.label for bidder in bidders):
            x = []
            y = []

            for bid in auction.bid_history:
                if label == bid.bidder:
                    x.append(bid.payment_timestep)
                    y.append(bid.value)
            
            # add results for current label to graph plot
            plt.scatter(x, y, label=label, alpha=0.5, s=2)

        plt.legend(loc='best')
        plt.show()

    # display data visualisation if --graphAvg flag is used on cli
    if graph_avg:
        plt.title('Auction simulation results')
        plt.xlabel('Simulation Timestep')
        plt.ylabel('Average Price Paid per Transaction by Block')

        # unique timesteps in the history
        x = list(set(bid.creation_timestep for bid in auction.bid_history))
        y = []

        import statistics
        for timestep in x:
            bids_accepted = [bid.value for bid in auction.bid_history if bid.creation_timestep == timestep]
            y.append(statistics.mean(bids_accepted))

        plt.plot(x, y, label="Avg Gas Price Paid")
        plt.legend(loc='best')
        plt.show()

if __name__ == '__main__':
    run_auctions()
