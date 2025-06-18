from mpython import Runtime


def spm_authors(*args, **kwargs):
    """
      Return list of SPM coauthors
        FORMAT [current, previous] = spm_authors
        current  - cell array of SPM coauthors of the current release
        previous - cell array of SPM coauthors of previous releases
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_authors.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_authors", *args, **kwargs)
