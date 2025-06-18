from mpython import Runtime


def spm_series_align(*args, **kwargs):
    """
      Longitudinal registration of image series
        FORMAT out = spm_series_align(job)
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Longitudinal/spm_series_align.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_series_align", *args, **kwargs)
