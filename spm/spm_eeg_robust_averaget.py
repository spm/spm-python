from spm.__wrap__ import _Runtime


def spm_eeg_robust_averaget(*args, **kwargs):
  """  Apply robust averaging routine to data sets   
    FORMAT [B,Wf] = spm_eeg_robust_averaget(data,ks)  
    data   - data matrix to be averaged  
    ks     - offset of the weighting function (default: 3)  
     
    Wf     - estimated weights  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_robust_averaget.m)
  """

  return _Runtime.call("spm_eeg_robust_averaget", *args, **kwargs)
