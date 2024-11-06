from spm.__wrapper__ import Runtime


def spm_dcm_csd_results(*args, **kwargs):
    """
      Results for CSD (SSR) Dynamic Causal Modeling (DCM)  
        FORMAT spm_dcm_csd_results(DCM,'spectral data');  
        FORMAT spm_dcm_csd_results(DCM,'Coupling (A)');  
        FORMAT spm_dcm_csd_results(DCM,'Coupling (B)');  
        FORMAT spm_dcm_csd_results(DCM,'Coupling (C)');  
        FORMAT spm_dcm_csd_results(DCM,'trial-specific effects');  
        FORMAT spm_dcm_csd_results(DCM,'Input');  
        FORMAT spm_dcm_csd_results(DCM,'Transfer functions');  
        FORMAT spm_dcm_csd_results(DCM,'Cross-spectra (sources)')  
        FORMAT spm_dcm_csd_results(DCM,'Cross-spectra (channels)')  
        FORMAT spm_dcm_csd_results(DCM,'Coherence (sources)')  
        FORMAT spm_dcm_csd_results(DCM,'Coherence (channels)')  
        FORMAT spm_dcm_csd_results(DCM,'Covariance (sources)')  
        FORMAT spm_dcm_csd_results(DCM,'Covariance (channels)')  
        FORMAT spm_dcm_csd_results(DCM,'Dipoles');  
                         
       ___________________________________________________________________________  
         
        DCM is a causal modelling procedure for dynamical systems in which  
        causality is inherent in the differential equations that specify the model.  
        The basic idea is to treat the system of interest, in this case the brain,  
        as an input-state-output system.  By perturbing the system with known  
        inputs, measured responses are used to estimate various parameters that  
        govern the evolution of brain states.  Although there are no restrictions  
        on the parameterisation of the model, a bilinear approximation affords a  
        simple re-parameterisation in terms of effective connectivity.  This  
        effective connectivity can be latent or intrinsic or, through bilinear  
        terms, model input-dependent changes in effective connectivity.  Parameter  
        estimation proceeds using fairly standard approaches to system  
        identification that rest upon Bayesian inference.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_dcm_csd_results.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_csd_results", *args, **kwargs, nargout=0)
