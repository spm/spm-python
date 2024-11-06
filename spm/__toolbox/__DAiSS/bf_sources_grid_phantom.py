from spm.__wrapper__ import Runtime


def bf_sources_grid_phantom(*args, **kwargs):
    """
      Generate beamforming grid  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_sources_grid_phantom.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bf_sources_grid_phantom", *args, **kwargs)
