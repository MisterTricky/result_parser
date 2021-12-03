from result_parser.functions import parse_file_data
import pandas as pd


def test_parse_file_data():
    """
    Simple Test to check file handling etc.
    :return:
    """
    file_name = "/home/lukas/result_parser/test_input/test_input.txt"
    result = parse_file_data(file_name)
    assert result is not None
