from spm._runtime import Runtime


def _freq2cumtapcnt(*args, **kwargs):
    r"""
    freq2cumtapcnt is a function.  
          freq = freq2cumtapcnt(freq, fsample)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/freq2cumtapcnt.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("freq2cumtapcnt", *args, **kwargs)
