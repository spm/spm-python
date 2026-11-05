from spm._runtime import Runtime


def spm_mar_pred(*args, **kwargs):
    r"""
      Get predictions from MAR model  
        FORMAT [y,y_pred] = spm_mar_pred (X,mar)  
         
        X              T-by-d matrix containing d-variate time series0)  
         
        mar            see spm_mar.m for data structure  
         
        y              Target values  
        y_pred         Predicted values  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/spectral/spm_mar_pred.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mar_pred", *args, **kwargs)
