from mpython import Runtime


def fiff_write_dig_point(*args, **kwargs):
    """

        fiff_write_dig_point(fid,dig)

        Writes a digitizer data point into a fif file

            fid           An open fif file descriptor
            dig           The point to write


    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_write_dig_point.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_write_dig_point", *args, **kwargs, nargout=0)
