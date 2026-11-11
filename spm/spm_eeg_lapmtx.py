from spm._runtime import Runtime


def spm_eeg_lapmtx(*args, **kwargs):
    r"""
      Laplace transform basis set for ERPs  
        FORMAT [T] = spm_eeg_lapmtx(pst)  
         
        pst - perstimulus time in ms  
         
        T   - Laplace transform basis set  
          
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_lapmtx.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_lapmtx", *args, **kwargs)
