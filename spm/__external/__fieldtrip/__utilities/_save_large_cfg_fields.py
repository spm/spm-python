from mpython import Runtime


def _save_large_cfg_fields(*args, **kwargs):
    """
      SAVE_LARGE_CFG_FIELDS is a helper function for ft_postamble_savevar and ft_postamble_savefig, and
        is used for the cfg.reproducescript functionality.


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/save_large_cfg_fields.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("save_large_cfg_fields", *args, **kwargs)
