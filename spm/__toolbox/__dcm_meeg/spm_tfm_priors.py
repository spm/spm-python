from spm.__wrapper__ import Runtime


def spm_tfm_priors(*args, **kwargs):
    """
      Prior moments for a canonical microcircuit model (with plasticity)  
        FORMAT [pE,pC] = spm_tfm_priors(A,B,C)  
         
        A{3},B{m},C  - binary constraints on extrinsic connections  
         
        pE - prior expectation - f(x,u,P,M)  
         
        synaptic parameters  
       --------------------------------------------------------------------------  
           pE.T - syaptic time constants  
           pE.S - intrinsic again  
           pE.G - intrinsic connection strengths  
         
        connectivity parameters  
       --------------------------------------------------------------------------  
           pE.A - extrinsic  
           pE.B - trial-dependent (driving)  
           pE.C - stimulus input  
           pE.D - delays  
           pE.N - trial-dependent (modulatory)  
         
        plasticity parameters  
       --------------------------------------------------------------------------  
           pE.E - voltage-dependent potentiation  
           pE.F - decay  
         
        stimulus and noise parameters  
       --------------------------------------------------------------------------  
           pE.R - onset and dispersion  
         
        pC - prior (co)variances  
         
        Because priors are specified under log normal assumptions, most  
        parameters are simply scaling coefficients with a prior expectation  
        and variance of one.  After log transform this renders pE = 0 and  
        pC = 1;  The prior expectations of what they scale are specified in  
        spm_fx_cmc_tfm  
       __________________________________________________________________________  
         
        David O, Friston KJ (2003) A neural mass model for MEG/EEG: coupling and  
        neuronal dynamics. NeuroImage 20: 1743-1755  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_tfm_priors.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_tfm_priors", *args, **kwargs)
