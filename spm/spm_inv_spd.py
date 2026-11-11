from spm._runtime import Runtime


def spm_inv_spd(*args, **kwargs):
    r"""
      Inverse for symmetric positive (semi)definite matrices  
        FORMAT X = spm_inv_spd(A,TOL)  
         
        A   - symmetric positive definite matrix (e.g. covariance or precision)  
        X   - inverse (should remain symmetric positive definite)  
         
        TOL - tolerance: default = exp(-32)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_inv_spd.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_inv_spd", *args, **kwargs)
