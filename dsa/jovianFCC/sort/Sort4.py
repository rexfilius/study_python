"""
You're working on a new feature on Jovian called "Top Notebooks of the Week".
Write a function to sort a list of notebooks in decreasing order of likes.
Keep in mind that up to millions of notebooks can be created every week, so your
function needs to be as efficient as possible.
"""


class Notebook:
    def __init__(self, title, username, likes):
        self.title = title
        self.username = username
        self.likes = likes

    def __repr__(self):
        return "Notebook <{}/{}, {} likes>" \
            .format(self.username, self.title, self.likes)


def comapareLikes(notebook1, notebook2):
    """
    Compares two notebooks using the 'likes' attribute.
    We want to sort the list in decreasing order.
    If notbook1 likes is > notebook 2 likes, it returns, lesser
    """
    if notebook1.likes > notebook2.likes:
        return 'lesser'
    elif notebook1.likes == notebook2.likes:
        return 'equal'
    elif notebook1.likes < notebook2.likes:
        return 'greater'


def comapareTitles(notebook1, notebook2):
    """
    Compares two notebooks using the 'title' attribute.
    """
    if notebook1.title < notebook2.title:
        return 'lesser'
    elif notebook1.title == notebook2.title:
        return 'equal'
    elif notebook1.title > notebook2.title:
        return 'greater'


def defaultCompare(x, y):
    if x < y:
        return 'lesser'
    elif x == y:
        return 'equal'
    else:
        return 'greater'


def mergerSortObjects(objects, compare=defaultCompare):
    if len(objects) < 2:
        return objects
    mid = len(objects) // 2
    left, right = objects[:mid], objects[mid:]
    return mergeObjects(mergerSortObjects(left, compare),
                        mergerSortObjects(right, compare), compare)


def mergeObjects(left, right, compare):
    i, j, merged = 0, 0, []
    while i < len(left) and j < len(right):
        result = compare(left[i], right[j])
        if result == 'lesser' or result == 'equal':
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    return merged + left[i:] + right[j:]
