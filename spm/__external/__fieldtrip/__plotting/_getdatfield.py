from spm.__wrapper__ import Runtime


def _getdatfield(*args, **kwargs):
  """  GETDATFIELD  
     
    Use as  
      [datfield, dimord] = getdatfield(data)  
    where the output arguments are cell-arrays.  
     
    See also GETDIMORD, GETDIMSIZ  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/private/getdatfield.m)
  """

  return Runtime.call("getdatfield", *args, **kwargs)
