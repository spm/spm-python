from spm.__wrapper__ import Runtime


def spm_dcm_nvc_priors(*args, **kwargs):
    """
      Priors for a multimodal DCM for fMRI and M/EEG  
        FORMAT [pE,pC,x] = spm_dcm_nvc_priors(DCM)  
         
        Input:  
        -------------------------------------------------------------------------  
        DCM      - multimodal DCM (see spm_dcm_nvc_specify.m)  
         
        Evaluates:  
        -------------------------------------------------------------------------  
        pE.H     - prior expectations (hemodynamic)  
        pC.H     - prior covariances  (hemodynamic)  
        pE.J     - prior expectations (neurovascular coupling)  
        pC.J     - prior covariances  (neurovascular coupling)  
        x        - prior (initial) states  
       __________________________________________________________________________  
        Jafarian, A., Litvak, V., Cagnan, H., Friston, K.J. and Zeidman, P., 2019.  
        Neurovascular coupling: insights from multi-modal dynamic causal modelling  
        of fMRI and MEG. arXiv preprint arXiv:1903.07478.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/NVC/spm_dcm_nvc_priors.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_nvc_priors", *args, **kwargs)
