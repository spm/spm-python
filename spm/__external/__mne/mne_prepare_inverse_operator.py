from spm.__wrap__ import _Runtime


def mne_prepare_inverse_operator(*args, **kwargs):
  """   
    [inv] = mne_prepare_inverse_operator(orig,nave,lambda2,dSPM,sLORETA)  
     
    Prepare for actually computing the inverse  
     
    orig        - The inverse operator structure read from a file  
    nave        - Number of averages (scales the noise covariance)  
    lambda2     - The regularization factor  
    dSPM        - Compute the noise-normalization factors for dSPM?  
    sLORETA     - Compute the noise-normalization factors for sLORETA?  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_prepare_inverse_operator.m)
  """

  return _Runtime.call("mne_prepare_inverse_operator", *args, **kwargs)
