from mpython import Runtime


def spm_eeg_spmft_chan_dictionary(*args, **kwargs):
    """
      Return a table of corresponce between SPM and FieldTrip channel types
        FORMAT dictionary = spm_eeg_spmft_chan_dictionary
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_spmft_chan_dictionary.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_spmft_chan_dictionary", *args, **kwargs)
