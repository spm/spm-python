from spm._runtime import Runtime


def spm_bsd_priors(*args, **kwargs):
    r"""
      spm_bsd_priors.m  
        Generate prior means, default values, and covariances for BSD model parameters.  
          
        Usage:  
          [pE, pC, pV] = spm_bsd_priors(fqs, ns, X, M, pE, pC)  
         
        Inputs:  
          fqs - Frequency bands (cell array or numeric)  
          ns  - Number of sources  
          X   - External input matrix  
          M   - Model structure (must contain fields 'Hz' and 'sharefreqs')  
          pE  - (Optional) Prior means structure  
          pC  - (Optional) Prior covariances structure  
         
        Outputs:  
          pE  - Prior means structure  
          pC  - Prior covariances structure  
          pV  - Default values structure  
         
       _______________________________________________________________________  
        Copyright (C) 2024-2025 Wellcome Trust Centre for Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/BSD/spm_bsd_priors.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_bsd_priors", *args, **kwargs)
