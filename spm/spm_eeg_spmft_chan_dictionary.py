from spm._runtime import Runtime


def spm_eeg_spmft_chan_dictionary(*args, **kwargs):
    r"""
      Return a table of corresponce between SPM and FieldTrip channel types  
        FORMAT dictionary = spm_eeg_spmft_chan_dictionary  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_spmft_chan_dictionary.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_spmft_chan_dictionary", *args, **kwargs)
