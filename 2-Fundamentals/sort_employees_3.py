def sort_employees(employees, sort_by):
    # Define a list of sorting criteria corresponding to indices in employee records
    sort_indices = ["name", "age", "salary"]
    # Determine the index of the sorting criteria in the sort_indices list
    sort_index = sort_indices.index(sort_by)

    # Sort the list of employees using the sort_index determined above
    # A lambda function is used to extract the sorting key from each employee record
    sorted_employees = sorted(employees, key=lambda x: x[sort_index])

    # Return the sorted list of employees
    return sorted_employees
