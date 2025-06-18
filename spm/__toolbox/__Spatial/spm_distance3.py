from mpython import Runtime


def spm_distance3(*args, **kwargs):
    """
      Compute Euclidean distances from a tissue map
        FORMAT d = spm_distance3(p,vx,maxit,d)
        p     - Tissue probability map
        vx    - Voxel sizes ([1 1 1])
        maxit - Maximum number of iterations (20)
        d     - Distances.
                - Initial estimates on input (zeros(size(p)))
                - Output estimate on output

        This implementation is very slow. Vectorising it would be memory
        hungry, so (if it turns out to be useful) it should be written in C.

       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Spatial/spm_distance3.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_distance3", *args, **kwargs)
