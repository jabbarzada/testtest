import os
import sys

# Add the parent directory of this file to the Python path so we can import multiply module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from multiply import multiply

def test_multiply_positive():
    assert multiply(2, 3) == 6

def test_multiply_negative():
    assert multiply(-2, 3) == -6
