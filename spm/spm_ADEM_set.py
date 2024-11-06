from spm.__wrapper__ import Runtime


def spm_ADEM_set(*args, **kwargs):
    """
      Perform checks on DEM structures for active inversion  
        FORMAT DEM = spm_ADEM_set(DEM)  
         
        DEM.G  - generative model  
        DEM.M  - recognition model  
        DEM.C  - exogenous causes  
        DEM.U  - prior expectation of causes  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_ADEM_set.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_ADEM_set", *args, **kwargs)
