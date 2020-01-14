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
        results = auction.executeAuctionRound(auctioneers, bidders, 10)
        print(results)


if __name__ == '__main__':
    print("starting simulations")

    numIterations = 5
    runAuctions(numIterations)

    # bidders = [  ]
    # for bidder in bidders:
    #     print(bidder.getBid(None))

    print("the end")
