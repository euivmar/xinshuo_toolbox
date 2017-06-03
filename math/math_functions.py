# Author: Xinshuo Weng
# email: xinshuo.weng@gmail.com
import math
import numpy as np
from numpy.testing import assert_almost_equal

import __init__paths__
from check import *

################################################################## 2d geometry ##################################################################
# TODO: check
def get_line(pts, slope, debug=True):
    '''
    # slope is the angle in degree, this function takes a point and a
    '''
    if debug:
        print('debug mode is on during get_line function. Please turn off after debuging')
        assert is2dpts(pts), 'point is not correct'

    if slope == 90 or -90:
        slope = slope + 0.00001
    slope = math.tan(math.radians(slope))
    if debug:
        print('slope is ' + str(slope))
    dividor = slope * pts[0] - pts[1]
    if dividor == 0:
        dividor += 0.00001
    b = 1.0 / dividor
    a = -b * slope
    if debug:
        assert_almost_equal(pts[0]*a + pts[1]*b + 1, 0, err_msg='Point is not on the line')
    return np.array([a, b, 1], dtype=float)

# TODO: check
def get_slope(pts1, pts2, debug=True):
    if debug:
        print('debug mode is on during get_slope function. Please turn off after debuging')
        assert is2dpts(pts1), 'point is not correct'
        assert is2dpts(pts2), 'point is not correct'

    slope = (pts1[1] - pts2[1]) / (pts1[0] - pts2[0])
    slope = np.arctan(slope)
    slope = math.degrees(slope)
    return slope

# TODO: check
def get_intersection(line1, line2, debug=True):
    if debug:
        print('debug mode is on during get_intersection function. Please turn off after debuging')
        assert is2dline(line1), 'line is not correct'
        assert is2dline(line2), 'line is not correct'
    
    a1 = line1[0]
    b1 = line1[1]
    a2 = line2[0]
    b2 = line2[1]
    dividor = a2 * b1 - a1 * b2
    if dividor == 0:
        dividor += 0.00001
    y = (a1 - a2) / dividor
    if a1 == 0:
        a1 += 0.00001
    x = (-1.0 - b1 * y) / a1

    if debug:
        assert_almost_equal(x*line1[0] + y*line1[1] + 1, 0, err_msg='Intersection point is not on the line')
        assert_almost_equal(x*line2[0] + y*line2[1] + 1, 0, err_msg='Intersection point is not on the line')
    return np.array([x, y], dtype=float)

def pts_euclidean(pts1, pts2, debug=True):
    '''
    calculate the euclidean distance of two sets of points

    parameter:
        pts1, pts2: 2 x N or (2, ) numpy array, (x, y)

    return
        average euclidean distance
    '''
    if debug:
        assert is2dptsarray(pts1) and is2dptsarray(pts2), 'the input points are not correct'
        assert pts1.shape == pts2.shape, 'shape of two points is not equal'
        if len(pts1.shape) > 1:
            assert len(pts1.shape) == 2 and pts1.shape[1] > 0, 'shape of input points is not correct'
    
    # if the shape of input points is (2, ), reshape them to (2, 1)
    if len(pts1.shape) == 1:
        pts1 = np.reshape(pts1, (2, 1))
        pts2 = np.reshape(pts2, (2, 1))

    # calculate the distance
    num_pts = pts1.shape[1]
    ave_euclidean = 0
    for pts_index in xrange(num_pts):
        pts1_tmp = pts1[:, pts_index]
        pts2_tmp = pts2[:, pts_index]
        ave_euclidean += math.sqrt((pts1_tmp[0] - pts2_tmp[0])**2 + (pts1_tmp[1] - pts2_tmp[1])**2)
    ave_euclidean = ave_euclidean / float(num_pts)
    return ave_euclidean

################################################################## coordinates ##################################################################
def cart2pol_2d_degree(pts, debug=True):
    '''
    input a 2d point and convert to polar coordinate

    return for degree: [0, 360)
    '''
    if debug:
        assert istuple(pts) or islist(pts) or isnparray(pts), 'input point is not correct'
        assert np.array(pts).size == 2, 'input point is not 2d points'

    x = pts[0]
    y = pts[1]
    rho = np.sqrt(x**2 + y**2)
    phi = math.degrees(np.arctan2(y, x))
    while phi < 0:
        phi += 360
    while phi >= 360.:
        phi -= 360
        
    return (rho, phi)

def pol2cart_2d_degree(pts, debug=True):
    '''
    input point: (rho, phi)

    phi is in degree
    '''
    if debug:
        assert istuple(pts) or islist(pts) or isnparray(pts), 'input point is not correct'
        assert np.array(pts).size == 2, 'input point is not 2d points'

    rho = pts[0]
    phi = math.radians(pts[1])
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return (x, y)