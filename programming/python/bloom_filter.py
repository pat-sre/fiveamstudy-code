class BloomFilter:
    def __init__(self, arr_size=100):
        self.bit_array = bytearray(arr_size)
        self.hash_funcs = self.init_hashes()

    def init_hashes(self):
        # will return a list of hash functions to call
        hash_functions = [self.djb2, self.sdbm, self.fnv1a_32]
        return hash_functions

    def djb2(self, data: bytes) -> int:
        """Simple and fast hash function (DJB2)."""
        hash_val = 5381
        for byte in data:
            # Equivalent to: hash_val = (hash_val * 33) + byte
            hash_val = ((hash_val << 5) + hash_val) + byte
        # Return as unsigned 32-bit integer
        return hash_val & 0xFFFFFFFF

    def sdbm(data: bytes) -> int:
        """Another simple hash function (SDBM)."""
        hash_val = 0
        for byte in data:
            # Equivalent to: hash_val = byte + (hash_val * 65599) - hash_val
            hash_val = byte + (hash_val << 6) + (hash_val << 16) - hash_val
        # Return as unsigned 32-bit integer

        return hash_val & 0xFFFFFFFF

    def fnv1a_32(data: bytes) -> int:
        """Fowler–Noll–Vo hash function, FNV-1a 32-bit version."""
        FNV_PRIME_32 = 16777619
        FNV_OFFSET_BASIS_32 = 2166136261
        hash_val = FNV_OFFSET_BASIS_32
        for byte in data:
            hash_val ^= byte
            hash_val = (hash_val * FNV_PRIME_32) & 0xFFFFFFFF # Ensure 32-bit unsigned
        return hash_val

    def __contains__(self, i):
        pass
    
    def add(self, data: bytes):
        for hash_func in self.hash_funcs:
            hashed_input = hash_func(data)
            print(hashed_input)

def encode_string(text: str) -> bytes:
    return text.encode("utf-8")

items_to_add = [
    "apple",
    "banana",
    "orange",
    "grape",
    "kiwi",
    "Hello World",
    "Bloom Filter Test",
    "", # Empty string
    "Duplicate",
    "Duplicate", # Add a duplicate to see it doesn't hurt
    "Data Science",
    "Site Reliability Engineering",
    "Torun", # From your background info
]
bytes_to_add = [encode_string(i) for i in items_to_add]
my_bloom = BloomFilter(arr_size=1000)

print(bytes_to_add)