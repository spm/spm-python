from spm.__wrapper__ import Runtime


def spm_dcm_fmri_csd_results(*args, **kwargs):
    """
      Review an estimated DCM for BOLD CSD  
        FORMAT spm_dcm_fmri_csd_results(DCM,action,fig)  
         
        Action:  
            'Spectral data'  
            'Coupling (A)'  
            'Coupling (C)'  
            'Inputs'  
            'Outputs'  
            'Transfer functions'  
            'Cross-spectra (BOLD)'  
            'Cross-spectra (neural)'  
            'Coherence (neural)'  
            'Covariance (neural)'  
            'Kernels'  
            'Functional connectivity'  
            'Location of regions'  
            'Quit'  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_fmri_csd_results.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_fmri_csd_results", *args, **kwargs, nargout=0)
