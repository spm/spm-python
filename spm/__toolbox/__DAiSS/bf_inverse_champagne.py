from spm.__wrap__ import _Runtime


def bf_inverse_champagne(*args, **kwargs):
  """  Computes Champagne filters  
     
    See Owen et al. Performance evaluation of the Champagne source   
    reconstruction algorithm on simulated and real M/EEG data. Neuroimage.  
    2012 Mar;60(1):305-23  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_inverse_champagne.m)
  """

  return _Runtime.call("bf_inverse_champagne", *args, **kwargs)
