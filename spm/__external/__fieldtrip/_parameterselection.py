from spm.__wrap__ import _Runtime


def _parameterselection(*args, **kwargs):
  """  PARAMETERSELECTION selects the parameters that are present as a volume in the data  
    add that have a dimension that is compatible with the specified dimensions of the  
    volume, i.e. either as a vector or as a 3D volume.  
     
    Use as  
      [select] = parameterselection(param, data)  
    where  
      param    cell-array, or single string, can be 'all'  
      data     structure with anatomical or functional data  
      select   returns the selected parameters as a cell-array  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/parameterselection.m)
  """

  return _Runtime.call("parameterselection", *args, **kwargs)
