from mpython import Runtime


def fiff_finish_writing_raw(*args, **kwargs):
    """

        function fiff_finish_writing_raw(fid)

        fid        of an open raw data file


    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_finish_writing_raw.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_finish_writing_raw", *args, **kwargs, nargout=0)
