from spm.__wrap__ import _Runtime


def _ft_test_moxunit_run(*args, **kwargs):
  """  FT_TEST_MOXUNIT_RUN documentation is included inside ft_test  
    documentation.  
      
    See also FT_TEST  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/ft_test_moxunit_run.m)
  """

  return _Runtime.call("ft_test_moxunit_run", *args, **kwargs)
