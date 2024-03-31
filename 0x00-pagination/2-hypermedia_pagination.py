#!/usr/bin/env python3
"""Defines the Server class"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Generates a tuple containing the start and end indexes
    of a range based on the page number and page size
    """
    return ((page_size * page) - page_size, page_size * page)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Gets the page specified"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        range = index_range(page=page, page_size=page_size)

        try:
            return self.dataset()[range[0]: range[1]]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Gets the page specified along with Hypermedia"""

        hyper = {}
        page_data = self.get_page(page, page_size)
        data_size = len(self.dataset())
        total_pages = math.ceil(data_size / page_size)
        hyper["page_size"] = len(page_data)
        hyper["page"] = page
        hyper["data"] = page_data
        hyper["next_page"] = page + 1 if page < total_pages else None
        hyper["prev_page"] = page - 1 if page - 1 > 0 else None
        hyper["total_pages"] = total_pages

        return hyper
