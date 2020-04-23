# Ethereum Fee Model Simulator

Tested on Python 3.7.7

How to run simulations

Create a Python virtual envirtonment to have a clean set of dependencies
```
python3 -m venv env
```

Activate the virtual envirtonment created
```
source env/bin/activate
```

Install the CLI application
```
python3 setup.py install
```

Run simulations:
```bash
feesim 1000
feesim 1000 --graph_each
feesim 1000 --graph_avg
feesim 1000 --outputfile results2.csv
```

The --graph_each flag allows you to visualise all bids in a graph.
The --graph_avg flag allows you to visualise the avg bid per auction in a graph.

## Test Cases
First install pytest
```
pip install pytest
```

Execute unit and integration tests
```
pytest
```
