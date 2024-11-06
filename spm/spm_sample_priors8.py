from spm.__wrapper__ import Runtime


def spm_sample_priors8(*args, **kwargs):
    """
      Sample prior probability maps  
        FORMAT [s,ds1,ds2,ds3] = spm_sample_priors8(tpm,x1,x2,x3)  
        b           - a cell array containing the tissue probability  
                      data (see spm_load_priors)  
        x1,x2,x3    - coordinates to sample  
        s           - sampled values  
        ds1,ds2,ds3 - spatial derivatives of sampled values  
         
        This function is intended to be used in conjunction with spm_load_priors.  
        V = spm_vol(P);  
        T = spm_load_priors(V);  
        B = spm_sample_priors(T,X,Y,Z);  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_sample_priors8.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_sample_priors8", *args, **kwargs)
