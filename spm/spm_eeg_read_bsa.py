from spm._runtime import Runtime


def spm_eeg_read_bsa(*args, **kwargs):
    r"""
      This function reads a definition of spatial confounds from a BESA  
        *.bsa file and returns an sconfounds struct with the following fields  
        .label - labels of channels  
        .coeff - matrix of coefficients (channels x components)  
        .bad - logical vector - channels marked as bad.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_read_bsa.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_read_bsa", *args, **kwargs)
