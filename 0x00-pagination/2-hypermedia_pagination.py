#!/usr/bin/env python3
"""Defines the Server class"""
import csv
import math
from typing import Any, Dict, List, Tuple


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

        dataset = self.dataset()

        range = index_range(page=page, page_size=page_size)

        if range[0] > len(dataset):
            return []
        return dataset[range[0]: range[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Gets the page specified along with Hypermedia"""
        dataset = self.dataset()

        hyper = {}
        hyper["page_size"] = page_size
        hyper["page"] = page
        hyper["data"] = self.get_page(page, page_size)
        hyper["next_page"] = page + 1 if page + 1 < len(dataset) else None
        hyper["prev_page"] = page - 1 if page - 1 > 0 else None
        hyper["total_pages"] = math.ceil(len(dataset) / page_size)

        return hyper
