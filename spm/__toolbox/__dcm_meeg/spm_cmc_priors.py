from spm.__wrapper__ import Runtime


def spm_cmc_priors(*args, **kwargs):
    """
      Prior moments for a canonical microcircuit model  
        FORMAT [pE,pC] = spm_cmc_priors(A,B,C)  
         
        A{3},B{m},C  - binary constraints on extrinsic connections  
         
        pE - prior expectation - f(x,u,P,M)  
         
        synaptic parameters  
       --------------------------------------------------------------------------  
           pE.T - syaptic time constants  
           pE.S - activation function parameters  
           pE.G - intrinsic connection strengths  
         
        connectivity parameters  
       --------------------------------------------------------------------------  
           pE.A - extrinsic  
           pE.B - trial-dependent (driving)  
           pE.N - trial-dependent (modulatory)  
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
        spm_fx_cmc  
       __________________________________________________________________________  
         
        David O, Friston KJ (2003) A neural mass model for MEG/EEG: coupling and  
        neuronal dynamics. NeuroImage 20: 1743-1755  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_cmc_priors.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_cmc_priors", *args, **kwargs)
