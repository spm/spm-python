from mpython import Runtime


def mne_rt_define_commands(*args, **kwargs):
    """

           [ FIFF ] = mne_rt_define_commands()

           Defines structure containing the MNE_RT constants


    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_rt_define_commands.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_rt_define_commands", *args, **kwargs)
