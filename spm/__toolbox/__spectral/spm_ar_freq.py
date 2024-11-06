from spm.__wrapper__ import Runtime


def spm_ar_freq(*args, **kwargs):
    """
      Compute spectra from AR coefficients  
        FORMAT [p] = spm_ar_freq (ar, freq, fs)  
         
        ar    AR model data structure (see spm_ar.m)  
        freq  [Nf x 1] vector containing list of frequencies  
        fs    sample rate  
         
        p     [Nf x 1] vector containing power estimates  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/spectral/spm_ar_freq.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_ar_freq", *args, **kwargs)
