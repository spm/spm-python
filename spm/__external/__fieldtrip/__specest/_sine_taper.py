from spm.__wrapper__ import Runtime


def _sine_taper(*args, **kwargs):
    """
      Compute Riedel & Sidorenko sine tapers.  
        sine_taper(n, k) produces the first 2*k tapers of length n,  
        returned as the columns of d.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/specest/private/sine_taper.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("sine_taper", *args, **kwargs)
