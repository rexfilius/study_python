def markInventory(clothingItems):
    """
    given ['Purple Shirt', 'Green Shirt']
    return [ "Purple Shirt Size-1", "Purple Shirt Size-2", "Purple Shirt Size-3",
    "Purple Shirt Size-4", "Purple Shirt Size-5", "Green Shirt Size-1",
    "Green Shirt Size-2", "Green Shirt Size-3", "Green Shirt Size-4",
    "Green Shirt Size-5"]
    Time complexity is O(N).
    NOTE: Nested loops often give O(N^2) time BUT Nested loops that result in
    O(N^2) occur when each loop revolves around N
    """
    clothingOptions = []
    for item in clothingItems:
        for size in range(1, 6):
            clothingOptions.append(item + ' Size-' + str(size))
    return clothingOptions


print(markInventory(['Purple Jean', 'Green Jean']))
