from mpython import Runtime


def mne_write_events(*args, **kwargs):
    """

        mne_write_events(filename,eventlist)

        Write an event list into a fif file


    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_write_events.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_write_events", *args, **kwargs, nargout=0)
