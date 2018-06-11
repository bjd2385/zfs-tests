from __future__ import division


def bytes_to_mebibyte(size_in_bytes):
    # type: (int) -> float
    """
    Since the output of zfs get -p is in bytes, and disk read/write is often
    measures in mb/s, this function will allow easy translation. 
    """
    size_in_mib = size_in_bytes / 0x100000

    return size_in_mib
