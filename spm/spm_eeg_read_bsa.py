from spm.__wrapper__ import Runtime


def spm_eeg_read_bsa(*args, **kwargs):
    """
      This function reads a definition of spatial confounds from a BESA  
        *.bsa file and returns an sconfounds struct with the following fields  
        .label - labels of channels  
        .coeff - matrix of coefficients (channels x components)  
        .bad - logical vector - channels marked as bad.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_read_bsa.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_read_bsa", *args, **kwargs)
