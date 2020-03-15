#!/usr/bin/env python3
# Author: Frederico Lacs

from agents import FixedBidAgent, NaiveAuctioneerAgent
from auction import FirstPriceAuction

def runAuctions(numIterations):
    auction = FirstPriceAuction()
    auctioneers = [ NaiveAuctioneerAgent() ]
    bidders = [ FixedBidAgent(5, 21000),FixedBidAgent(3, 21000), FixedBidAgent(7, 21000) ]

    for i in range(numIterations):
        print(f"Executing auction number {i+1}")

        # 3 ticks for agents to place bids
        for bidder in bidders:
            bid, weight = bidder.getBid(auction.getVisibleBids(bidder))
            if bid: auction.addBid(bidder, bid, weight)

        for bidder in bidders:
            bid, weight = bidder.getBid(auction.getVisibleBids(bidder))
            if bid: auction.addBid(bidder, bid, weight)
        
        for bidder in bidders:
            bid, weight = bidder.getBid(auction.getVisibleBids(bidder))
            if bid: auction.addBid(bidder, bid, weight)

        # execute auction after 3 rounds are given for bids to be placed
        openSlots = 20
        results = auction.executeAuctionRound(auctioneers, openSlots)


if __name__ == '__main__':
    print("starting simulations")

    numIterations = 1000
    runAuctions(numIterations)

    print("the end")
