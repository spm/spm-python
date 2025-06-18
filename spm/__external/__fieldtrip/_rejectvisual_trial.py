from mpython import Runtime


def _rejectvisual_trial(*args, **kwargs):
    """
      SUBFUNCTION for ft_rejectvisual


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/rejectvisual_trial.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("rejectvisual_trial", *args, **kwargs)
