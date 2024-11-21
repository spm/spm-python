from spm.__wrapper__ import Runtime


def spm_DEM_eval_diff(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_DEM_eval_diff.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_DEM_eval_diff", *args, **kwargs)
