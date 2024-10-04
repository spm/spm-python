from spm.__wrap__ import _Runtime


def _getdatfield(*args, **kwargs):
  """  GETDATFIELD  
     
    Use as  
      [datfield, dimord] = getdatfield(data)  
    where the output arguments are cell-arrays.  
     
    See also GETDIMORD, GETDIMSIZ  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/getdatfield.m)
  """

  return _Runtime.call("getdatfield", *args, **kwargs)
