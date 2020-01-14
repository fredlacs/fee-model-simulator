#!/usr/bin/env python3
# Author: Frederico Lacs

from agents import FixedBidAgent

def runSimulation(numIterations):
    for i in range(numIterations):
        print(f"Executing auction number {i}")


if __name__ == '__main__':
    print("starting simulations")

    numIterations = 5
    runSimulation(numIterations)

    # bidders = [ FixedBidAgent(5),FixedBidAgent(3), FixedBidAgent(7) ]
    # for bidder in bidders:
    #     print(bidder.getBid(None))

    print("the end")
