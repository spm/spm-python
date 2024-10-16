from spm.__wrapper__ import Runtime


def _save_large_cfg_fields(*args, **kwargs):
  """  SAVE_LARGE_CFG_FIELDS is a helper function for ft_postamble_savevar and ft_postamble_savefig, and  
    is used for the cfg.reproducescript functionality.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/save_large_cfg_fields.m)
  """

  return Runtime.call("save_large_cfg_fields", *args, **kwargs)
