from mpython import Runtime


def fiff_read_evoked_all(*args, **kwargs):
    """

        [data] = fiff_read_evoked_all(fname)

        Read all evoked data set (averages only)


    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_read_evoked_all.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_read_evoked_all", *args, **kwargs)
