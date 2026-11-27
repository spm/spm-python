from spm._runtime import Runtime


def spm_ssm2ker(*args, **kwargs):
    r"""
      computes cross spectral density from state space representation  
        FORMAT [ker,pst] = spm_ssm2ker(dfdx,dfdu,dgdx,pst)  
         
        dfdx - Jacobian  
        dfdu - input matrix  [default: 1]  
        dgdx - output matrix [default: 1]  
        pst  - time          [default: based on maximum eigenvalue]  
         
        ker  - first-order (Volterra) kernels  
          
        NB: Please see notes at the end of this routine for a demonstration of  
        the systems analyses using the suite of spm_???2??.m routines  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/spectral/spm_ssm2ker.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_ssm2ker", *args, **kwargs)
