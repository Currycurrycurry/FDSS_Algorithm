import sys
# 391. 完美矩形
# 1、判断面积，通过完美矩形的理论坐标计算出一个理论面积，然后和 rectangles 中小矩形的实际面积和做对比。
# 2、判断顶点，points 集合中应该只剩下 4 个顶点且剩下的顶点必须都是完美矩形的理论顶点。
def isRectangleCover(rectangles) -> bool:
    points = set()
    area = 0
    for [x1, y1, x2, y2] in rectangles:
        area += (x2 - x1) * (y2 - y1)

        points.symmetric_difference_update([(x1, y1), (x1, y2), (x2, y1), (x2, y2)])

    if len(points) != 4:
        return False

    l = b = sys.maxsize
    r = t = -sys.maxsize
    for [x, y] in points:
        l = min(x, l)
        b = min(y, b)
        r = max(x, r)
        t = max(y, t)
    return (r - l) * (t - b) == area