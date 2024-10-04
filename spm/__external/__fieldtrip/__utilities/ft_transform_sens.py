from spm.__wrap__ import _Runtime


def ft_transform_sens(*args, **kwargs):
  """  This function is a backward compatibility wrapper for existing MATLAB scripts  
    that call a function that is not part of the FieldTrip toolbox any more.  
     
    Please update your code to make it future-proof.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/ft_transform_sens.m)
  """

  return _Runtime.call("ft_transform_sens", *args, **kwargs)
