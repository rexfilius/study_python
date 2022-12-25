from algoFreeCodeCamp.courseJovian.sort.Sort4 \
    import Notebook, mergerSortObjects, comapareLikes, comapareTitles

nb0 = Notebook('pytorch-basics', 'aakshns', 373)
nb1 = Notebook('linear-regression', 'siddhant', 532)
nb2 = Notebook('logisitic-regression', 'vikas', 31)
nb3 = Notebook('feedforward-nn', 'sonaksh', 94)
nb4 = Notebook('cifar10-cnn', 'biraj', 2)
nb5 = Notebook('cifar10-resnet', 'tanya', 29)
nb6 = Notebook('anime-gans', 'hemanth', 80)
nb7 = Notebook('python-fundamentals', 'vishal', 136)
nb8 = Notebook('python-functions', 'aakshns', 74)
nb9 = Notebook('python-numpy', 'siddhant', 92)

notebooks = [nb0, nb1, nb2, nb3, nb4, nb5, nb6, nb7, nb8, nb9]
print(notebooks)
print()

sortedBooksByDecreasingLikes = mergerSortObjects(notebooks, comapareLikes)
print(sortedBooksByDecreasingLikes)
print()

sortedBooksByTitle = mergerSortObjects(notebooks, comapareTitles)
print(sortedBooksByTitle)
