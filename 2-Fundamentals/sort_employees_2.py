def sort_employees(employees, sort_by):
    # Define a list of valid sort criteria
    sort_indices = ["name", "age", "salary"]
    # Find the index corresponding to the sort_by criteria within the list
    sort_index = sort_indices.index(sort_by)

    # Initialize an empty list to store the sorted employees
    sorted_employees = []
    # Create a copy of the original employees list to manipulate during sorting
    employees_copy = employees[:]

    # Continue looping until all employees are sorted and removed from the copy
    while len(employees_copy) > 0:
        # Assume the first employee is the smallest for comparison purposes
        smallest_employee_index = 0

        # Loop through the current list of employees to find the one with the smallest attribute
        for i, employee in enumerate(employees_copy):
            # Get the value of the current smallest employee based on the sort_index
            current_smallest_value = employees_copy[smallest_employee_index][sort_index]
            # If the current employee has a smaller attribute, update the smallest index
            if employee[sort_index] < current_smallest_value:
                smallest_employee_index = i

        # Add the smallest employee found to the sorted list
        next_sorted_employee = employees_copy[smallest_employee_index]
        sorted_employees.append(next_sorted_employee)
        # Remove the smallest employee from the copy list
        employees_copy.pop(smallest_employee_index)

    # Return the list of employees sorted by the chosen attribute
    return sorted_employees
