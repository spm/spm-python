from spm._runtime import Runtime


def spm_bsd_csd(*args, **kwargs):
    r"""
      Compute cross-spectral density (CSD) matrix G and optional modes/noise structure H  
        for a Bayesian spectral density model.  
         
        Inputs:  
          P - Parameter structure (contains spectral parameters)  
          M - Model structure (contains frequency info, dipfit info, etc.)  
         
        Outputs:  
          G - Cross-spectral density matrix (nf x ns x ns)  
          H - (optional) Structure with spectral modes and noise components  
       _______________________________________________________________________  
        Copyright (C) 2024-2025 Wellcome Trust Centre for Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/BSD/spm_bsd_csd.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_bsd_csd", *args, **kwargs)
