from mpython import Runtime


def fiff_write_id(*args, **kwargs):
    """

        fiff_write_id(fid,kind,id)

        Writes fiff id

            fid           An open fif file descriptor
            kind          The tag kind
            id            The id to write

        If the id argument is missing it will be generated here


    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_write_id.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_write_id", *args, **kwargs, nargout=0)
