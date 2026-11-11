from spm._runtime import Runtime


def spm_vb_models(*args, **kwargs):
    r"""
      Specify models for ANOVAs  
        FORMAT [model] = spm_vb_models(SPM,factor)  
         
        SPM    - SPM structure  
        factor - Structure specifying factors and levels  
                 factor(i).name                  Name of ith factor  
                 factor(i).levels                Number of levels  
                 It is assumed that the levels of the first factor change  
                 slowest with condition  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_vb_models.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_vb_models", *args, **kwargs)
