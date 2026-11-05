from spm._runtime import Runtime


def spm_bgt_priors(*args, **kwargs):
    r"""
      Prior moments for a basal ganglia circuit  
        FORMAT [pE,pC] = spm_bgt_priors  
        only contains priors for intrinsic parameters  
        priors for extrinsic parameters are defined in spm_cmc_priors  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/dcm_meeg/spm_bgt_priors.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_bgt_priors", *args, **kwargs)
