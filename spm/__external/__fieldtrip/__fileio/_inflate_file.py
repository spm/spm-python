from spm._runtime import Runtime


def _inflate_file(*args, **kwargs):
    r"""
      INFLATE_FILE helper function to uncompress a compressed file of arbitrary  
        compression type. Returns the full path to the extracted file or  
        directory, which will be located in a temporary location.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/inflate_file.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("inflate_file", *args, **kwargs)
