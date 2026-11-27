from spm._runtime import Runtime


def spm_RDP_O(*args, **kwargs):
    r"""
      places outcomes in a recursive model  
        FORMAT RDP = spm_RDP_O(RDP,O,[L])  
        RDP - recursive MDP  
        O   - outcomes  
        L   - level [default: 1]  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_RDP_O.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_RDP_O", *args, **kwargs)
