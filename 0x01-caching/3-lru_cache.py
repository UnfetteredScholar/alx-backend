#!/usr/bin/env python3
"""
Defines the LRUCache class
"""

from collections import deque

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class"""

    def __init__(self):
        """Constructs LRUCache object"""
        super().__init__()
        self.queue = deque()

    def update_palcement(self, key):
        """Updates the placement of an item in the queue"""
        if key in self.queue:
            self.queue.remove(key)
        self.queue.append(key)

    def put(self, key, item):
        """
        Puts an item in the cache
        If the number of items in self.cache_data is higher
        that BaseCaching.MAX_ITEMS
        discards the least recently used item (LRU algorithm)
        """

        if key and item:
            self.cache_data[key] = item

            if len(self.cache_data.keys()) > self.MAX_ITEMS:
                k = self.queue.popleft()
                del self.cache_data[k]
                print(f"DISCARD: {k}")

            self.update_palcement(key)

    def get(self, key):
        """Gets an item in the cache"""
        if key:
            res = self.cache_data.get(key)
            if res:
                self.update_palcement(key)
            return res
