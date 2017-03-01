class ShapeError(Exception):
    pass


class Vector:

    def __init__(self, vector):
        if isinstance(vector, list):
            self.vector = vector
            self.length = len(vector)
        else:
            raise TypeError

    def shape(self):
        """shape takes a vector or matrix and return a tuple with the
        number of rows (for a vector) or the number of rows and columns
        (for a matrix.)"""
        return ((self.length, ))

    def vector_add(self, other):
        """
        [a b]  + [c d]  = [a+c b+d]
        Matrix + Matrix = Matrix
        add checks shape
        """
        if self.shape() == other.shape():
            return Vector([a + b for a, b in zip(self.vector, other.vector)])
        else:
            raise ShapeError

    def vector_sub(self, other):
        """
        [a b]  - [c d]  = [a-c b-d]
        Matrix + Matrix = Matrix
        sub checks shape
        """
        if self.shape() == other.shape():
            return Vector([a - b for a, b in zip(self.vector, other.vector)])
        else:
            raise ShapeError

    def vector_sum(self, *args):
        """vector_sum can take any number of vectors and add them together."""
        for arg in args:
            if self.shape(arg) != self.shape(args[0]):
                raise ShapeError
            else:
                continue

        return Vector([sum(arg) for arg in zip(*args)])

    def dot(self, other):
        """
        dot([a b], [c d])   = a * c + b * d
        dot(Vector, Vector) = Scalar
        """
        if self.shape() == other.shape():
            return sum([a*b for (a, b) in zip(self.vector, other.vector)])
        else:
            raise ShapeError

    def vector_multiply(self, multiplier):
        """
        [a b]  *  Z     = [a*Z b*Z]
        Vector * Scalar = Vector
        """
        return Vector([a * multiplier for a in self.vector])

    def vector_mean(self, other):
        """
        mean([a b], [c d]) = [mean(a, c) mean(b, d)]
        mean(Vector)       = Vector
        """
        if self.shape() == other.shape():
            return Vector([(a+b)/self.length for (a, b) in zip(self.vector, other.vector)])
        else:
            raise ShapeError

    def magnitude(self):
        """
        magnitude([a b])  = sqrt(a^2 + b^2)
        magnitude(Vector) = Scalar
        """
        return (sum([a*2 for a in self.vector]))**0.5
