from spm.__wrapper__ import Runtime


def spm_robust_glm(*args, **kwargs):
    """
      Apply robust GLM  
        FORMAT [B, W] = spm_robust_glm(Y, X, dim, ks)  
        Y      - data matrix  
        X      - design matrix  
        dim    - the dimension along which the function will work  
        ks     - offset of the weighting function (default: 3)  
         
        OUTPUT:  
        B      - parameter estimates  
        W      - estimated weights  
         
        Implementation of:  
          Wager TD, Keller MC, Lacey SC, Jonides J.  
          Increased sensitivity in neuroimaging analyses using robust regression.  
          Neuroimage. 2005 May 15;26(1):99-113  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_robust_glm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_robust_glm", *args, **kwargs)
