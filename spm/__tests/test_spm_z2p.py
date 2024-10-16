from spm.__wrapper__ import Runtime


def test_spm_z2p(*args, **kwargs):
  """  Unit Tests for spm_z2p  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_spm_z2p.m)
  """

  return Runtime.call("test_spm_z2p", *args, **kwargs)
