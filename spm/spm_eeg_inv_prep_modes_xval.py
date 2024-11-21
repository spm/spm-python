from spm.__wrapper__ import Runtime


def spm_eeg_inv_prep_modes_xval(*args, **kwargs):
    """
      Prepare a spatial mode file for inversion  
        FORMAT [spatialmodename,Nmodes,newpctest,testchans]=spm_eeg_inv_prep_modes_xval(filenames, Nmodes, spatialmodename,Nblocks,pctest)  
         
        this file ensures the same spatial modes are used across different files (which would contain the same data but different head-models for example)  
        it also makes sure that the same channels groups are preserved to allow comparable cross validation and free energy metrics  
        input a list of the M/EEG dataset names: filenames  
        Nmodes - number of required spatial modes (if empty uses all available  
        channels)  
        channels)  
        spatialmodename- name of output file  
        Nblocks- number of cross validation runs (optional and  
        default 1)  
        pctest- percentatge of channels to be used for testdata (optional and  
        default 0)  
        if pctest*Nblocks=100 then will use independent MEG channels and may adjust pctest (in output) to   
        accommodate this. ( k-fold cross val)  
        if pctest*Nblocks~=100 then uses random selection of pctest channels for each block (Monte-Carlo cross val)  
         
        in output file  
        megind- good meg channel indices  
        testchans - indices to megind of channels to be turned off during training phase (and tested later)  
        U{} - a different spatial modes matrix for each set of training channels or megind without indexed testchans or megind(setdiff(1:length(megind),testchans(b,:)))  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_inv_prep_modes_xval.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_inv_prep_modes_xval", *args, **kwargs)
