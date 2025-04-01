import re
import os

CHUNK_SIZE = 1024

def parsle_tongue():
    # Define a regex pattern to match secret messages
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logo.jpg')
    message_pattern = re.compile(r'[a-z]{5,}!')

    def read_in_chunks(file):
        """Generator to read file in chunks."""

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
                # Find and yield all secret messages in the chunk
                for match in message_pattern.findall(text):
                    result.append(match[:-1])
            except UnicodeDecodeError:
                continue
    return result

if __name__ == '__main__':
    for message in parsle_tongue():
        print("Found secret message:", message)
