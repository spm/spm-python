from spm._runtime import Runtime


def mci_approach_struct(*args, **kwargs):
    r"""
      Approach model structure  
        FORMAT [M,U] = mci_approach_struct (Nobs)  
         
        Nobs      Number of observations  
        M         Model structure  
        U         Input structure  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/models/approach/mci_approach_struct.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_approach_struct", *args, **kwargs)
