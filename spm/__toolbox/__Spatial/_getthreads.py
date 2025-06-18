from mpython import Runtime


def _getthreads(*args, **kwargs):
    """
      Size of block of threads on a CUDA kernel
        FORMAT s = getthreads(kernel,d)
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Spatial/private/getthreads.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("getthreads", *args, **kwargs)
