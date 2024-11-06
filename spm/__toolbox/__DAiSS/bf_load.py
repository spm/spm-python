from spm.__wrapper__ import Runtime


def bf_load(*args, **kwargs):
    """
      Load BF data into memory with just the requested fields  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_load.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bf_load", *args, **kwargs)
