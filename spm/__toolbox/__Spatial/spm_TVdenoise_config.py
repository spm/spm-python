from mpython import Runtime


def spm_TVdenoise_config(*args, **kwargs):
    """
      SPM Configuration file for total variation denoising
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Spatial/spm_TVdenoise_config.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_TVdenoise_config", *args, **kwargs)
