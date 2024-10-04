from spm.__wrap__ import _Runtime


def spm_mvb_R2(*args, **kwargs):
  """  Return the proportion of variance explained by the (MVB) MAP estimates  
    FORMAT [R2,X,P] = spm_mvb_R2(MVB)  
     
    MVB - MVB structure  
    R2  - proportion of variance explained  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_mvb_R2.m)
  """

  return _Runtime.call("spm_mvb_R2", *args, **kwargs)
