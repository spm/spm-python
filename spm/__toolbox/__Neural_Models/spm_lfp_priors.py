from spm.__wrapper__ import Runtime


def spm_lfp_priors(*args, **kwargs):
    """
      prior moments for a neural mass model of ERPs  
        FORMAT [pE,pC] = spm_lfp_priors(A,B,C)  
         
        A{3},B{m},C    - binary constraints on extrinsic connectivity  
         
        pE - prior expectation  
         
        synaptic parameters  
       --------------------------------------------------------------------------  
           pE.T - synaptic time constants  
           pE.G - synaptic densities (intrinsic gain)  
           pE.R - activation function parameters  
         
        connectivity parameters  
       --------------------------------------------------------------------------  
           pE.A - extrinsic - coupling  
           pE.B - extrinsic - trial-dependent  
           pE.C - extrinsic - stimulus input  
           pE.H - intrinsic rates  
           pE.D - extrinsic delays  
           pE.I - intrinsic delays  
         
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Neural_Models/spm_lfp_priors.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_lfp_priors", *args, **kwargs)
