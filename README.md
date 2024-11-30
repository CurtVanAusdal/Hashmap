#Hashmap

The HashMap class implements a simple hash map (or dictionary) structure using a list of lists to store key-value pairs. The keys are tuples, and each key is hashed to determine its position in the internal storage. This hash map supports typical operations such as inserting new elements, retrieving values, deleting elements, and clearing the hash map. It also tracks its current size and capacity.

Key Features:
Tuple Keys: The hash map only supports keys that are tuples (not strings).
Custom Hash Function: A custom hashing method is used, which generates a hash value based on the sum of factors derived from the first element of the tuple.
Collision Handling: When multiple key-value pairs hash to the same location, they are placed in lists at the corresponding index.
Dynamic Resizing: The internal storage size is adjusted dynamically if the hash key exceeds the current array size.
Methods:
set(key, value): Inserts a key-value pair into the hash map.
get(key): Retrieves the value associated with a given key.
remove(key): Removes the key-value pair corresponding to the given key.
size(): Returns the number of key-value pairs currently in the hash map.
capacity(): Returns the current internal storage size of the hash map.
clear(): Clears all entries and resets the hash map.
keys(): Returns a list of all keys currently in the hash map.