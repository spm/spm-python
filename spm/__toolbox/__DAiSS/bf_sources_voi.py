from spm.__wrapper__ import Runtime


def bf_sources_voi(*args, **kwargs):
    """
      Generate a set of VOIs specified in MNI coordinates  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_sources_voi.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bf_sources_voi", *args, **kwargs)
