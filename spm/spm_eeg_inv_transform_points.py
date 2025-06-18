from mpython import Runtime


def spm_eeg_inv_transform_points(*args, **kwargs):
    """
      Apply homogeneous transformation to a set of 3D points
        FORMAT new = spm_eeg_inv_transform_points(M, old)
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_inv_transform_points.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_inv_transform_points", *args, **kwargs)
