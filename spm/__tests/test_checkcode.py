from spm.__wrapper__ import Runtime


def test_checkcode(*args, **kwargs):
  """  Test for possible problems in all of MATLAB code files  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_checkcode.m)
  """

  return Runtime.call("test_checkcode", *args, **kwargs)
