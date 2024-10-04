from spm.__wrap__ import _Runtime


def test_spm_trace(*args, **kwargs):
  """  Unit Tests for spm_trace  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_spm_trace.m)
  """

  return _Runtime.call("test_spm_trace", *args, **kwargs)
