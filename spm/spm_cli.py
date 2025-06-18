from mpython import Runtime


def spm_cli(*args, **kwargs):
    """
      Command line interface for SPM
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_cli.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cli", *args, **kwargs, nargout=0)
