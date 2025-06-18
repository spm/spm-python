from mpython import Runtime


def spm_slice2vol(*args, **kwargs):
    """
      Slice-to-volume alignment job
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Spatial/spm_slice2vol.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_slice2vol", *args, **kwargs)
