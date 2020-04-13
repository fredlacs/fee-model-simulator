#!/usr/bin/env python3
# Author: Frederico Lacs

from auction import FirstPriceAuction
from population import createAuctioneerPopulation, createBidderPopulation
import csv, click


@click.command()
@click.option("--outputfile", default="results.csv", help="Simulation output filename", type=str)
@click.argument("iterations", type=int)
def runAuctions(outputfile, iterations):
    auction = FirstPriceAuction()
    auctioneers = createAuctioneerPopulation()
    bidders = createBidderPopulation()

    csvfile = open(outputfile, 'w', newline='')
    writer = csv.writer(csvfile, dialect='excel')
    writer.writerow(["timestep", "bidValue", "bidWeight", "creationTimestep"])

    # Each iteration is one timestep of the simulation
    for timestep in range(iterations):
        print(f"Executing auction number {timestep+1}")

        # 3 ticks for agents to place bids
        for bidder in bidders:
            bid, weight = bidder.getBid(auction.getVisibleBids(bidder))
            if bid: auction.addBid(bidder, bid, weight, timestep)

        for bidder in bidders:
            bid, weight = bidder.getBid(auction.getVisibleBids(bidder))
            if bid: auction.addBid(bidder, bid, weight, timestep)
        
        for bidder in bidders:
            bid, weight = bidder.getBid(auction.getVisibleBids(bidder))
            if bid: auction.addBid(bidder, bid, weight, timestep)

        # execute auction after 3 rounds are given for bids to be placed
        for auctioneer in auctioneers:
            visibleBids = auction.getVisibleBids(auctioneer)

            winningBids = auctioneer.getAllocationRule(visibleBids, auction.weightLimit)
            totalWeight = sum(bid.weight for bid in winningBids)

            if(totalWeight > auction.weightLimit):
                raise AssertionError("The total weight of the bids exceeds the weight allowed")
            
            # apply auction's payment rule on winning bids
            paymentResult = auction.paymentRule(winningBids)
            auction.removeWinningBids(winningBids)
            
            # store results
            for res in paymentResult:
                writer.writerow([timestep, res.value, res.weight, res.creationTimestep])


if __name__ == '__main__':
    runAuctions()
