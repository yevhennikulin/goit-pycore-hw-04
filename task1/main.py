# Init file path
wages_file_path = 'wages.txt'
# Function to calculate total and average salary
def total_salary(file_path):
    # Initialize total wages and average
    try:
        # Read the file and calculate total wages and average
        with open(file_path, 'r') as file:
            # Initialize total wages
            total_wages = 0
            # Read lines from the file
            lines = file.readlines()
            # Calculate total wages
            for line in lines:
                name, salary = line.strip().split(',')
                total_wages += int(salary)
            # Calculate average wages
            average = total_wages / len(lines)
    except FileNotFoundError:
        # Handle file not found error
        return "The specified file was not found."
    except ValueError:
        # Handle value error in case of incorrect data format
        return "There was an error processing the file contents."
    return (total_wages, average)

salary_tuple = total_salary(wages_file_path)

