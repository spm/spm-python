from mpython import Runtime


def spm_extract_files(*args, **kwargs):
    """
      FORMAT spm_extract_files(P,cwd)
        forints files (and their subroutines) and expect them to the current
        directory
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_extract_files.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_extract_files", *args, **kwargs, nargout=0)
