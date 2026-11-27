from spm._runtime import Runtime


def mci_approach_gen(*args, **kwargs):
    r"""
      Approach to limit model  
        FORMAT [y] = mci_approach_gen (P,M,U)  
         
        P         parameters  
        M,U       as usual  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/models/approach/mci_approach_gen.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_approach_gen", *args, **kwargs)
