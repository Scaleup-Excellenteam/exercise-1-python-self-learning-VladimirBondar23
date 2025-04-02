"""
This script lists files in a given directory that start with "deep".
"""

import os

def thats_the_way(directory):
    """
        Lists files in the given directory that start with 'deep'.

        :param directory: The directory to search in.
        :return: A list of filenames starting with 'deep'.
        """
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return []

    # List files that start with "deep"
    return [file for file in os.listdir(directory) if file.startswith('deep')]

if __name__ == '__main__':
    RELATIVE_PATH = "Notebooks/content/week05/images"  # Relative path (renamed to UPPER_CASE)
    FULL_PATH = os.path.abspath(RELATIVE_PATH)  # Convert to absolute path
    print(thats_the_way(FULL_PATH))
