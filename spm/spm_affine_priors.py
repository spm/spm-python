from spm._runtime import Runtime


def spm_affine_priors(*args, **kwargs):
    r"""
      Distribution of the priors used in affine registration  
         
        The parameters for this distribution were derived empirically from 227  
        scans, that were matched to the ICBM space.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_affine_priors.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_affine_priors", *args, **kwargs)
