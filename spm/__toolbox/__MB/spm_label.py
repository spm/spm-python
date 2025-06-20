from spm._runtime import Runtime


def spm_label(*args, **kwargs):
    """
      Factorisation-based Image Labelling  
        FORMAT out = spm_label(cfg)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MB/spm_label.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_label", *args, **kwargs)
