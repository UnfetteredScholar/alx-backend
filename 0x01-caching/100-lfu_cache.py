#!/usr/bin/env python3
"""
Defines the LFUCache class
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache class"""

    def __init__(self):
        """Constructs LFUCache object"""
        super().__init__()
        self.ftable = {}
        self._time = 0

    def update_palcement(self, key):
        """Updates the placement of an item in the ftable"""
        if key not in self.ftable:
            self.ftable[key] = {"frequency": 1, "time": self._time}
        else:
            self.ftable[key]["frequency"] += 1
            self.ftable[key]["time"] = self._time
        self._time += 1

    def get_lfu_item(self):
        """Gets the least frequenty used item"""
        items = self.ftable.items()

        items = sorted(items, key=lambda x: (x[1]["frequency"], x[1]["time"]))

        return items[0][0]

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
                k = self.get_lfu_item()
                del self.cache_data[k]
                del self.ftable[k]
                print(f"DISCARD: {k}")

            self.update_palcement(key)

    def get(self, key):
        """Gets an item in the cache"""
        if key:
            res = self.cache_data.get(key)
            if res:
                self.update_palcement(key)
            return res
