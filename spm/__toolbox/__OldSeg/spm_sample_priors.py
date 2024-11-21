from spm.__wrapper__ import Runtime


def spm_sample_priors(*args, **kwargs):
    """
      Sample prior probability maps  
        FORMAT [s,ds1,ds2,ds3] = spm_sample_priors(b,x1,x2,x3,bg)  
        b           - a cell array containing the tissue probability  
                      data (see spm_load_priors)  
        x1,x2,x3    - coordinates to sample  
        bg          - background intensity (i.e. value for points  
                      outside FOV)  
        s           - sampled values  
        ds1,ds2,ds3 - spatial derivatives of sampled values  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/OldSeg/spm_sample_priors.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_sample_priors", *args, **kwargs)
