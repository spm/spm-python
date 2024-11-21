from spm.__wrapper__ import Runtime


def spm_dwtmtx(*args, **kwargs):
    """
      Create basis functions for Discrete (Haar) Wavelet Transform  
        FORMAT H = spm_dwtmtx(N,K,T)  
         
          N - dimension  
          K - order: number of basis functions = N/K  
         
          T - option flag for thinning eccentric wavelets [default: false]  
       __________________________________________________________________________  
         
        spm_dwtmtx creates a matrix for the first few basis functions of a one  
        dimensional Haar Discrete Wavelet transform.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dwtmtx.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dwtmtx", *args, **kwargs)
