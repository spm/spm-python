from spm._runtime import Runtime


def _save_large_cfg_fields(*args, **kwargs):
    r"""
      SAVE_LARGE_CFG_FIELDS is a helper function for ft_postamble_savevar and ft_postamble_savefig, and  
        is used for the cfg.reproducescript functionality.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/private/save_large_cfg_fields.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("save_large_cfg_fields", *args, **kwargs)
