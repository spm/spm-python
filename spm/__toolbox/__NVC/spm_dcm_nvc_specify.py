from spm.__wrapper__ import Runtime


def spm_dcm_nvc_specify(*args, **kwargs):
    """
      Specify unestimated structure for (multimodal) DCM for fMRI and M/EEG  
        FORMAT DCM = spm_dcm_nvc_specify(SPM,xY_fMRI, MEEG, Model,N_exclude,fmri_cond,options)  
         
        See spm_dcm_nvc.m for detailed descriptions of the parameters  
         
        Inputs:  
        -------------------------------------------------------------------------  
        SPM          -  SPM structure or location of SPM.mat  
        xY_fMRI      -  Cell array of VOI filenames (the same order as sources in EEG DCM)  
        MEEG         -  Location of DCM for M/EEG .mat file or DCM structure  
        model        -  Model space definition (see spm_dcm_nvc.m)  
        n_exclude    -  Which neuronal populations should drive haemodynamics (optional)  
        fmri_cond    -  Which fMRI conditions to include (optional)  
        options      -  DCM options  
         
        Evaluates:  
        -------------------------------------------------------------------------  
         
        DCM          -  unestimated DCM  
       __________________________________________________________________________  
        Jafarian, A., Litvak, V., Cagnan, H., Friston, K.J. and Zeidman, P., 2019.  
        Neurovascular coupling: insights from multi-modal dynamic causal modelling  
        of fMRI and MEG. arXiv preprint arXiv:1903.07478.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/NVC/spm_dcm_nvc_specify.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_nvc_specify", *args, **kwargs)
