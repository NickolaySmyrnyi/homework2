import numpy as np


def findIntersection(line1, line2):
    matrix = np.array([line1[1] - line1[0], line2[0] - line2[1]]).T
    b = line2[0] - line1[0]
    solved = False
    dimensions = [slice(1, 3), slice(0, 3, 2), slice(0, 2)]
    for sl in dimensions:
        try:
            t, s = np.linalg.solve(matrix[sl], b[sl])
            solved = True
        except Exception as e:
            print(e)
            continue
    return line1[0]*(1-t) + line1[1]*t


def findCentroid(a, b, c, d):
    a1 = np.array(a)
    b1 = np.array(b)
    c1 = np.array(c)
    d1 = np.array(d)
    line1 = np.array([a1, c1])
    line2 = np.array([b1, d1])
    point1 = findIntersection(line1, line2)
    point2 = a1 - point1 + c1
    point3 = (b1 + d1)/2
    return point3 + (point2 - point3)/3
