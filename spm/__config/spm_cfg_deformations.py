from mpython import Runtime


def spm_cfg_deformations(*args, **kwargs):
    """
      Configuration file for deformation jobs
       _______________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_cfg_deformations.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cfg_deformations", *args, **kwargs)
