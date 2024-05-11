class FileSystem:
    def __init__(self):
        self.root = Directory("/")  # Initialize the FileSystem with a root directory

    def create_directory(self, path):
        before_last_node, new_directory_name = self._extract_from_path(
            path)  # Extract the parent directory and new directory name

        new_directory = Directory(new_directory_name)  # Create a new directory object
        before_last_node.add_node(new_directory)  # Add the new directory to the parent directory

    def create_file(self, path, contents):
        before_last_node, new_file_name = self._extract_from_path(
            path)  # Extract the parent directory and new file name

        new_file = File(new_file_name)  # Create a new file object
        new_file.write_contents(contents)  # Write contents to the new file
        before_last_node.add_node(new_file)  # Add the new file to the parent directory

    def read_file(self, path):
        before_last_node, file_name = self._extract_from_path(path)  # Extract the parent directory and file name

        if file_name not in before_last_node.children:
            raise ValueError(f"File not found: {file_name}")  # Check if the file exists and raise error if not

        return before_last_node.children[file_name].contents  # Return the contents of the file

    def delete_directory_or_file(self, path):
        before_last_node, node_to_delete_name = self._extract_from_path(
            path)  # Extract the parent directory and the node name to be deleted

        if node_to_delete_name not in before_last_node.children:
            raise ValueError(
                f"Node not found: {node_to_delete_name}.")  # Check if the node exists and raise error if not

        before_last_node.delete_node(node_to_delete_name)  # Delete the specified node

    def size(self):
        size = 0
        nodes = [self.root]  # Start with the root directory
        while len(nodes) > 0:
            current_node = nodes.pop()  # Process one node at a time
            if isinstance(current_node, Directory):
                children = list(current_node.children.values())  # If directory, get all children
                nodes.extend(children)  # Add children to the list to process them next
                continue

            if isinstance(current_node, File):
                size += len(current_node)  # If file, add its size to the total size

        return size  # Return the total size of all files in the system

    def __str__(self):
        return f"*** FileSystem ***\n" + self.root.__str__() + "\n***"  # String representation of the entire file system

    @staticmethod
    def _validate_path(path):
        if not path.startswith("/"):
            raise ValueError("Path should start with `/`.")  # Validate that all paths start with a '/'

    def _extract_from_path(self, path):
        FileSystem._validate_path(path)  # Validate path format

        path_node_names = path[1:].split("/")  # Split the path into parts
        middle_node_names = path_node_names[:-1]  # Path to the parent directory
        last_node_name = path_node_names[-1]  # The last part of the path, either a new directory or file

        before_last_node = self._find_bottom_node(middle_node_names)  # Find the parent directory

        if not isinstance(before_last_node, Directory):
            raise ValueError(f"{before_last_node.name} isn't a Directory.")  # Ensure the found node is a directory

        return (before_last_node, last_node_name)  # Return the parent directory and the new node name

    def _find_bottom_node(self, node_names):
        current_node = self.root  # Start from the root directory
        for node_name in node_names:
            if not isinstance(current_node, Directory):
                raise ValueError(
                    f"{current_node.name} isn't a Directory.")  # Ensure each node in the path is a directory

            if node_name not in current_node.children:
                raise ValueError(f"Node not found: {node_name}")  # Check if the next node in the path exists

            current_node = current_node.children[node_name]  # Move to the next node in the path

        return current_node  # Return the node at the end of the path


class Node:
    def __init__(self, name):
        self.name = name  # Name of the node (file or directory)

    def __str__(self):
        return f"{self.name} ({type(self).__name__})"  # Return a string representation of the node with its type


class Directory(Node):
    def __init__(self, name):
        super().__init__(name)  # Initialize the base Node class
        self.children = {}  # Dictionary to hold child nodes

    def add_node(self, node):
        self.children[node.name] = node  # Add a child node to the directory

    def delete_node(self, name):
        del self.children[name]  # Delete a child node by name

    def __str__(self):
        string = super().__str__()  # Get the base node string representation

        children_strings = []  # Collect strings of all child nodes
        for child in self.children.values():
            child_string = child.__str__().rstrip()  # String representation of each child node
            children_strings.append(child_string)

        children_combined_string = indent("\n".join(children_strings), 2)  # Indent the strings of the child nodes
        string += "\n" + children_combined_string.rstrip()  # Append the indented child strings to the directory string
        return string


class File(Node):
    def __init__(self, name):
        super().__init__(name)  # Initialize the base Node class
        self.contents = ""  # Start with empty contents for the file

    def write_contents(self, contents):
        self.contents = contents  # Set or update the contents of the file

    def __len__(self):
        return len(self.contents)  # Return the size of the file's contents

    def __str__(self):
        return super().__str__() + f" | {len(self)} characters"  # Enhance the string representation with the size of the contents


def indent(string, number_of_spaces):
    spaces = " " * number_of_spaces  # Create a string of spaces for indentation
    lines = string.split("\n")  # Split the string into individual lines
    indented_lines = [spaces + line for line in lines]  # Indent each line
    return "\n".join(indented_lines)  # Combine the indented lines back into a single string
