#!/usr/bin/env python3
"""
Defines the LIFOCache classs
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache Class"""

    def __init__(self):
        """Constructs LIFOCache object"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """
        Puts an item in the cache
        If the number of items in self.cache_data is higher
        that BaseCaching.MAX_ITEMS
        discards the last item that was added to the cache (LIFO)
        """

        if key and item:
            self.cache_data[key] = item

            if len(self.cache_data.keys()) > self.MAX_ITEMS:
                k = self.stack.pop()
                del self.cache_data[k]
                print(f"DISCARD: {k}")

            self.stack.append(key)

    def get(self, key):
        """Gets an item in the cache"""
        if key:
            return self.cache_data.get(key)
