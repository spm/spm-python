from spm.__wrap__ import _Runtime


def ft_struct2single(*args, **kwargs):
  """  FT_STRUCT2SINGLE converts all double precision numeric data in a structure  
    into single precision, which takes up half the amount of memory compared  
    to double precision. It will also convert plain matrices and cell-arrays.  
     
    Use as  
      x = ft_struct2single(x)  
     
    Starting from MATLAB 7.0, you can use single precision data in your  
    computations, i.e. you do not have to convert back to double precision.  
     
    MATLAB version 6.5 and older only support single precision for storing  
    data in memory or on disk, but do not allow computations on single  
    precision data. After reading a single precision structure from file, you  
    can convert it back with FT_STRUCT2DOUBLE.  
     
    See also FT_STRUCT2DOUBLE, FT_STRUCT2CHAR, FT_STRUCT2STRING  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/ft_struct2single.m)
  """

  return _Runtime.call("ft_struct2single", *args, **kwargs)
