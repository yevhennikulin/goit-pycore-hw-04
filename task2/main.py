cats_file_path = 'cats.txt'
# Function to read and return cat names from the file
def get_cats_info(file_path):
    try:
        # Read the file and extract cat names
        with open(file_path, 'r') as file:
            # Read lines from the file
            lines = file.readlines()
            # Extract cat names and store in a list
            cat_names = []
            for line in lines:
                id, name, age = line.strip().split(',')
                cat_names.append({'id': id, 'name': name, 'age': age})
    except FileNotFoundError:
        # Handle file not found error
        return "The specified file was not found."
    except IOError:
        # Handle general I/O error
        return "An error occurred while reading the file."
    return cat_names

#use the function to get cat names
cat_names_list = get_cats_info(cats_file_path)
print(cat_names_list)
