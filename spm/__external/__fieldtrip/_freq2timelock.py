from spm._runtime import Runtime


def _freq2timelock(*args, **kwargs):
    r"""
      FREQ2TIMELOCK  transform the frequency data into something  
        on which the timelocked source reconstruction methods can  
        perform their trick.  
         
        This function also performs frequency and channel selection, using  
          cfg.frequency  
          cfg.channel  
         
        After source reconstruction, you should use TIMELOCK2FREQ.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/freq2timelock.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("freq2timelock", *args, **kwargs)
