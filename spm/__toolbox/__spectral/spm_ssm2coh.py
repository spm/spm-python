from spm._runtime import Runtime


def spm_ssm2coh(*args, **kwargs):
    r"""
      computes coherence from state space representation  
        FORMAT [coh,fsd] = spm_ssm2coh(dfdx,dfdu,dgdx,Hz)  
         
        dfdx - Jacobian  
        dfdu - input matrix  [default: 1]  
        dgdx - output matrix [default: 1]  
        Hz   - frequencies   [default: based on maximum eigenvalue]  
         
        coh            - coherence  
        fsd            - frequency specific delay (seconds)   
                       - phase-delay/radial frequency  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/spectral/spm_ssm2coh.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_ssm2coh", *args, **kwargs)
