from spm._runtime import Runtime


def spm_find_pC(*args, **kwargs):
    r"""
      Utility routine that finds the indices of non-zero covariance  
        FORMAT [i,pC,pE,Np] = spm_find_pC(pC,pE,fields)  
        FORMAT [i,pC,pE,Np] = spm_find_pC(DCM,fields)  
        FORMAT [i,pC,pE,Np] = spm_find_pC(DCM)  
          
        pC     - covariance matrix or variance structure  
        pE     - parameter structure  
        fields - desired fields of pE  
         
        or  
         
        DCM    - DCM structure  
         
        i      - find(diag(pC) > TOL)  
        rC     - reduced covariances  
        rE     - reduced expectation  
          
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_find_pC.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_find_pC", *args, **kwargs)
