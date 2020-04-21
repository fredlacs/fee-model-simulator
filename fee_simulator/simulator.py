#!/usr/bin/env python3
# Author: Frederico Lacs

from fee_simulator.auction import FirstPriceAuction
from fee_simulator.population import createAuctioneerPopulation, createBidderPopulation
import csv, click
import matplotlib.pyplot as plt


@click.command()
@click.option("--outputfile", default="results.csv", help="Simulation output filename", type=str)
@click.option('--graph', is_flag=True, help="Plot graph with simulation results")
@click.argument("iterations", type=int)
def run_auctions(outputfile, graph, iterations):
    auction = FirstPriceAuction()
    auctioneers = createAuctioneerPopulation()
    bidders = createBidderPopulation()

    csvfile = open(outputfile, 'w', newline='')
    writer = csv.writer(csvfile, dialect='excel')
    writer.writerow(["Timestep", "BidValue", "BidWeight", "CreationTimestep"])
    results = []

    # Each iteration is one timestep of the simulation
    for timestep in range(iterations):
        print(f"Executing auction number {timestep+1}")

        # 3 ticks for agents to place bids
        for bidder in bidders:
            bid, weight = bidder.get_bid(auction.get_visible_bids(bidder))
            if bid: auction.add_bid(bidder, bid, weight, timestep)

        for bidder in bidders:
            bid, weight = bidder.get_bid(auction.get_visible_bids(bidder))
            if bid: auction.add_bid(bidder, bid, weight, timestep)
        
        for bidder in bidders:
            bid, weight = bidder.get_bid(auction.get_visible_bids(bidder))
            if bid: auction.add_bid(bidder, bid, weight, timestep)

        # execute auction after 3 rounds are given for bids to be placed
        for auctioneer in auctioneers:
            visible_bids = auction.get_visible_bids(auctioneer)

            winning_bids = auctioneer.get_allocation_rule(visible_bids, auction.weight_limit)
            total_weight = sum(bid.weight for bid in winning_bids)

            if(total_weight > auction.weight_limit):
                raise AssertionError("The total weight of the bids exceeds the weight allowed")
            
            # apply auction's payment rule on winning bids
            payment_result = auction.payment_rule(winning_bids)
            # removes winning bids from current auction
            auction.remove_winning_bids(winning_bids)
            
            # store results
            for bid in winning_bids:
                writer.writerow([timestep, bid.value, bid.weight, bid.creation_timestep])
                results.append(bid)
    
    # data visualisation
    if graph:
        x = [ bid.creation_timestep+1 for bid in results ]
        y = []

        import statistics
        for timestep in results:
            average_weight_per_timestep = [ bid.weight for bid in results if bid.creation_timestep == timestep ]
            y.append(sum(average_weight_per_timestep))

        plt.plot(x, y, label='Total gas used per block')
        plt.xlabel('Timestep')
        plt.ylabel('Total Weight of winning bids')
        plt.title('Auction simulation results')
        plt.legend()

        plt.show()



if __name__ == '__main__':
    run_auctions()
