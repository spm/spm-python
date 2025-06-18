from mpython import Runtime


def _isricohmegfile(*args, **kwargs):
    """
      The extentions, .con, .ave, and .mrk are common between Ricoh and Yokogawa systems.
        isricohmegfile idetifies whether the file is generated from Ricoh system or not.
        This function uses a function in YOKOGAWA_MEG_READER toolbox, getYkgwHdrSystem.


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/isricohmegfile.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("isricohmegfile", *args, **kwargs)
