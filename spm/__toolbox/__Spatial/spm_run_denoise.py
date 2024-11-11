from spm.__wrapper__ import Runtime


def spm_run_denoise(*args, **kwargs):
    """
      FORMAT out = spm_run_denoise(opt,cfg)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Spatial/spm_run_denoise.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_run_denoise", *args, **kwargs)
