from spm._runtime import Runtime


def spm_DEM_eval_diff(*args, **kwargs):
    r"""
      Evaluate derivatives for DEM schemes  
        FORMAT [D] = spm_DEM_eval_diff(x,v,qp,M,bilinear)  
        v{i} - casual states  
        x(i) - hidden states  
        qp - conditional density of parameters  
         qp.p{i} - parameter deviates for i-th level  
         qp.u(i) - basis set  
         qp.x(i) - expansion point ( = prior expectation)  
        M        - model structure  
        bilinear - optional flag to suppress second-order derivatives  
         
        D        - derivatives  
          D.dgdv  
          ...  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_DEM_eval_diff.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_DEM_eval_diff", *args, **kwargs)
