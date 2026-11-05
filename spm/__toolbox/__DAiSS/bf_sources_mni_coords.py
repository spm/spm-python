from spm._runtime import Runtime


def bf_sources_mni_coords(*args, **kwargs):
    r"""
      Generate beamforming grid  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DAiSS/bf_sources_mni_coords.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_sources_mni_coords", *args, **kwargs)
