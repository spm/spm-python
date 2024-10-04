from spm.__wrap__ import _Runtime


def tbx_cfg_fieldmap(*args, **kwargs):
  """  MATLABBATCH Configuration file for toolbox 'FieldMap'  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/FieldMap/tbx_cfg_fieldmap.m)
  """

  return _Runtime.call("tbx_cfg_fieldmap", *args, **kwargs)
