from spm.__wrapper__ import Runtime


def spm_dcm_load(*args, **kwargs):
    """
      Load a cell array of DCM filenames into a subjects x models cell array  
        FORMAT DCM = spm_dcm_load(P)  
         
        P        - a DCM's filename or  
                 - a GCM's filename (which contains a cell array of DCM files) or  
                 - a cell array of DCM filenames or  
                 - a character array of DCM filenames  
        save_mem - (Optional) if true, only loads priors, posteriors and F for  
                   models 2-N  
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_load.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_load", *args, **kwargs)
