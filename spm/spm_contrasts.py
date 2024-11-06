from spm.__wrapper__ import Runtime


def spm_contrasts(*args, **kwargs):
    """
      Compute and store contrast parameters and inference SPM{.}  
        FORMAT SPM = spm_contrasts(SPM,Ic)  
         
        SPM  - SPM data structure  
        Ic   - indices of xCon to compute  
         
        This function fills in SPM.xCon and writes con_????, ess_???? and  
        spm?_???? images.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_contrasts.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_contrasts", *args, **kwargs)
