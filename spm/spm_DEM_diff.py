from spm._runtime import Runtime


def spm_DEM_diff(*args, **kwargs):
    r"""
      Evaluate an active model given innovations z{i} and w{i}  
        FORMAT [u,dg,df] = spm_DEM_diff(M,u)  
         
        M    - generative model  
         
        u.v - causal states - updated  
        u.x - hidden states - updated  
        u.z - innovation (causal state)  
        u.w - innovation (hidden states)  
        u.a - [active states]  
         
        dg.dv, ...  components of the Jacobian in generalised coordinates  
         
        The system is evaluated at the prior expectation of the parameters  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_DEM_diff.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_DEM_diff", *args, **kwargs)
