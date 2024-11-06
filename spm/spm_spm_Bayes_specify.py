from spm.__wrapper__ import Runtime


def spm_spm_Bayes_specify(*args, **kwargs):
    """
      Specification of a PEB model for a voxel with empirical priors  
         
        SPM - standard SPM structure (see spm_spm.m)  
         
        sP(i).P{1}.X - 1st level design matrix  
        sP(i).P{1}.C - 1st level prior covariance (see spm_est_non_sphericity.m)  
        sP(i).P{2}.X - 2nd level expected values (zeros)  
        sP(i).P{2}.C - 2nd level prior covariance (empirical prior)  
        sP(i).u      - indices of scans  
        sP(i).v      - indices of regressors  
         
        ...for each separable partition (e.g. session) of the design i  
       __________________________________________________________________________  
         
        Creates a structure for a 2-level hierarchical regression model,   
        compatible with spm_PEB.m. The spatial covariance of the betas over   
        voxels is used as an empirical prior for voxel-wise estimation.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_spm_Bayes_specify.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_spm_Bayes_specify", *args, **kwargs)
