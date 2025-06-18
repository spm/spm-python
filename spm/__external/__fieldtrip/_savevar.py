from mpython import Runtime


def _savevar(*args, **kwargs):
    """
      SAVEVAR is a helper function for cfg.outputfile

        See also LOADVAR


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/savevar.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("savevar", *args, **kwargs, nargout=0)
