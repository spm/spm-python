from spm.__wrapper__ import Runtime


def spm_ness_cond(*args, **kwargs):
    """
      Conditional moments of a Gaussian density (polynomial parameterisation)  
        FORMAT [m,C] = spm_ness_cond(n,K,Sp,ni,x)  
       --------------------------------------------------------------------------  
        n  - Dimensionality of state space  
        K  - Order of polynomial expansion (K = 3 corresponds to quadratic)  
        Sp - Polynomial coefficients or parameters of log density  
          
        ni - States on which to condition (Optional)  
        x  - Values of states [default: 0]  
         
        m  - (Conditional) mean  
        C  - (Conditional) covariance  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_ness_cond.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_ness_cond", *args, **kwargs)
