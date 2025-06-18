from mpython import Runtime


def spm_lfp_log(*args, **kwargs):
    """
      Feature selection for lfp and mtf (spectral) neural mass models
        FORMAT [y] = spm_lfp_log(y,M)

        Y -> log(y) (including cells)
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Neural_Models/spm_lfp_log.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_lfp_log", *args, **kwargs)
