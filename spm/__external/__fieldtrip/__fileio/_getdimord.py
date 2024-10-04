from spm.__wrap__ import _Runtime


def _getdimord(*args, **kwargs):
  """  GETDIMORD determine the dimensions and order of a data field in a FieldTrip  
    structure.  
     
    Use as  
      dimord = getdimord(data, field)  
     
    See also GETDIMSIZ, GETDATFIELD, FIXDIMORD  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/getdimord.m)
  """

  return _Runtime.call("getdimord", *args, **kwargs)
