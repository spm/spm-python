from spm._runtime import Runtime


def spm_load_priors(*args, **kwargs):
    r"""
      Load the tissue probability maps for segmentation  
        FORMAT b0 = spm_load_priors(B)  
        B  - structures of image volume information (or filenames)  
        b0 - a cell array of tissue probabilities  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/OldSeg/spm_load_priors.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_load_priors", *args, **kwargs)
