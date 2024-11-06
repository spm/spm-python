from spm.__wrapper__ import Runtime


def _timelock2freq(*args, **kwargs):
    """
      TIMELOCK2FREQ transform the reconstructed dipole moment into  
        something that again resembles the physical input parameter in  
        the frequency domain.   
         
        This is needed after source reconstruction using FREQ2TIMELOCK.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/timelock2freq.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("timelock2freq", *args, **kwargs)
