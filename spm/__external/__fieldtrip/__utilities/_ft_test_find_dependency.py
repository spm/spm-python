from spm.__wrap__ import _Runtime


def _ft_test_find_dependency(*args, **kwargs):
  """  FT_TEST_FIND_DEPENDENCY documentation is included inside ft_test  
    documentation.  
      
    See also FT_TEST  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/ft_test_find_dependency.m)
  """

  return _Runtime.call("ft_test_find_dependency", *args, **kwargs)
