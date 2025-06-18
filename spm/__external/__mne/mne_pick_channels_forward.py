from mpython import Runtime


def mne_pick_channels_forward(*args, **kwargs):
    """

        [fwd] = mne_pick_channels_forward(orig,include,exclude)

        Pick desired channels from a forward solution

        orig      - The original forward solution
        include   - Channels to include (if empty, include all available)
        exclude   - Channels to exclude (if empty, do not exclude any)


    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_pick_channels_forward.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_pick_channels_forward", *args, **kwargs)
