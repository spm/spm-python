from spm._runtime import Runtime


def spm_ADEM_set(*args, **kwargs):
    r"""
      Perform checks on DEM structures for active inversion  
        FORMAT DEM = spm_ADEM_set(DEM)  
         
        DEM.G  - generative model  
        DEM.M  - recognition model  
        DEM.C  - exogenous causes  
        DEM.U  - prior expectation of causes  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_ADEM_set.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_ADEM_set", *args, **kwargs)
