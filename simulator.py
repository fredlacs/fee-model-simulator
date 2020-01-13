#!/usr/bin/env python3
# Author: Frederico Lacs

def runSimulation(numIterations):
    for i in range(numIterations):
        print(f"Executing auction number {i}")


if __name__ == '__main__':
    print("starting simulations")

    numIterations = 5
    runSimulation(numIterations)

    print("the end")

