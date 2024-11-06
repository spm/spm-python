from spm.__wrapper__ import Runtime


def spm_mb_fit(*args, **kwargs):
    """
      Multi-Brain - Groupwise normalisation and segmentation of images  
        FORMAT [dat,sett,mu] = spm_mb_fit(dat,sett)  
         
        OUTPUT  
        dat                 - struct of length N storing each subject's information  
        mu                  - array with template data  
        sett  (inputParser) - struct storing final algorithm settings  
        model (inputParser) - struct storing shape and appearance model  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MB/spm_mb_fit.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mb_fit", *args, **kwargs)
