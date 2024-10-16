from spm.__wrapper__ import Runtime


def read_16bit(*args, **kwargs):
  """  READ_16BIT read a stream of 16 bit values and converts them to doubles  
    This function is designed for EDF files and is implemented as mex  
    file for efficiency.  
     
    Use as  
      [dat] = read_16bit(filename, offset, numwords);  
     
    See also READ_24BIT  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/src/read_16bit.m)
  """

  return Runtime.call("read_16bit", *args, **kwargs)
