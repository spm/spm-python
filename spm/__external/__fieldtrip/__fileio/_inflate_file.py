from spm.__wrapper__ import Runtime


def _inflate_file(*args, **kwargs):
    """
      INFLATE_FILE helper function to uncompress a compressed file of arbitrary  
        compression type. Returns the full path to the extracted file or  
        directory, which will be located in a temporary location.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/inflate_file.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("inflate_file", *args, **kwargs)
