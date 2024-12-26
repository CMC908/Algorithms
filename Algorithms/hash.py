class HashTable:
    def __init__(self):
        self.table_size = 26  # Assuming hashing table size as 26 (for 26 alphabetical characters)
        self.hash_table = [None] * self.table_size  # Initialize hash table as a list of None values

    def compute_hash(self, text):
        hash_value = 0
        for char in text:
            if char.isalpha():  # Check if the character is an alphabet
                char_value = ord(char.lower()) - ord('a') + 1  # Assign numerical value 1-26 to alphabetical characters
                hash_value += char_value
        return hash_value % self.table_size  # Ensure hash value falls within the range of hash table size

if __name__ == "__main__":
    hash_table = HashTable()

    # Input textx   
    input_text = input("Enter a text to compute hash: ")

    # Compute hash
    hash_value = hash_table.compute_hash(input_text)

    # Display hash value
    print("Hash value for '{}' is: {}".format(input_text, hash_value))
