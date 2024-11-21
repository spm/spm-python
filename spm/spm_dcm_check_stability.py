from spm.__wrapper__ import Runtime


def spm_dcm_check_stability(*args, **kwargs):
    """
      Check stability of a DCM using Lyapunov exponent  
        FORMAT [is_stable,eigval] = spm_dcm_check_stability(DCM)  
         
        DCM        - DCM structure or its filename  
         
        is_stable  - returns 1 if stable, 0 if not stable  
        eigval     - Lyapunov exponent  
         
        This function checks the stability of a DCM by examining the eigenvalue  
        spectrum for the intrinsic connectivity matrix (Lyapunov exponent).  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_check_stability.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_check_stability", *args, **kwargs)
