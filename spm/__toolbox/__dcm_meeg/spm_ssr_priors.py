from spm._runtime import Runtime


def spm_ssr_priors(*args, **kwargs):
    r"""
      Augments prior moments of a neural mass model for CSD analyses  
        FORMAT [pE,pC] = spm_ssr_priors(pE,pC)  
         
        pE - prior expectation  
         
        adds  
         
        input and noise parameters  
       --------------------------------------------------------------------------  
           pE.a - neuronal innovations         - amplitude and exponent  
           pE.b - channel noise (non-specific) - amplitude and exponent  
           pE.c - channel noise (specific)     - amplitude and exponent  
           pE.d - neuronal innovations         - basis set  coefficients  
           pE.f - filtering                    - polynomial coefficients  
         
       --------------------------------------------------------------------------  
         
        pC - prior (co)variances  
         
        Because priors are specified under log normal assumptions, most  
        parameters are simply scaling coefficients with a prior expectation  
        and variance of one.  After log transform this renders pE = 0 and  
        pC = 1;  The prior expectations of what they scale are specified in  
        spm_lfp_fx  
       __________________________________________________________________________  
         
        David O, Friston KJ (2003) A neural mass model for MEG/EEG: coupling and  
        neuronal dynamics. NeuroImage 20: 1743-1755  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/dcm_meeg/spm_ssr_priors.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_ssr_priors", *args, **kwargs)
