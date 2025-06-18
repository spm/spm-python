from mpython import Runtime


def tbx_cfg_mb(*args, **kwargs):
    """
      MATLABBATCH Configuration file for toolbox 'Multi-Brain'
       _____________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MB/tbx_cfg_mb.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("tbx_cfg_mb", *args, **kwargs)
