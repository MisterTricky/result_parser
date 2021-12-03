<h1>Results Parser</h1>

A simple cli to parse input file with League Game Results

The project was built with python 3.9, and is compatible with python>=3.6,
and was packaged with flit.

To test locally do the following:
1) Clone the repo
2) cd ~/results_parser
3) sudo python3.9 -m pip install -e .
4) In terminal:
   1) python3.9 -m results_parser --file ~/results_parser/test_input/test_input.txt (You can specify
      your own file/directory)
5) The Results table should print to stdout.

Test are run with pytest:

1) cd into the dir where you cloned the repo
2) run pytest.

** The test is very simple, and simply verifies that the result from the parsed file is not Empty or None.
** since the spec states that input will not be malformed, I decided not to waste time.