"""
Given some points in cartesian coordinate, (X, Y) find the number of rectangles that can be created
by those points.
Take into consideration only the rectangles that are parallel with the X, Y axes.
"""


def countRectangles(points):
    """
    :param points: list of tuples, each tuple is a point in cartesian coordinate
    :return: number of rectangles that can be created by those points
    """
    """
    # my approach is to use the diagonal of a rectangle to find the other two points
    # and then check if the other two points are in the list of points
    (x1,y2)---------(x2,y2)
         | *        |
         |  *       | 
         |   *      |
         |    *     |
         |     *    | 
         |      *   | 
         |       *  | 
    (x1,y1)---------(x2,y1)
    """
    rectangles = 0
    points_set = set(points)  # to make the search for a point faster we convert the list to a set

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            # take two points from the list
            p1 = points[i]
            p2 = points[j]
            # check if the points can form a diagonal of a rectangle, if not move to the next pair of points
            if p1[0] == p2[0] or p1[1] == p2[1]:
                continue

            # check if the other two points are in the list of points and if they are, increment the number of rectangles
            p3 = (p1[0], p2[1])
            p4 = (p2[0], p1[1])
            if p3 in points_set and p4 in points_set:
                rectangles += 1

    return rectangles // 2  # each rectangle is counted twice because we are checking each pair of points twice, so we divide by 2


if __name__ == '__main__':
    points1 = [(1, 1), (1, 3), (2, 1), (3, 1), (3, 3)]
    points2 = [(1, 1), (1, 3), (2, 1), (2, 3), (3, 1), (3, 3)]
    points3 = [(1, 1), (1, 3), (2, 1), (2, 3), (3, 1), (3, 3), (2, 4), (3, 4)]
    print(countRectangles(points1))
    print(countRectangles(points2))
    print(countRectangles(points3))
