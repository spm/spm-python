from spm.__wrapper__ import Runtime


def _freq2timelock(*args, **kwargs):
    """
      FREQ2TIMELOCK  transform the frequency data into something  
        on which the timelocked source reconstruction methods can  
        perform their trick.  
         
        This function also performs frequency and channel selection, using  
          cfg.frequency  
          cfg.channel  
         
        After source reconstruction, you should use TIMELOCK2FREQ.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/freq2timelock.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("freq2timelock", *args, **kwargs)
