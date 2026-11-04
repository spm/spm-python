from spm._runtime import Runtime


def spm_ADEM_update(*args, **kwargs):
    r"""
      Update ADEM structure using conditional expectations  
        FORMAT DEM = spm_ADEM_update(DEM,COV)  
         
        DEM - DEM structure  
        COV - Covariance of parameter (P) fluctuations (E): P(i + 1) = P(i) + E  
            - where cov(E) = COV*pC  
         
        This routine updates posterior expectations about states and parameters  
        by replacing prior expectations with posterior expectations (and  
        similarly updating hidden states and causes to the final iteration). If  
        called with an extra argument, the posterior variances of the  
        parameters are also updated.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_ADEM_update.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_ADEM_update", *args, **kwargs)
