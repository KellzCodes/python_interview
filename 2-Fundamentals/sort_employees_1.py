def sort_employees(employees, sort_by):
    # Initialize an empty list to store the sorted employees
    new_list = []

    # Define a helper function to get the age from an employee record
    def sort_age(lst):
        return lst[1]  # Assuming the second element in the list is the age

    # Define a helper function to get the salary from an employee record
    def sort_salary(lst):
        return lst[2]  # Assuming the third element in the list is the salary

    # Check if the sorting should be done by name
    if sort_by == "name":
        # Sort the list of employees alphabetically by their name (first element by default)
        new_list = sorted(employees)
        return new_list
    # Check if the sorting should be done by age
    elif sort_by == "age":
        # Sort the list of employees by age using the sort_age function as the key
        new_list = sorted(employees, key=sort_age)
        return new_list
    # Otherwise, sort by salary
    else:
        # Sort the list of employees by salary using the sort_salary function as the key
        new_list = sorted(employees, key=sort_salary)
        return new_list
