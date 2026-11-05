from spm._runtime import Runtime


def _read_bham(*args, **kwargs):
    r"""
      READ_BHAM reads the EEG data files as recorded by Praamstra in Birmingham  
        the datafiles are in a particular ascii format  
         
        [dat, lab] = read_bham(filename)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_bham.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_bham", *args, **kwargs)
