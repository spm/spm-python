from mpython import Runtime


def spm_dcm_reduce(*args, **kwargs):
    """
      Reduce the posterior of DCM given new priors (rE,rC)
        FORMAT RCM = spm_dcm_reduce(DCM,rE,rC)
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_reduce.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dcm_reduce", *args, **kwargs)
