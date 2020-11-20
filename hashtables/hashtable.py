# Hash Tables are direct access data structures of key: value pairs, and the keys must be unique within one Hash Table.
# Values can be directly accessed using their keys, similar to how an array value is accesed using its index.
# However, while array indexes must be integers, hash table keys are more flexible, e.g. they can be strings.
#
# The main operations on a Hash Table are:
# - Store a value with some key
# - Extract the value given the key
# - Delete the key: value pair, given the key
# - Replace the value of an existing key: value pair, given the key
#
# Keys are "hashed" using a hash function (https://en.wikipedia.org/wiki/Hash_function ).
# Hashing is quite complex, but fortunately Python comes with a ready built hash table implementation
# called a dictionary (https://docs.python.org/3/tutorial/datastructures.html#dictionaries ).
#
# Hash tables are commonly used to build data caches (https://en.wikipedia.org/wiki/Cache_(computing) ).
class HashTable:

    def __init__(self):
        # Create an empty Dictionary.
        self.key_value_pairs = {}

    # Store a value with some key.
    # This would replace the value of an existing key: value pair,
    # or create a new pair.
    def store(self, key, value):
        self.key_value_pairs[key] = value

    # Extract, but not delete, the value given the key.
    def get_value(self, key):
        return self.key_value_pairs[key]

    # Delete the key: value pair, given the key.
    def delete(self, key):
        del self.key_value_pairs[key]

    def print(self):
        print(self.key_value_pairs)

# Create a new hash table.
hash_table = HashTable()
# Add data.
hash_table.store("key1", 5)
hash_table.store("key2", 10)
hash_table.store(3, 15)
hash_table.store("4", 20)

# Exercise the hash table.
hash_table.print()

key = "key2"
value = hash_table.get_value(key)
print("Extracted value ", value, " given key ", key)

hash_table.print()
print("Deleted key: value pair with key '4'.")
hash_table.delete("4")
hash_table.print()

print("Replace value with key 'key1'")
hash_table.store("key1", 2)
hash_table.print()

print("Trying to access non-existant key will throw a KeyError...")
hash_table.get_value("random")