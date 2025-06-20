from spm._runtime import Runtime


def spm_immune_priors(*args, **kwargs):
    """
      Default priors for immune model  
        FORMAT [P,C] = spm_immune_priors  
        P - Prior expectations  
        C - Prior covariances  
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_immune_priors.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_immune_priors", *args, **kwargs)
