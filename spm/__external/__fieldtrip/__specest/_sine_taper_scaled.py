from spm._runtime import Runtime


def _sine_taper_scaled(*args, **kwargs):
    r"""
      Compute Riedel & Sidorenko sine tapers.  
        sine_taper_scaled(n, k) produces the first 2*k tapers of length n,  
        returned as the columns of d. The norm of the tapers will not be 1. The  
        norm is a function of the number of the taper in the sequence. This is to  
        mimick behavior of the scaling of the resulting powerspectra prior to  
        april 29, 2011. Before april 29, 2011, equivalent scaling was applied to  
        the powerspectra of the tapered data segments, prior to averaging.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/specest/private/sine_taper_scaled.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("sine_taper_scaled", *args, **kwargs)
