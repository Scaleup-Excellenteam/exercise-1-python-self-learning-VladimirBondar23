"""
A Post Office simulation that allows users to send, read, and search messages.
"""

class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental ID of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, title, message_body, urgent=False):
        """Send a message to a recipient.

        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str title: The title of the message.
        :param str message_body: The body of the message.
        :param bool urgent: Whether the message is urgent (default: False).
        :return: The message ID, auto-incremented number.
        :rtype: int
        :raises KeyError: If the recipient does not exist.
        """
        if recipient not in self.boxes:
            raise KeyError(f"Recipient '{recipient}' does not exist.")

        self.message_id += 1
        message_details = {
            'id': self.message_id,
            'title': title,
            'body': message_body,
            'sender': sender,
            'unread': True  # This allows sorting messages into read and unread
        }
        if urgent:
            self.boxes[recipient].insert(0, message_details)
        else:
            self.boxes[recipient].append(message_details)

        return self.message_id

    def search_inbox(self, username, search_string):
        """
        Search for messages in the user's inbox that contain a specific string.

        :param str username: The username whose inbox is being searched.
        :param str search_string: The string to search for in messages.
        :return: A list of matching messages.
        """
        return [
            message for message in self.boxes.get(username, [])
            if search_string.lower() in (message['title'] + message['body']).lower()
        ]

    def read_inbox(self, username, n=0):
        """
        Retrieve and mark as read the first `n` messages in a user's inbox.

        :param str username: The username whose inbox is being read.
        :param int n: The number of messages to read (0 returns all).
        :return: A list of messages.
        """
        messages = self.boxes.get(username, [])

        if n == 0:
            n = len(messages)  # If n is 0, return all messages

        read_messages = []
        for i in range(min(n, len(messages))):  # Avoid index errors
            message_copy = messages[i].copy()  # Create a copy to mark as read
            message_copy['unread'] = False
            read_messages.append(message_copy)
            self.boxes[username][i] = message_copy  # Update original message status

        return read_messages


if __name__ == '__main__':
    post_office = PostOffice(['John', 'Jane', 'Mary'])
    post_office.send_message('John', 'Mary', 'Hello', 'Hello Mary')
    post_office.send_message('Mary', 'John', 'Reply', 'Hello John')
    post_office.send_message('John', 'Mary', 'Checking in', 'How is it going?')

    print(post_office.read_inbox('Mary'))
    print(post_office.search_inbox('Mary', 'Hello'))
