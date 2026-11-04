from spm._runtime import Runtime


def spm_inv(*args, **kwargs):
    r"""
      Inverse for ill-conditioned matrices  
        FORMAT X = spm_inv(A,TOL)  
         
        A   - matrix  
        X   - inverse  
         
        TOL - tolerance: default = max(eps(norm(A,'inf'))*max(m,n),exp(-32))  
         
        This routine simply adds a small diagonal matrix to A and calls inv.m  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_inv.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_inv", *args, **kwargs)
