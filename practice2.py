
def score(x, y):
    """
    Write a function that returns the earned points in a single toss of a Darts game.

Darts is a game where players throw darts at a target.

In our particular instance of the game, the target rewards 4 different amounts of points, depending on where the dart lands:

If the dart lands outside the target, player earns no points (0 points).
If the dart lands in the outer circle of the target, player earns 1 point.
If the dart lands in the middle circle of the target, player earns 5 points.
If the dart lands in the inner circle of the target, player earns 10 points.
The outer circle has a radius of 10 units (this is equivalent to the total radius for the entire target),
the middle circle a radius of 5 units, and the inner circle a radius of 1.
Of course, they are all centered at the same point (that is, the circles are concentric) defined by the coordinates (0, 0).

Write a function that given a point in the target (defined by its Cartesian coordinates x and y, where x and y are real), returns the correct amount earned by a dart landing at that point.
    """
    from math import sqrt
    try:
        radius = sqrt(x ** 2 + y ** 2)
        print(radius)
    except:
        raise ValueError("wrong inputs")
    if radius > 10:
        return 0
    elif radius > 5:
        return 1
    elif radius > 1:
        return 5
    elif radius >= 0:
        return 10


# print(score(1, 2))

def flatten(iterable):
    """
    Take a nested list and return a single flattened list with all values except nil/null.

The challenge is to write a function that accepts an arbitrarily-deep nested list-like structure and returns a flattened structure without any nil/null values.

For Example

input: [1,[2,3,null,4],[null],5]

output: [1,2,3,4,5]
    """

    items = []
    for item in iterable:
        if isinstance(item, (list, tuple)):
            items += flatten(item)
        elif item is not None:
            items.append(item)
    return items

print(flatten([4,7,[9,4],[2,5,9]]))