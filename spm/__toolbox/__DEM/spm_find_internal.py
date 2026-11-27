from spm._runtime import Runtime


def spm_find_internal(*args, **kwargs):
    r"""
      FORMAT nj = spm_find_internal(z,J)  
        finds indices of internal states (that do not contribute to slow modes)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_find_internal.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_find_internal", *args, **kwargs)
