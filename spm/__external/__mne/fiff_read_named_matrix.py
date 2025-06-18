from mpython import Runtime


def fiff_read_named_matrix(*args, **kwargs):
    """

        [mat] = fiff_read_named_matrix(fid,node)

        Read named matrix from the given node


    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_read_named_matrix.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_read_named_matrix", *args, **kwargs)
