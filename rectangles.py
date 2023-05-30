# https://www.youtube.com/watch?v=EuPSibuIKIg\
#
def count_rectangles(coords):
    # Return number of rectangles (with vertical/horizontal sides) that can be
    # formed from list of 2D points `coords`.

    # Convert to a set of complex points for convenient vector addition and
    # efficient membership checks
    coords = {a + b * 1j for a, b in coords}

    # O(M^2N^2)

    n_rectangles = 0
    for point in coords:
        # Find rectangles of which this is the top-left point
        n_rectangles += _count_rectangles_with_top_left_at(point, coords)
    return n_rectangles


def _count_rectangles_with_top_left_at(point, coords):
    # We seek a point below and a point to the right, such that their vector sum
    # is also a point.
    n_rectangles = 0
    a, b = point
    for i in range(a, NROWS):
        if i + b not in coords:
            continue
        for j in range(int(b.imag), NCOLS):
            if a + j * 1j not in coords:
                continue
            if i + j * 1j in coords:
                n_rectangles += 1
    return n_rectangles
