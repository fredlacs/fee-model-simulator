# Author: Frederico Lacs
import csv, click
import matplotlib.pyplot as plt
from fee_simulator.simulator import simulate_auction

@click.command()
@click.option("--outputfile", default="results.csv", help="Simulation output filename", type=str)
@click.option('--graph_each', is_flag=True, help="Plot graph with simulation results labeling each agent")
@click.option('--graph_avg', is_flag=True, help="Plot graph with simulation results and avg bid price")
@click.argument("iterations", type=int)
def run(outputfile, graph_each, graph_avg, iterations):
    """
    A wrapper around the auction simulation to allow it to be called as a CLI application.
    Exports data into a csv file, and allows for visualisation.
    """
    # runs auction the requested number of times
    bids = simulate_auction(iterations)
    
    # export results to csv format
    csvfile = open(outputfile, 'w', newline='')
    writer = csv.writer(csvfile, dialect='excel')
    writer.writerow(["Bidder", "BidValue", "BidWeight", "CreationTimestep", "TimestepPaid"])

    for bid in bids:
        entry = [bid.bidder, bid.value, bid.weight, bid.creation_timestep, bid.payment_timestep]
        writer.writerow(entry)

    # display data visualisation if --graphEach flag is used on cli
    if graph_each:
        plt.title('Auction simulation results')
        plt.xlabel('Simulation Timestep')
        plt.ylabel('Price Paid per Transaction by Agent')

        # for each unique bidder
        for bidder in list(set([bid.bidder for bid in bids])):
            x = []
            y = []

            for bid in bids:
                if bidder == bid.bidder:
                    x.append(bid.payment_timestep)
                    y.append(bid.value)
            
            # add results for current bidder to graph plot
            plt.scatter(x, y, label=bidder, alpha=0.5, s=2)

        plt.legend(loc='best')
        plt.show()

    # display data visualisation if --graphAvg flag is used on cli
    if graph_avg:
        plt.title('Auction simulation results')
        plt.xlabel('Simulation Timestep')
        plt.ylabel('Average Price Paid per Transaction by Block')

        # unique timesteps in the history
        x = list(set(bid.creation_timestep for bid in bids))
        y = []

        import statistics
        for timestep in x:
            bids_accepted = [bid.value for bid in bids if bid.creation_timestep == timestep]
            y.append(statistics.mean(bids_accepted))

        plt.plot(x, y, label="Avg Gas Price Paid")
        plt.legend(loc='best')
        plt.show()
