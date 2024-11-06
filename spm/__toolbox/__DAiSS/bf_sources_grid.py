from spm.__wrapper__ import Runtime


def bf_sources_grid(*args, **kwargs):
    """
      Generate beamforming grid  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_sources_grid.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bf_sources_grid", *args, **kwargs)
