from spm.__wrapper__ import Runtime


def spm_find_pC(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_find_pC.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_find_pC", *args, **kwargs)
