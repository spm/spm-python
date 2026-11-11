from spm._runtime import Runtime


def spm_ssm2csd(*args, **kwargs):
    r"""
      computes cross spectral density from state space representation  
        FORMAT [csd,Hz] = spm_ssm2csd(dfdx,dfdu,dgdx,Hz)  
         
        dfdx - Jacobian  
        dfdu - input matrix  [default: 1]  
        dgdx - output matrix [default: 1]  
        Hz   - frequencies   [default: based on maximum eigenvalue]  
         
        csd  - cross spectral density  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/spectral/spm_ssm2csd.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_ssm2csd", *args, **kwargs)
