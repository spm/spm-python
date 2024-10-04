from spm.__wrap__ import _Runtime


def spm_mar_pred(*args, **kwargs):
  """  Get predictions from MAR model  
    FORMAT [y,y_pred] = spm_mar_pred (X,mar)  
     
    X              T-by-d matrix containing d-variate time series0)  
     
    mar            see spm_mar.m for data structure  
     
    y              Target values  
    y_pred         Predicted values  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/spectral/spm_mar_pred.m)
  """

  return _Runtime.call("spm_mar_pred", *args, **kwargs)
