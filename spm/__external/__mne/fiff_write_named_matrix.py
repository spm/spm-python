from mpython import Runtime


def fiff_write_named_matrix(*args, **kwargs):
    """

        fiff_write_named_matrix(fid,kind,mat)

        Writes a named single-precision floating-point matrix

            fid           An open fif file descriptor
            kind          The tag kind to use for the data
            mat           The data matrix


    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_write_named_matrix.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_write_named_matrix", *args, **kwargs, nargout=0)
