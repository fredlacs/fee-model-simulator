#!/usr/bin/env python3
# Author: Frederico Lacs

from agents import FixedBidAgent, NaiveAuctioneerAgent
from auction import FirstPriceAuction

def runAuctions(numIterations):
    auction = FirstPriceAuction()
    auctioneers = [ NaiveAuctioneerAgent ]
    bidders = [ FixedBidAgent(5),FixedBidAgent(3), FixedBidAgent(7) ]

    for i in range(numIterations):
        print(f"Executing auction number {i+1}")

        # 2 ticks to place bids
        for bidder in bidders:
            auction.addBid(bidder, bidder.getBid(auction.getVisibleBids(bidder)))

        for bidder in bidders:
            auction.addBid(bidder, bidder.getBid(auction.getVisibleBids(bidder)))

        # auction executed and closed
        # print(auction.bids)
        results = auction.executeAuctionRound(auctioneers, 20)
        # print(auction.bids)
        # print(results)


if __name__ == '__main__':
    print("starting simulations")

    numIterations = 5
    runAuctions(numIterations)

    # bidders = [  ]
    # for bidder in bidders:
    #     print(bidder.getBid(None))

    print("the end")
