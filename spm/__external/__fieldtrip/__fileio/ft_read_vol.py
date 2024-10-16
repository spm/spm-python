from spm.__wrapper__ import Runtime


def ft_read_vol(*args, **kwargs):
  """  This function is a backward compatibility wrapper for existing MATLAB scripts  
    that call a function that is not part of the FieldTrip toolbox any more.  
     
    Please update your code to make it future-proof.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/ft_read_vol.m)
  """

  return Runtime.call("ft_read_vol", *args, **kwargs)
