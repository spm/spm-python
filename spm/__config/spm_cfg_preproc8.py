from mpython import Runtime


def spm_cfg_preproc8(*args, **kwargs):
    """
      Configuration file for 'Combined Segmentation and Spatial Normalisation'
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_cfg_preproc8.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cfg_preproc8", *args, **kwargs)
