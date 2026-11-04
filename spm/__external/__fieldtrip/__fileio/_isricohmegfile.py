from spm._runtime import Runtime


def _isricohmegfile(*args, **kwargs):
    r"""
      The extentions, .con, .ave, and .mrk are common between Ricoh and Yokogawa systems.  
        isricohmegfile idetifies whether the file is generated from Ricoh system or not.  
        This function uses a function in YOKOGAWA_MEG_READER toolbox, getYkgwHdrSystem.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/isricohmegfile.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("isricohmegfile", *args, **kwargs)
