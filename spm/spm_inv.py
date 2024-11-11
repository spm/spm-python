from spm.__wrapper__ import Runtime


def spm_inv(*args, **kwargs):
    """
      Inverse for ill-conditioned matrices  
        FORMAT X = spm_inv(A,TOL)  
         
        A   - matrix  
        X   - inverse  
         
        TOL - tolerance: default = max(eps(norm(A,'inf'))*max(m,n),exp(-32))  
         
        This routine simply adds a small diagonal matrix to A and calls inv.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_inv.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_inv", *args, **kwargs)
