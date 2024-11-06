from spm.__wrapper__ import Runtime


def _sine_taper_scaled(*args, **kwargs):
    """
      Compute Riedel & Sidorenko sine tapers.  
        sine_taper_scaled(n, k) produces the first 2*k tapers of length n,  
        returned as the columns of d. The norm of the tapers will not be 1. The  
        norm is a function of the number of the taper in the sequence. This is to  
        mimick behavior of the scaling of the resulting powerspectra prior to  
        april 29, 2011. Before april 29, 2011, equivalent scaling was applied to  
        the powerspectra of the tapered data segments, prior to averaging.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/specest/private/sine_taper_scaled.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("sine_taper_scaled", *args, **kwargs)
