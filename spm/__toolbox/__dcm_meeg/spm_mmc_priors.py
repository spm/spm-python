from spm.__wrapper__ import Runtime


def spm_mmc_priors(*args, **kwargs):
    """
      Prior moments for a canonical motor cortex microcircuit model  
        FORMAT [E,V] = spm_mmc_priors(A,B,C)  
         
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
        spm_fx_mmc  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_mmc_priors.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mmc_priors", *args, **kwargs)
