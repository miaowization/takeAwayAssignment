# -*- coding: utf-8 -*-
from os.path import exists, join, split, splitext
import json


def _get_trace_data(item):
    """This method makes path to test data json file depending on test case location.
    If test case has relative path 'tests/test_case'
    then json file with test data should have path resources/tests/test_case"""
    dir_, py_file = split(item.location[0])
    dir_ = join('resources', dir_)
    json_file = join(dir_, f'{splitext(py_file)[0]}.json')
    test_method = item.originalname or item.location[2]

    return dir_, json_file, test_method


def get_test_data(item):
    """This method tries to extract dictionary with test data from path"""
    _, json_file, test_method = _get_trace_data(item)
    if not exists(json_file):
        return {}

    with open(json_file, 'r', encoding='utf-8') as file:
        try:
            json_data = json.load(file)
            return json_data[test_method]
        except json.JSONDecodeError:
            raise TestDataException('Unable to read test data from '
                                    f'"{json_file}" for '
                                    f'test method {test_method}.')
        except KeyError:
            return {}


class TestDataException(Exception):
    pass
