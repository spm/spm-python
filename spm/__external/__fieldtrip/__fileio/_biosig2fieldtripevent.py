from spm._runtime import Runtime


def _biosig2fieldtripevent(*args, **kwargs):
    r"""
      BIOSIG2FIELDTRIPEVENT converts event information from a biosig hdr into  
        fieldtrip events  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/biosig2fieldtripevent.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("biosig2fieldtripevent", *args, **kwargs)
