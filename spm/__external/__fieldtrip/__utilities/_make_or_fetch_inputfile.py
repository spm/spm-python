from spm.__wrapper__ import Runtime


def _make_or_fetch_inputfile(*args, **kwargs):
    """
      MAKE_OR_FETCH_INPUTFILE is a helper function for ft_preamble_loadvar and ft_postamble_savevar, and  
        is used for the cfg.reproducescript functionality.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/make_or_fetch_inputfile.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("make_or_fetch_inputfile", *args, **kwargs)
