from spm.__wrap__ import _Runtime


def end2end_restingfMRI(*args, **kwargs):
  """  End-to-end test for resting dataset  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/end2end_restingfMRI.m)
  """

  return _Runtime.call("end2end_restingfMRI", *args, **kwargs)
