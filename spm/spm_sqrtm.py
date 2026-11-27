from spm._runtime import Runtime


def spm_sqrtm(*args, **kwargs):
    r"""
      Matrix square root for sparse symmetric positive semi-definite matrices  
        FORMAT [K] = spm_sqrtm(V)  
         
        This routine covers and extends sqrtm functionality by using a  
        computationally expedient approximation that can handle sparse symmetric  
        positive semi-definite matrices.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_sqrtm.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_sqrtm", *args, **kwargs)
