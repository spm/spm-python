from mpython import Runtime


def spm_swarp(*args, **kwargs):
    """
      Warp surface
        FORMAT that = spm_swarp(this,def)
        this - a gifti object
        def  - a deformation (nifti object or filename)
        that - the warped gifti object

        FORMAT that = spm_swarp(this,def,M)
        this - a gifti object
        def  - a deformation field (nx*ny*nz*1*3)
        M    - mapping from voxels to world, for deformation field
        that - the warped gifti object
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_swarp.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_swarp", *args, **kwargs)
