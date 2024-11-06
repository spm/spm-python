from spm.__wrapper__ import Runtime


def spm_ADEM_diff(*args, **kwargs):
    """
      Evaluate an active model given innovations z{i} and w{i}  
        FORMAT [u,dg,df] = spm_ADEM_diff(M,u)  
         
        M    - generative model  
         
        u.a - active states  
        u.v - causal states - updated  
        u.x - hidden states - updated  
        u.z - innovation (causal state)  
        u.w - innovation (hidden states)  
         
        dg.dv, ...  components of the Jacobian in generalised coordinates  
         
        The system is evaluated at the prior expectation of the parameters.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_ADEM_diff.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_ADEM_diff", *args, **kwargs)
