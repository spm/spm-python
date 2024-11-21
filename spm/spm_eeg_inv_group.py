from spm.__wrapper__ import Runtime


def spm_eeg_inv_group(*args, **kwargs):
    """
      Source reconstruction for a group ERP or ERF study  
        FORMAT spm_eeg_inv_group(S)  
         
        S  - string array of names of M/EEG mat files for inversion (optional)  
       __________________________________________________________________________  
         
        spm_eeg_inv_group inverts forward models for a group of subjects or ERPs  
        under the simple assumption that the [empirical prior] variance on each  
        source can be factorised into source-specific and subject-specific terms.  
        These covariance components are estimated using ReML (a form of Gaussian  
        process modelling) to give empirical priors on sources.  Source-specific  
        covariance parameters are estimated first using the sample covariance  
        matrix in sensor space over subjects and trials using multiple sparse  
        priors (and,  by default, a greedy search).  The subject-specific terms  
        are then estimated by pooling over trials for each subject separately.  
        All trials in D.events.types will be inverted in the order specified.  
        The result is a contrast (saved in D.mat) and a 3-D volume of MAP or  
        conditional estimates of source activity that are constrained to the  
        same subset of voxels.  These would normally be passed to a second-level  
        SPM for classical inference about between-trial effects, over subjects.  
       __________________________________________________________________________  
         
        References:  
        Electromagnetic source reconstruction for group studies. V. Litvak and  
        K.J. Friston. NeuroImage, 42:1490-1498, 2008.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_inv_group.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_inv_group", *args, **kwargs, nargout=0)
