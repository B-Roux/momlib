"""
Provides definitions and implementations that need to be available to
    all modules that implement graph theory functionality.
"""

__all__ = ("NodeNotFoundError",)


class NodeNotFoundError(KeyError):
    def __init__(self, message: str):
        super().__init__(message)
