#!/usr/bin/env python3
# Author: Frederico Lacs

from agents import FixedBidAgent, NaiveAuctioneerAgent
from auction import FirstPriceAuction

def runAuctions(numIterations):
    auction = FirstPriceAuction()
    auctioneers = [ NaiveAuctioneerAgent() ]
    bidders = [ FixedBidAgent(5),FixedBidAgent(3), FixedBidAgent(7) ]

    for i in range(numIterations):
        print(f"Executing auction number {i+1}")

        # 2 ticks for agents to place bids
        for bidder in bidders:
            bid = bidder.getBid(auction.getVisibleBids(bidder))
            if bid: auction.addBid(bidder, bid)

        for bidder in bidders:
            bid = bidder.getBid(auction.getVisibleBids(bidder))
            if bid: auction.addBid(bidder, bid)

        # execute auction after 2 rounds are given for bids to be placed
        openSlots = 20
        results = auction.executeAuctionRound(auctioneers, openSlots)


if __name__ == '__main__':
    print("starting simulations")

    numIterations = 5
    runAuctions(numIterations)

    print("the end")
