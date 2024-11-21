from spm.__wrapper__ import Runtime


def spm_sqrtm(*args, **kwargs):
    """
      Matrix square root for sparse symmetric positive semi-definite matrices  
        FORMAT [K] = spm_sqrtm(V)  
         
        This routine covers and extends sqrtm functionality by using a  
        computationally expedient approximation that can handle sparse symmetric  
        positive semi-definite matrices.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_sqrtm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_sqrtm", *args, **kwargs)
