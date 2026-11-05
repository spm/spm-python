from spm._runtime import Runtime


def _timelock2freq(*args, **kwargs):
    r"""
      TIMELOCK2FREQ transform the reconstructed dipole moment into  
        something that again resembles the physical input parameter in  
        the frequency domain.   
         
        This is needed after source reconstruction using FREQ2TIMELOCK.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/timelock2freq.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("timelock2freq", *args, **kwargs)
