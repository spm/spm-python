from spm._runtime import Runtime


def spm_ssm2ccf(*args, **kwargs):
    r"""
      computes cross covariance from state space representation  
        FORMAT [ccf,pst] = spm_ssm2ccf(dfdx,dfdu,dgdx,Hz)  
         
        dfdx - Jacobian  
        dfdu - input matrix  [default: 1]  
        dgdx - output matrix [default: 1]  
        Hz   - frequencies  
         
        ccf  - cross covariance functions  
        pst  - vector of lags for evaluation (seconds)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/spectral/spm_ssm2ccf.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_ssm2ccf", *args, **kwargs)
