#!/usr/bin/env python3
"""
Defines the function index_range
"""
from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int,int]:
    """
    Generates a tuple containing the start and end indexes 
    of a range based on the page number and page size
    """
    return ((page_size * page) - page_size, page_size * page)