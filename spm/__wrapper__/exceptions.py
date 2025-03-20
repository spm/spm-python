class IndexOrKeyOrAttributeError(IndexError, KeyError, AttributeError):
    """
    Error raised when a non-indexing operation is performed on a
    non-finalized delayed array.
    """
