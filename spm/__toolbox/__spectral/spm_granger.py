from spm._runtime import Runtime


def spm_granger(*args, **kwargs):
    r"""
      Compute Granger causality matrix   
        FORMAT [G,Psig] = spm_granger (mar)  
         
        mar            MAR data structure (see spm_mar.m)   
         
        G              [d x d] matrix with i,jth entry equal to 1 if  
                       time series j 'Granger causes' time series i.   
                       All other entries set to 0.  
         
        Psig           [d x d] matrix of corresponding significance values  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/spectral/spm_granger.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_granger", *args, **kwargs)
