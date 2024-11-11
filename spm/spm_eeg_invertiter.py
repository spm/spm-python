from spm.__wrapper__ import Runtime


def spm_eeg_invertiter(*args, **kwargs):
    """
       Function to perform several MSP type inversions with different  
         pseudo-randomly selected priors- in this case single cortical patches  
         
        Npatchiter: number of iterations  
        funcname is name of MSP alogorithm: current (spm_eeg_invert) or classic (spm_eeg_invert_classic)  
        patchind is an optional list of indices of vertices which will be patch  
        centres. patchind will have size Npatchiter*Np (where Np is number of patches set in  
        inverse.Np )  
        if  Dtest{1}.inv{val}.inverse.mergeflag==1 then merges Npatchiter posterior current  
        distributions, else replaces posterior with best of the iterations.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_invertiter.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_invertiter", *args, **kwargs)
