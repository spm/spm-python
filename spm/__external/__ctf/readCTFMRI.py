from spm.__wrapper__ import Runtime


def readCTFMRI(*args, **kwargs):
    """
       Version 1.2: 25 April 2007   Module readCPersist changed and removed from this listing.  
         Version 1.1: 19 April 2007   No changes since v1.0  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/ctf/readCTFMRI.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("readCTFMRI", *args, **kwargs)
