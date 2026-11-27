from spm._runtime import Runtime


def _make_or_fetch_inputfile(*args, **kwargs):
    r"""
      MAKE_OR_FETCH_INPUTFILE is a helper function for ft_preamble_loadvar and ft_postamble_savevar, and  
        is used for the cfg.reproducescript functionality.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/private/make_or_fetch_inputfile.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("make_or_fetch_inputfile", *args, **kwargs)
