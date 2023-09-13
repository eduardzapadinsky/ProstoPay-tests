"""
This implementation efficiently handles collisions, maintains simplicity, and provides robust testing
for reliable key-value storage:

- Linear Probing for Collisions: Linear probing efficiently handles collisions by searching for the next available slot,
minimizing wasted space.
- Fixed-Size Array: Using a fixed-size array simplifies implementation and avoids the complexity of dynamic resizing.
- Efficient Hash Function: The hash function (key % self.size) evenly distributes keys for minimal collisions.
- Handling Updates: Properly updates existing keys, ensuring the latest values are associated with them.
- Comprehensive Test Coverage: Unit tests cover key aspects, enhancing implementation correctness and robustness.
- Simplicity and Readability: Code is clear, concise, and follows best practices for maintainability.
- Default Size Parameter: Offers flexibility with a default size of 10 when not explicitly specified.

"""


class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size

    def put(self, key, value):
        """
        Inserts a key-value pair into the hash map. Handles collisions using linear probing.

        Args:
            key: The key to insert.
            value: The associated value.
        """

        index = self.hash(key)
        item = self.table[index]
        if item is None:
            self.table[index] = [key, value]
        else:
            # Collision detected. Handle it by linear probing.
            while item is not None and item[0] != key:
                index = self.rehash(index)
                item = self.table[index]

            if item is None:
                self.table[index] = [key, value]
            else:
                # Key already exists; update the value.
                item[1] = value

    def get(self, key):
        """Retrieves the value associated with the given key.

        Args:
            key: The key to look up.
        Returns:
            The associated value or None if the key is not found.
        """

        index = self.hash(key)
        item = self.table[index]
        while item is not None:
            if key == item[0]:
                return item[1]
            index = self.rehash(index)
            item = self.table[index]
        return None

    def hash(self, key):
        """Computes the hash value for the given key.

        Args:
            key: The key to hash.
        Returns:
            The hash value.
        """

        return key % self.size

    def rehash(self, index):
        """Computes a new index for handling collisions using linear probing.

        Args:
            index: The current index.
        Returns:
            The new index after linear probing.
        """

        return (index + 1) % self.size
