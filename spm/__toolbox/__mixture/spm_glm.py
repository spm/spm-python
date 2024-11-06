from spm.__wrapper__ import Runtime


def spm_glm(*args, **kwargs):
    """
      Fit a Bayesian GLM   
        FORMAT [rglm] = spm_glm (y,X,alpha,verbose)  
         
        This function is called by spm_robust_glm if m==1  
          
        y          [N x 1] data vector  
        X          [N x p] design matrix  
        alpha      [1 x 1] weight precision (default=0.001)  
        verbose    0/1 to printout inner workings (default=0)  
         
        rglm       Returned model   
         
        -------------------------------------------------------  
        The fields in rglm are:  
         
        m                The number of error components  
        fm               The negative free energy  
         
                         In the field priors:  
         
        b_0,c_0          Gamma parameters for precisions  
         
                         In the field posts:  
         
        b,c              Gamma parameters for precisions  
        w_mean           Mean estimated regression coefficients  
        w_cov            Covariance of regression coefficients  
         
                         Mean posterior values:  
        variances        variances (1./(b.*c))  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mixture/spm_glm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_glm", *args, **kwargs)
