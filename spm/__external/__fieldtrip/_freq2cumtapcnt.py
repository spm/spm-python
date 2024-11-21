from spm.__wrapper__ import Runtime


def _freq2cumtapcnt(*args, **kwargs):
    """
    freq2cumtapcnt is a function.  
          freq = freq2cumtapcnt(freq, fsample)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/freq2cumtapcnt.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("freq2cumtapcnt", *args, **kwargs)
