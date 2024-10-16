from spm.__wrapper__ import Runtime


def _makessense(*args, **kwargs):
  """  MAKESSENSE determines whether a some specific fields in a FieldTrip data structure  
    make sense.  
     
    Use as  
      status = makessense(data, field)  
     
    See also GETDIMORD, GETDIMSIZ, GETDATFIELD  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/makessense.m)
  """

  return Runtime.call("makessense", *args, **kwargs)
