def pairs_sum_to_target(list1, list2, target):
    # Initialize an empty list to store pairs of indices where elements sum to the target
    pairs = []

    # Iterate through list1 with both index and value
    for i, value1 in enumerate(list1):
        # Iterate through list2 with both index and value
        for j, value2 in enumerate(list2):
            # Check if the sum of the values from list1 and list2 equals the target
            if value1 + value2 == target:
                # If they sum to the target, append the pair of indices (i, j) to the pairs list
                pairs.append([i, j])

    # Return the list of index pairs where the corresponding values sum to the target
    return pairs