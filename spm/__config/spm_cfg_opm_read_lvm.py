from spm.__wrap__ import _Runtime


def spm_cfg_opm_read_lvm(*args, **kwargs):
  """  Configuration file for reading lab view file  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_opm_read_lvm.m)
  """

  return _Runtime.call("spm_cfg_opm_read_lvm", *args, **kwargs)
