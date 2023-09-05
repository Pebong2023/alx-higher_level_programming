#!/usr/bin/python3
class LockedClass:
    """LockedClass with only 'first_name' attribute allowed."""
    __slots__ = ['first_name']
