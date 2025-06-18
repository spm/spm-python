from mpython import Runtime


def spm_thin(*args, **kwargs):
    """
      Erosion to find medial planes
        FORMAT B = spm_thin(B,M)
        B - 3D binary array to thin (on input)
        M - Optional additional input constraining some voxels to be 1
        B - Thinned array (on output)

        This code is not beautiful, but it seems to work a bit. If it is deemed
        to be sufficiently useful, then it could be speeded up by recoding parts
        of it in C.
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Spatial/spm_thin.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_thin", *args, **kwargs)
