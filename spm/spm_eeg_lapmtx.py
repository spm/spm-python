from spm._runtime import Runtime


def spm_eeg_lapmtx(*args, **kwargs):
    """
      Laplace transform basis set for ERPs  
        FORMAT [T] = spm_eeg_lapmtx(pst)  
         
        pst - perstimulus time in ms  
         
        T   - Laplace transform basis set  
          
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_lapmtx.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_lapmtx", *args, **kwargs)
