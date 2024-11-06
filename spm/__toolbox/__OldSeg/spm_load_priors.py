from spm.__wrapper__ import Runtime


def spm_load_priors(*args, **kwargs):
    """
      Load the tissue probability maps for segmentation  
        FORMAT b0 = spm_load_priors(B)  
        B  - structures of image volume information (or filenames)  
        b0 - a cell array of tissue probabilities  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/OldSeg/spm_load_priors.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_load_priors", *args, **kwargs)
