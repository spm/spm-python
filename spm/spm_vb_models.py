from spm.__wrapper__ import Runtime


def spm_vb_models(*args, **kwargs):
    """
      Specify models for ANOVAs  
        FORMAT [model] = spm_vb_models(SPM,factor)  
         
        SPM    - SPM structure  
        factor - Structure specifying factors and levels  
                 factor(i).name                  Name of ith factor  
                 factor(i).levels                Number of levels  
                 It is assumed that the levels of the first factor change  
                 slowest with condition  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_vb_models.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_vb_models", *args, **kwargs)
