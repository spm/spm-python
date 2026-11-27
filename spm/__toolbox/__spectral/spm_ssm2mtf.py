from spm._runtime import Runtime


def spm_ssm2mtf(*args, **kwargs):
    r"""
      computes cross spectral density from state space representation  
        FORMAT [mtf,Hz] = spm_ssm2mtf(dfdx,dfdu,dgdx,Hz)  
         
        dfdx - Jacobian  
        dfdu - input matrix  [default: 1]  
        dgdx - output matrix [default: 1]  
        Hz   - frequencies   [default: based on maximum eigenvalue]  
         
        mtf  - directed or modulation transfer function  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/spectral/spm_ssm2mtf.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_ssm2mtf", *args, **kwargs)
