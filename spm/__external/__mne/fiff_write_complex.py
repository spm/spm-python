from mpython import Runtime


def fiff_write_complex(*args, **kwargs):
    """

        fiff_write_complex(fid,kind,data)

        Writes a single-precision complex tag to a fif file

            fid           An open fif file descriptor
            kind          Tag kind
            data          The data


    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_write_complex.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fiff_write_complex", *args, **kwargs, nargout=0)
