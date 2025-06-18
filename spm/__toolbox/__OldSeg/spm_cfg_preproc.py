from mpython import Runtime


def spm_cfg_preproc(*args, **kwargs):
    """
      SPM Configuration file for toolbox 'Old Segment'
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/OldSeg/spm_cfg_preproc.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cfg_preproc", *args, **kwargs)
