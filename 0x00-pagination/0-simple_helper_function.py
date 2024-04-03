#!/usr/bin/env python3
"""
function named index_range that takes two integer arguments page and page_size
"""


def index_range(page, page_size):
    """function should return a tuple of size two"""
    previous = (page - 1) * page_size
    return (previous, previous + page_size)
