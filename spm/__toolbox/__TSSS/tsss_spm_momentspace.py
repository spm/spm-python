from spm.__wrapper__ import Runtime


def tsss_spm_momentspace(*args, **kwargs):
    """
      Switch a dataset to SSS space using virtual montage  
        FORMAT D = spm_eeg_crop(S)  
         
        S        - input struct  
         fields of S:  
          D          - MEEG object or filename of M/EEG mat-file with data after  
                       TSSS tool  
          condthresh - threshold on condition number for regularisation  
         
        Output:  
        D        - MEEG object (also written on disk)  
         
        Reference: Vrba J, Taulu S, Nenonen J, Ahonen A. Signal space separation  
        beamformer. Brain Topogr. 2010 Jun;23(2):128-33.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/TSSS/tsss_spm_momentspace.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("tsss_spm_momentspace", *args, **kwargs)
