from mpython import Runtime


def mne_omit_first_line(*args, **kwargs):
    """

        [rest] = mne_omit_first_line(str)

        Omit the first line in a multi-line string (useful for handling
        error messages)


    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_omit_first_line.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_omit_first_line", *args, **kwargs)
