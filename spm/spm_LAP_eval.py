from spm._runtime import Runtime


def spm_LAP_eval(*args, **kwargs):
    r"""
      Evaluate precisions for a LAP model  
        FORMAT [p,dp] = spm_LAP_eval(M,qu,qh)  
         
        p.h     - vector of precisions for causal states (v)  
        p.g     - vector of precisions for hidden states (x)  
         
        dp.h.dx - dp.h/dx  
        dp.h.dv - dp.h/dv  
        dp.h.dh - dp.h/dh  
         
        dp.g.dx - dp.g/dx  
        dp.g.dv - dp.g/dv  
        dp.g.dg - dp.g/dg  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_LAP_eval.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_LAP_eval", *args, **kwargs)
