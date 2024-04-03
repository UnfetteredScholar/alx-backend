#!/usr/bin/env python3
"""
Defines the FIFOCache class
"""
from collections import deque

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache Class"""

    def __init__(self):
        """Constructs FIFOCache object"""
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """
        Puts an item in the cache
        If the number of items in self.cache_data is higher
        that BaseCaching.MAX_ITEMS
        discards the first item that was added to the cache (FIFO)
        """

        if key and item:
            self.queue.append(key)
            self.cache_data[key] = item

        if len(self.cache_data.keys()) > self.MAX_ITEMS:
            k = self.queue.popleft()
            del self.cache_data[k]
            print(f"DISCARD: {k}")

    def get(self, key):
        """Gets an item in the cache"""
        if key:
            return self.cache_data.get(key)
