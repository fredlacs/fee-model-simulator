# Integration tests!

from click.testing import CliRunner
from fee_simulator.cli import run


def test_different_simulation_numbers():
  runner = CliRunner()
  result = runner.invoke(run, ['5'])
  assert result.output == "Executing auction number 1\nExecuting auction number 2\nExecuting auction number 3\nExecuting auction number 4\nExecuting auction number 5\n"

  result = runner.invoke(run, ['1'])
  assert result.output == "Executing auction number 1\n"

def test_csv_output():
  runner = CliRunner()
  result = runner.invoke(run, ['1', '--outputfile', 'resultsTest.csv'])
  assert result.output == "Executing auction number 1\n"

  file = open("resultsTest.csv", 'r', newline='')
  assert "Bidder,BidValue,BidWeight,CreationTimestep,TimestepPaid" in file.read()

