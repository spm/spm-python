from spm.__wrapper__ import Runtime


def spm_cfg_opm_read_lvm(*args, **kwargs):
    """
      Configuration file for reading lab view file  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_cfg_opm_read_lvm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_cfg_opm_read_lvm", *args, **kwargs)
