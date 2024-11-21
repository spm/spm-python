from spm.__wrapper__ import Runtime


def spm_inv_spd(*args, **kwargs):
    """
      Inverse for symmetric positive (semi)definite matrices  
        FORMAT X = spm_inv_spd(A,TOL)  
         
        A   - symmetric positive definite matrix (e.g. covariance or precision)  
        X   - inverse (should remain symmetric positive definite)  
         
        TOL - tolerance: default = exp(-32)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_inv_spd.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_inv_spd", *args, **kwargs)
