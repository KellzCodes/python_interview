class FileSystem:
    def __init__(self):
        self.root = Directory("/")  # Initialize the file system with a root directory

    def create_directory(self, path):
        FileSystem._validate_path(path)  # Ensure path starts with '/'

        path_node_names = path[1:].split("/")  # Break path into parts
        middle_node_names = path_node_names[:-1]  # All but the last part represent the path to the parent directory
        new_directory_name = path_node_names[-1]  # Last part is the name of the new directory

        before_last_node = self._find_bottom_node(middle_node_names)  # Find the parent directory node

        if not isinstance(before_last_node, Directory):
            raise ValueError(f"{before_last_node.name} isn't a Directory.")  # Ensure the node is a directory

        new_directory = Directory(new_directory_name)  # Create the new directory
        before_last_node.add_node(new_directory)  # Add the new directory to the parent directory

    def create_file(self, path, contents):
        FileSystem._validate_path(path)  # Ensure path starts with '/'

        path_node_names = path[1:].split("/")  # Break path into parts
        middle_node_names = path_node_names[:-1]  # Path to the directory
        new_file_name = path_node_names[-1]  # The new file name

        before_last_node = self._find_bottom_node(middle_node_names)  # Find the parent directory node

        if not isinstance(before_last_node, Directory):
            raise ValueError(f"{before_last_node.name} isn't a Directory.")  # Ensure it is a directory

        new_file = File(new_file_name)  # Create the file
        new_file.write_contents(contents)  # Write contents to the file
        before_last_node.add_node(new_file)  # Add the file to the directory

    def read_file(self, path):
        FileSystem._validate_path(path)  # Ensure path starts with '/'

        path_node_names = path[1:].split("/")  # Break path into parts
        middle_node_names = path_node_names[:-1]  # Path to the directory
        file_name = path_node_names[-1]  # Name of the file to read

        before_last_node = self._find_bottom_node(middle_node_names)  # Find the parent directory

        if file_name not in before_last_node.children:
            raise ValueError(f"File not found: {file_name}")  # Ensure file exists

        return before_last_node.children[file_name].contents  # Return file contents

    def delete_directory_or_file(self, path):
        FileSystem._validate_path(path)  # Ensure path starts with '/'

        path_node_names = path[1:].split("/")  # Break path into parts
        middle_node_names = path_node_names[:-1]  # Path to the parent directory
        node_to_delete_name = path_node_names[-1]  # Name of the node to delete

        before_last_node = self._find_bottom_node(middle_node_names)  # Find the parent directory

        if node_to_delete_name not in before_last_node.children:
            raise ValueError(f"Node not found: {node_to_delete_name}")  # Ensure node exists

        before_last_node.delete_node(node_to_delete_name)  # Delete the node

    def size(self):
        size = 0
        nodes = [self.root]  # Start with the root directory
        while len(nodes) > 0:
            current_node = nodes.pop()  # Get one node
            if isinstance(current_node, Directory):
                children = list(current_node.children.values())  # List children if directory
                nodes.extend(children)  # Add children to nodes list to continue traversal
                continue

            if isinstance(current_node, File):
                size += len(current_node)  # Add file size to total size

        return size  # Return the total size of all files

    def __str__(self):
        return f"*** FileSystem ***\n" + self.root.__str__() + "\n***"  # Represent the file system as a string

    @staticmethod
    def _validate_path(path):
        if not path.startswith("/"):
            raise ValueError("Path should start with `/`.")  # Path validation

    def _find_bottom_node(self, node_names):
        current_node = self.root  # Start from the root
        for node_name in node_names:
            if not isinstance(current_node, Directory):
                raise ValueError(f"{current_node.name} isn't a Directory.")  # Ensure current node is a directory

            if node_name not in current_node.children:
                raise ValueError(f"Node not found: {node_name}")  # Ensure child node exists

            current_node = current_node.children[node_name]  # Move to the child node

        return current_node  # Return the bottom node in the specified path


class Node:
    def __init__(self, name):
        self.name = name  # Node name

    def __str__(self):
        return f"{self.name} ({type(self).__name__})"  # Node string representation


class Directory(Node):
    def __init__(self, name):
        super().__init__(name)  # Initialize the Node part of Directory
        self.children = {}  # Children of the directory

    def add_node(self, node):
        self.children[node.name] = node  # Add a child node

    def delete_node(self, name):
        del self.children[name]  # Remove a child node

    def __str__(self):
        string = super().__str__()  # Get Node string representation

        children_strings = []  # Strings of child nodes
        for child in list(self.children.values()):
            child_string = child.__str__().rstrip()  # Get child node string
            children_strings.append(child_string)

        children_combined_string = indent("\n".join(children_strings), 2)  # Indent child node strings
        string += "\n" + children_combined_string.rstrip()  # Append indented strings
        return string


class File(Node):
    def __init__(self, name):
        super().__init__(name)  # Initialize the Node part of File
        self.contents = ""  # File contents

    def write_contents(self, contents):
        self.contents = contents  # Update file contents

    def __len__(self):
        return len(self.contents)  # Return length of contents

    def __str__(self):
        return super().__str__() + f" | {len(self)} characters"  # Append content length to string representation


def indent(string, number_of_spaces):
    spaces = " " * number_of_spaces  # Create indentation spaces
    lines = string.split("\n")  # Split string into lines
    indented_lines = [spaces + line for line in lines]  # Indent each line
    return "\n".join(indented_lines)  # Combine lines back into a single string
