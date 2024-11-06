from spm.__wrapper__ import Runtime


def spm_ind_priors(*args, **kwargs):
    """
      Prior moments for a neural-mass model of induced responses  
        FORMAT [pE,gE,pC,gC] = spm_ind_priors(A,B,C,dipfit,Nu,Nf)  
        A{2},B{m},C  - binary constraints on extrinsic connections  
        Nm           - number of frequency modes used  
        Nf           - number of frequency modes explained  
         
        pE - prior expectation - f(x,u,P,M)  
        gE - prior expectation - g(x,u,G,M)  
         
        connectivity parameters  
       --------------------------------------------------------------------------  
           pE.A    - trial-invariant  
           pE.B{m} - trial-dependent  
           pE.C    - stimulus-stimulus dependent  
         
        stimulus and noise parameters  
       --------------------------------------------------------------------------  
           pE.R    - onset and dispersion  
         
        pC - prior covariances: cov(spm_vec(pE))  
       __________________________________________________________________________  
         
        David O, Friston KJ (2003) A neural mass model for MEG/EEG: coupling and  
        neuronal dynamics. NeuroImage 20: 1743-1755  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_ind_priors.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_ind_priors", *args, **kwargs)
