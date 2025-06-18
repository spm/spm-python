from mpython import Runtime


def spm_gen_phase(*args, **kwargs):
    """
      Generate state activities for trial-specific phase-coupled activity
        FORMAT [x] = spm_gen_phase(P,M,U)

        P - parameters
        M - model structure
        U - trial-specific effects

        x - states
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_gen_phase.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_gen_phase", *args, **kwargs)
