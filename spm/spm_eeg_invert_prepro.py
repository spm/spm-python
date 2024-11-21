from spm.__wrapper__ import Runtime


def spm_eeg_invert_prepro(*args, **kwargs):
    """
       
        Preprocessing for inversion stage.   
        includes spatial and temporal dimension reduction  
         
        this version only handles single subject single modality data  
        the removal of many scaling factors makes it easier to compare between forward models  
        ReML inversion of multiple forward models for EEG-MEG  
        FORMAT [D] = spm_eeg_invert_classic(D)  
        ReML estimation of regularisation hyperparameters using the  
        spatiotemporal hierarchy implicit in EEG/MEG data  
         
        Requires:  
        D{i}.inv{val}.inverse:  
         
            inverse.modality - modality to use in case of multimodal datasets  
         
            inverse.trials - D.events.types to invert  
            inverse.type   - 'GS' Greedy search on MSPs  
                             'ARD' ARD search on MSPs  
                             'MSP' GS and ARD multiple sparse priors  
                             'LOR' LORETA-like model  
                             'IID' minimum norm  
                             'EBB' for empirical bayes beamformer  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_invert_prepro.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_invert_prepro", *args, **kwargs)
