from spm.__wrapper__ import Runtime


def spm_nmda_priors(*args, **kwargs):
    """
      prior moments for a neural-mass model of ERPs  
        FORMAT [pE,pC] = spm_nmm_priors(A,B,C)  
         
        A{3},B{m},C  - binary constraints on extrinsic connections  
         
        pE - prior expectation - f(x,u,P,M)  
         
        population variance  
       --------------------------------------------------------------------------  
            E.S    - variance  
         
        synaptic parameters  
       --------------------------------------------------------------------------  
           pE.T    - synaptic time constants  
           pE.G    - intrinsic connectivity  
         
        connectivity parameters  
       --------------------------------------------------------------------------  
           pE.A    - extrinsic  
           pE.B    - trial-dependent  
           pE.C    - stimulus input  
         
           pE.SA - switches on extrinsic (excitatory)  
           pE.GE - switches on intrinsic (excitatory)  
           pE.GI - switches on intrinsic (inhibitory)  
         
        stimulus and noise parameters  
       --------------------------------------------------------------------------  
           pE.R    - onset and dispersion  
           pE.D    - delays  
           pE.U    - exogenous background activity  
         
        pC - prior (co)variances  
         
        Because priors are specified under log normal assumptions, most  
        parameters are simply scaling coefficients with a prior expectation  
        and variance of one.  After log transform this renders pE = 0 and  
        pC = 1;  The prior expectations of what they scale are specified in  
        spm_erp_fx  
       __________________________________________________________________________  
         
        David O, Friston KJ (2003) A neural mass model for MEG/EEG: coupling and  
        neuronal dynamics. NeuroImage 20: 1743-1755  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Neural_Models/spm_nmda_priors.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_nmda_priors", *args, **kwargs)
