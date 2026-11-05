from spm._runtime import Runtime


def _read_asa_msr(*args, **kwargs):
    r"""
      READ_ASA_MSR reads EEG or MEG data from an ASA data file  
        converting the units to uV or fT  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_asa_msr.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_asa_msr", *args, **kwargs)
