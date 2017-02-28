class ShapeError(Exception):
    pass


m = [3, 4]
n = [5, 0]

v = [1, 3, 0]
w = [0, 2, 4]
u = [1, 1, 1]
y = [10, 20, 30]
z = [0, 0, 0]


def are_equal(x, y, tolerance=0.001):
    """Helper function to compare floats, which are often not quite equal."""
    return abs(x - y) <= tolerance


def shape(v):
    """shape takes a vector or matrix and return a tuple with the
    number of rows (for a vector) or the number of rows and columns
    (for a matrix.)"""
    return ((len(v), ))


def vector_add(vect1, vect2):
    """
    [a b]  + [c d]  = [a+c b+d]
    Matrix + Matrix = Matrix
    add checks shape
    """
    if shape(vect1) == shape(vect2):
        return [a + b for a, b in zip(vect1, vect2)]
    else:
        raise ShapeError


def vector_sub(vect1, vect2):
    """
    [a b]  - [c d]  = [a-c b-d]
    Matrix + Matrix = Matrix
    sub checks shape
    """
    if shape(vect1) == shape(vect2):
        return [a - b for a, b in zip(vect1, vect2)]
    else:
        raise ShapeError


def vector_sum(*args):
    """vector_sum can take any number of vectors and add them together."""
    for arg in args:
        if shape(arg) != shape(args[0]):
            raise ShapeError
        else:
            continue

    return [sum(arg) for arg in zip(*args)]


def dot(vect1, vect2):
    """
    dot([a b], [c d])   = a * c + b * d
    dot(Vector, Vector) = Scalar
    """
    if shape(vect1) == shape(vect2):
        return sum([a*b for (a, b) in zip(vect1, vect2)])
    else:
        raise ShapeError


def vector_multiply(vector, multiplier):
    """
    [a b]  *  Z     = [a*Z b*Z]
    Vector * Scalar = Vector
    """
    return [i * multiplier for i in vector]


def vector_mean(vect1, vect2, *args):
    """
    mean([a b], [c d]) = [mean(a, c) mean(b, d)]
    mean(Vector)       = Vector
    """
    return [sum(i)/len(i) for i in zip(vect1, vect2, *args)]


def magnitude(vector):
    """
    magnitude([a b])  = sqrt(a^2 + b^2)
    magnitude(Vector) = Scalar
    """
    return (sum([v**2 for v in vector]))**0.5
