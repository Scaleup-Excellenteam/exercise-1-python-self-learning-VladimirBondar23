"""
This script scans a binary file for hidden messages matching a specific pattern.
"""

import re
import os

CHUNK_SIZE = 1024

def parsle_tongue():
    """
    Reads a binary file in chunks and extracts secret messages.

    The function searches for words with at least five lowercase letters followed by an exclamation mark (!).
    It ignores non-ASCII characters while decoding.

    :return: A list of extracted secret messages without the exclamation mark.
    """
    # Define a regex pattern to match secret messages
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/logo.jpg'))
    message_pattern = re.compile(r'[a-z]{5,}!')

    def read_in_chunks(file):
        """Generator to read a file in chunks."""
        while True:
            chunk = file.read(CHUNK_SIZE)
            if not chunk:
                break
            yield chunk

    result = []
    with open(file_path, 'rb') as file:
        for chunk in read_in_chunks(file):
            # Decode the chunk as binary to string if possible (ignore non-ASCII chars)
            try:
                text = chunk.decode('ascii', errors='ignore')
                # Find and collect all secret messages in the chunk
                for match in message_pattern.findall(text):
                    result.append(match[:-1])
            except UnicodeDecodeError:
                continue
    return result

if __name__ == '__main__':
    for message in parsle_tongue():
        print("Found secret message:", message)
