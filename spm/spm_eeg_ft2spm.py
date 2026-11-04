from spm._runtime import Runtime


def spm_eeg_ft2spm(*args, **kwargs):
    r"""
      Converter from FieldTrip data structures to SPM file format  
        FORMAT D = spm_eeg_ft2spm(ftdata, filename)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_ft2spm.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_ft2spm", *args, **kwargs)
