from mpython import Runtime


def spm_bgt_priors(*args, **kwargs):
    """
      Prior moments for a basal ganglia circuit
        FORMAT [pE,pC] = spm_bgt_priors
        only contains priors for intrinsic parameters
        priors for extrinsic parameters are defined in spm_cmc_priors
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_bgt_priors.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_bgt_priors", *args, **kwargs)
