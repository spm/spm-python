from spm._runtime import Runtime


def spm_cfg(*args, **kwargs):
    """
      SPM Configuration file for MATLABBATCH  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_cfg.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cfg", *args, **kwargs)
