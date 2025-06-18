from mpython import Runtime


def spm_get_volumes(*args, **kwargs):
    """
      Compute total volumes from tissue segmentations
        FORMAT gl = spm_get_volumes(P)
        P  - a matrix of image filenames
        gl - a vector of volumes (in litres)
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_get_volumes.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_get_volumes", *args, **kwargs)
