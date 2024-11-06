from spm.__wrapper__ import Runtime


def spm_L_priors(*args, **kwargs):
    """
      Prior moments for the lead-field parameters of ERP models  
        FORMAT [pE,pC] = spm_L_priors(dipfit)  
         
        dipfit    - forward model structure:  
         
           dipfit.type     - 'ECD', 'LFP' or 'IMG'  
           dipfit.symmetry - distance (mm) for symmetry constraints (ECD)  
           dipfit.location - allow changes in source location       (ECD)  
           dipfit.Lpos     - x,y,z source positions (mm)            (ECD)  
           dipfit.Nm       - number of modes                        (IMG)  
           dipfit.Ns       - number of sources  
           dipfit.Nc       - number of channels  
         
        pE - prior expectation  
        pC - prior covariance  
         
        adds spatial parameters  
       --------------------------------------------------------------------------  
           pE.Lpos - position                    - ECD  
           pE.L    - orientation                 - ECD  
                     coefficients of local modes - Imaging  
                     gain of electrodes          - LFP  
           pE.J    - contributing states (length(J) = number of states per source  
         
       __________________________________________________________________________  
         
        David O, Friston KJ (2003) A neural mass model for MEG/EEG: coupling and  
        neuronal dynamics. NeuroImage 20: 1743-1755  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_L_priors.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_L_priors", *args, **kwargs)
