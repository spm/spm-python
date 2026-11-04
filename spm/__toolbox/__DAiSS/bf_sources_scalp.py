from spm._runtime import Runtime


def bf_sources_scalp(*args, **kwargs):
    r"""
      Generate source space on the scalp surface, as a part of measuring a  
        magnetomyogram (MMG) of the face.  
          
        See https://doi.org/10.1111/psyp.13507 for more information.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DAiSS/bf_sources_scalp.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_sources_scalp", *args, **kwargs)
