from spm.__wrapper__ import Runtime


def spm_mbnorm(*args, **kwargs):
    """
      Quick spatial normalisation with MB  
        FORMAT spm_mbnorm(P)  
        P - an array of filenames of scans (one per subject)  
         
        This is intended to show how Multi_brain can be used for  
        spatially normalising images.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MB/spm_mbnorm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mbnorm", *args, **kwargs)
