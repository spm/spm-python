from spm.__wrapper__ import Runtime


def spm_ssm2csd(*args, **kwargs):
    """
      computes cross spectral density from state space representation  
        FORMAT [csd,Hz] = spm_ssm2csd(dfdx,dfdu,dgdx,Hz)  
         
        dfdx - Jacobian  
        dfdu - input matrix  [default: 1]  
        dgdx - output matrix [default: 1]  
        Hz   - frequencies   [default: based on maximum eigenvalue]  
         
        csd  - cross spectral density  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/spectral/spm_ssm2csd.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_ssm2csd", *args, **kwargs)
