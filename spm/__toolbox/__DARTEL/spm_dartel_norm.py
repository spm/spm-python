from mpython import Runtime


def spm_dartel_norm(*args, **kwargs):
    """
      Warp individuals to match template
        FORMAT spm_dartel_norm(job)
        job.flowfields - Flow-fields
        job.images     - Image to warp
        job.interp     - Interpolation method
        job.K          - 2^K timesteps are used
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DARTEL/spm_dartel_norm.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dartel_norm", *args, **kwargs)
