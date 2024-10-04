from spm.__wrap__ import _Runtime


def spm_ar_pred(*args, **kwargs):
  """  Make predictions from Bayesian autoregressive models  
    FORMAT [y_pred,y,r2] = spm_ar_pred (Z,ar)  
     
    Z             [N x 1] univariate time series   
    ar            data structure - see spm_ar.m  
     
    y_pred        (one-step ahead) predictions   
    y             the values we are 'predicting'  
    r2            proportion of variance explained  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/spectral/spm_ar_pred.m)
  """

  return _Runtime.call("spm_ar_pred", *args, **kwargs)
