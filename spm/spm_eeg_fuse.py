from spm.__wrapper__ import Runtime


def spm_eeg_fuse(*args, **kwargs):
    """
      Fuse MEG and EEG datasets to create a multimodal dataset  
        FORMAT D = spm_eeg_fuse(S)  
         
        S           - input structure (optional)  
         fields of S:  
          S.D       - character array containing filenames of M/EEG mat-files  
          S.prefix     - prefix for the output file (default - 'u')  
         
        D        - MEEG object (also written to disk, with a 'u' prefix)  
       __________________________________________________________________________  
         
        Vladimir Litvak  
        Copyright (C) 2008-2022 Wellcome Centre for Human Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_fuse.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_fuse", *args, **kwargs)
