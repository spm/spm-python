from spm.__wrapper__ import Runtime


def spm_pairwise(*args, **kwargs):
    """
      Longitudinal registration of image pairs  
        FORMAT out = spm_pairwise(job)  
        See tbx_cfg_longitudinal.m for a description of the various fields.   
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Longitudinal/spm_pairwise.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_pairwise", *args, **kwargs)
