from spm._runtime import Runtime


def _read_asa_elc(*args, **kwargs):
    r"""
      READ_ASA_ELC reads electrodes from an ASA electrode file  
        converting the units to mm  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_asa_elc.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_asa_elc", *args, **kwargs)
