from spm.__wrapper__ import Runtime


def spm_dcm_nvc_nd(*args, **kwargs):
    """
      Generate neuronal drive signals for multimodal DCM for fMRI and M/EEG  
        FORMAT neuronal_drive = spm_dcm_nvc_nd(DCM)  
         
        Inputs:  
        -------------------------------------------------------------------------  
        DCM              -  (unestimated multimodal) DCM for fMRI and MEG.  
                            see spm_dcm_nvc_specify.m  
         
        Evaluates:  
        -------------------------------------------------------------------------  
        neuronal_drive   -  neural_drive signals.  
       __________________________________________________________________________  
        Jafarian, A., Litvak, V., Cagnan, H., Friston, K.J. and Zeidman, P., 2019.  
        Neurovascular coupling: insights from multi-modal dynamic causal modelling  
        of fMRI and MEG. arXiv preprint arXiv:1903.07478.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/NVC/spm_dcm_nvc_nd.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_nvc_nd", *args, **kwargs)
