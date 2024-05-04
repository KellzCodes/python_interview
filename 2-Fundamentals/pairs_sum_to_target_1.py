def pairs_sum_to_target(list1, list2, target):
    # Initialize an empty list to store pairs of indices
    new_list = []

    # Loop through each element in list1 by its index
    for i in range(len(list1)):
        # Loop through each element in list2 by its index
        for j in range(len(list2)):
            # Check if the sum of the elements at the current indices equals the target
            if list1[i] + list2[j] == target:
                # If they sum to target, append the pair of indices (i, j) to the new_list
                new_list.append([i, j])

    # Return the list of index pairs where their corresponding elements sum to the target
    return new_list