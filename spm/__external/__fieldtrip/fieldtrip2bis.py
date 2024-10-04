from spm.__wrap__ import _Runtime


def fieldtrip2bis(*args, **kwargs):
  """  FIELDTRIP2BIS writes BioImage Suite .mgrid files with eletrode   
    positions in 'xyz' coordinates using a elec datatype structure and the   
    corresponding MRI volume   
     
    Use as  
      fieldtrip2bis('Subject_grid.mgrid', elec, 'Subject_MR.nii')  
     
    See also BIS2FIELDTRIP, FT_WRITE_SENS, WRITE_BIOIMAGE_MGRID  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fieldtrip2bis.m)
  """

  return _Runtime.call("fieldtrip2bis", *args, **kwargs, nargout=0)
