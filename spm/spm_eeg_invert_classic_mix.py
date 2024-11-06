from spm.__wrapper__ import Runtime


def spm_eeg_invert_classic_mix(*args, **kwargs):
    """
      FORMAT [D] = spm_eeg_invert_classic_mix(D,val,Qpriors,surfind,ugainfiles)  
         
        ReML inversion of multiple posterior current variances from previous  
        iterations spm_eeg_invert_classic or spm_eeg_invert  
        ReML estimation of regularisation hyperparameters using the  
        spatiotemporal hierarchy implicit in EEG/MEG data  
         
        D contains the data and inversion parameters (see  
        spm_eeg_invert.m/spm_eeg_invert_classic.m)  
        val the inversion index   
        Qpriors is N solutions of rows by Nd variance estimates  
        surfind is N solutions long and contains indices into ugainfiles to these priors with different lead field structures  
        ugainfiles are the SPMgain matrices for the different surfaces  
         
        Output D will have a solution which is optimal REML mixture of Qpriors  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_invert_classic_mix.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_invert_classic_mix", *args, **kwargs)
