from spm._runtime import Runtime


def spm_dcm_erp_results(*args, **kwargs):
    """
      Results for ERP Dynamic Causal Modeling (DCM)  
        FORMAT spm_dcm_erp_results(DCM,'ERPs (mode)');  
        FORMAT spm_dcm_erp_results(DCM,'ERPs (sources)');  
        FORMAT spm_dcm_erp_results(DCM,'Coupling (A)');  
        FORMAT spm_dcm_erp_results(DCM,'Coupling (B)');  
        FORMAT spm_dcm_erp_results(DCM,'Coupling (C)');  
        FORMAT spm_dcm_erp_results(DCM,'trial-specific effects');  
        FORMAT spm_dcm_erp_results(DCM,'Input');  
        FORMAT spm_dcm_erp_results(DCM,'Response');  
        FORMAT spm_dcm_erp_results(DCM,'Response (image)');  
        FORMAT spm_dcm_erp_results(DCM,'Scalp maps');  
        FORMAT spm_dcm_erp_results(DCM,'Data');  
         
       __________________________________________________________________________  
         
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_dcm_erp_results.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dcm_erp_results", *args, **kwargs)
