class HashTable:
    """A simple hash table implementation using Python dictionaries."""

    def __init__(self):
        self.collection = {}

    def hash(self, key):
        """Generate a hash for a given key."""
        total = 0
        for char in key:
            total += ord(char)
        return total

    def add(self, key, value):
        """Add a key-value pair to the hash table."""
        hashed_key = self.hash(key)

        if hashed_key not in self.collection:
            self.collection[hashed_key] = {}

        self.collection[hashed_key][key] = value

    def remove(self, key):
        """Remove a key-value pair from the hash table."""
        hashed_key = self.hash(key)

        if hashed_key in self.collection and key in self.collection[hashed_key]:
            del self.collection[hashed_key][key]

            if not self.collection[hashed_key]:
                del self.collection[hashed_key]

    def lookup(self, key):
        """Retrieve a value by its key."""
        hashed_key = self.hash(key)

        if hashed_key in self.collection:
            return self.collection[hashed_key].get(key)

        return None

    def __str__(self):
        return str(self.collection)


if __name__ == '__main__':
    table = HashTable()
    table.add("apple", 5)
    table.add("banana", 3)

    print(table.lookup("apple"))
    table.remove("apple")
    print(table.lookup("apple"))
