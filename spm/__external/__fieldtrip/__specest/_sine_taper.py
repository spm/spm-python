from spm._runtime import Runtime


def _sine_taper(*args, **kwargs):
    r"""
      Compute Riedel & Sidorenko sine tapers.  
        sine_taper(n, k) produces the first 2*k tapers of length n,  
        returned as the columns of d.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/specest/private/sine_taper.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("sine_taper", *args, **kwargs)
