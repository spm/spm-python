from spm._runtime import Runtime


def spm_shoot_defaults(*args, **kwargs):
    """
      Defaults file  
        FORMAT d = spm_shoot_defaults  
        This file contains settings that are intended to be customised  
        according to taste.  Some of them will influence the speed/accuracy  
        tradeoff, whereas others are various regularisation settings  
        (registration and template blurring)...  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Shoot/spm_shoot_defaults.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_shoot_defaults", *args, **kwargs)
