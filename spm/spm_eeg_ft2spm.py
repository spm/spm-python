from mpython import Runtime


def spm_eeg_ft2spm(*args, **kwargs):
    """
      Converter from FieldTrip data structures to SPM file format
        FORMAT D = spm_eeg_ft2spm(ftdata, filename)
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_ft2spm.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_ft2spm", *args, **kwargs)
