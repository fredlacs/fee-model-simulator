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


CLI syntax
```bash
feesim [number of simulations] --outputfile [optional output filename] 
```

```bash
feesim 1000
feesim 1000 --outputfile results2.csv
```


## Test Cases
First install pytest
```
pip install pytest
```

Execute unit and integration tests
```
pytest
```
