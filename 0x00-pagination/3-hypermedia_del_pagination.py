#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import Dict, List, Union


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(
        self, index: Union[int, None] = None, page_size: int = 10
    ) -> dict:
        """Gets indexed data from dataset regardless of deleted items"""
        dataset = self.indexed_dataset()
        assert (
            index is not None and index >= 0 and index <= max(dataset.keys())
        )

        data = []
        count = 0
        next_index = None

        for k, v in dataset.items():
            if k >= index and count < page_size:
                data.append(v)
                count += 1
                continue

            if count == page_size:
                next_index = k
                break

        hyper = {}
        hyper["index"] = index
        hyper["next_index"] = next_index
        hyper["page_size"] = len(data)
        hyper["data"] = data

        return hyper
