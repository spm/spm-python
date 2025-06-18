from mpython import Runtime


def spm_DAiSS(*args, **kwargs):
    """
     __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/spm_DAiSS.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_DAiSS", *args, **kwargs, nargout=0)
