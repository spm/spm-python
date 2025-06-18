from mpython import Runtime


def spm_markdown(*args, **kwargs):
    """
      Convert a job configuration tree into a series of markdown documents
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_markdown.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_markdown", *args, **kwargs, nargout=0)
