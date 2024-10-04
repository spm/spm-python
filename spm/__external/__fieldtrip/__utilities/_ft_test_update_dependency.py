from spm.__wrap__ import _Runtime


def _ft_test_update_dependency(*args, **kwargs):
  """  FT_TEST_UPDATE_DEPENDENCY documentation is included inside ft_test  
    documentation.  
      
    See also FT_TEST, READLINES, WRITELINES  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/ft_test_update_dependency.m)
  """

  return _Runtime.call("ft_test_update_dependency", *args, **kwargs, nargout=0)
