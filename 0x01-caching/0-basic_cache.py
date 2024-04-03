#!/usr/bin/env python3
"""
Defines the BasicCache Class
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class"""

    def put(self, key, item):
        """Puts an item in the cache"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Gets an item in the cache"""
        if key:
            return self.cache_data.get(key)
