# Author: Xinshuo Weng
# email: xinshuo.weng@gmail.com
import numpy as np, pytest

import init_paths
from check import isinteger, isfloat

def test_isinteger():
	input_test = 1
	assert isinteger(input_test)
	input_test = (1)			# tuple with length 1 is not a tuple
	assert isinteger(input_test)
	input_test = True
	assert isinteger(input_test)

	input_test = 1.5
	assert isinteger(input_test) is False
	input_test = 1e-10
	assert isinteger(input_test) is False
	input_test = {'a':1}
	assert isinteger(input_test) is False
	input_test = [1]
	assert isinteger(input_test) is False
	input_test = (1, 2)
	assert isinteger(input_test) is False
	input_test = 'sss'
	assert isinteger(input_test) is False
	input_test = np.array([1]).astype('bool')
	assert isinteger(input_test) is False

def test_isfloat():
	pass

def test_ispositiveinteger():
	pass

def test_isnonnegativeinteger():
	pass

def test_isuintnparray():
	pass

def test_isfloatnparray():
	pass

def test_isnannparray():
	pass

if __name__ == '__main__':
	pytest.main([__file__])