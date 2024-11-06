from spm.__wrapper__ import Runtime


def spm_phase_priors(*args, **kwargs):
    """
      Prior moments of DCM for phase coupling  
        FORMAT [pE,gE,pC,gC] = spm_phase_priors(DCM,fb,dipfit,freq_prior)  
         
        freq_prior   Priors on frequency: 'hard_freq' (default),'soft_freq'  
          
        Fields of DCM:  
         
        As,Bs{m},Ac,Bc{m} - binary constraints (first two mandatory)  
        dipfit       - prior forward model structure  
         
        pE - prior expectation - f(x,u,P,M)  
        gE - prior expectation - g(x,u,G,M)  
         
        connectivity parameters  
       --------------------------------------------------------------------------  
           pE.As    - trial-invariant  
           pE.Bs{m} - trial-dependent  
           pE.Ac    - trial-invariant  
           pE.Bc{m} - trial-dependent  
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_phase_priors.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_phase_priors", *args, **kwargs)
