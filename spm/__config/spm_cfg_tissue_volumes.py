from spm.__wrap__ import _Runtime


def spm_cfg_tissue_volumes(*args, **kwargs):
  """  SPM Configuration file for Tissue Volumes  
     
    See also: spm_run_tissue_volumes, spm_summarise  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_tissue_volumes.m)
  """

  return _Runtime.call("spm_cfg_tissue_volumes", *args, **kwargs)
