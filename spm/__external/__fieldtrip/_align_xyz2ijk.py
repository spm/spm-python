from spm._runtime import Runtime


def _align_xyz2ijk(*args, **kwargs):
    r"""
      ALIGN_XYZ2IJK updates the transform and coordsys fields such that the axes of the  
        resulting head coordinate system are aligned with the voxel indices. The intention  
        is to create a volume structure that can be plotted in native voxel coordinates.  
         
        See also ALIGN_IJK2XYZ, VOLUMEPERMUTE, VOLUMEFLIP  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/align_xyz2ijk.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("align_xyz2ijk", *args, **kwargs)
