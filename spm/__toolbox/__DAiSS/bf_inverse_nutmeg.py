from mpython import Runtime


def bf_inverse_nutmeg(*args, **kwargs):
    """
      Interface to NUTMEG inverse methods
        http://www.nitrc.org/plugins/mwiki/index.php/nutmeg:MainPage
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_inverse_nutmeg.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_inverse_nutmeg", *args, **kwargs)
