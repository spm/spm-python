from spm._runtime import Runtime


def spm_erp_priors(*args, **kwargs):
    """
      Prior moments for a neural-mass model of ERPs  
        FORMAT [pE,pC] = spm_erp_priors(A,B,C)  
         
        A{3},B{m},C  - binary constraints on extrinsic connections  
         
        pE - prior expectation - f(x,u,P,M)  
         
        synaptic parameters  
       --------------------------------------------------------------------------  
           pE.T - synaptic time constants  
           pE.G - synaptic densities (intrinsic gain)  
           pE.S - activation function parameters  
           pE.G - intrinsic connection strengths  
         
        connectivity parameters  
       --------------------------------------------------------------------------  
           pE.A - extrinsic  
           pE.B - trial-dependent  
           pE.C - stimulus input  
           pE.D - delays  
         
        stimulus and noise parameters  
       --------------------------------------------------------------------------  
           pE.R - onset and dispersion  
         
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_erp_priors.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_erp_priors", *args, **kwargs)
