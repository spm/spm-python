from spm._runtime import Runtime


def spm_label(*args, **kwargs):
    r"""
      Factorisation-based Image Labelling  
        FORMAT out = spm_label(cfg)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/MB/spm_label.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_label", *args, **kwargs)
