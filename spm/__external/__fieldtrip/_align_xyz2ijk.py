from spm.__wrapper__ import Runtime


def _align_xyz2ijk(*args, **kwargs):
    """
      ALIGN_XYZ2IJK updates the transform and coordsys fields such that the axes of the  
        resulting head coordinate system are aligned with the voxel indices. The intention  
        is to create a volume structure that can be plotted in native voxel coordinates.  
         
        See also ALIGN_IJK2XYZ, VOLUMEPERMUTE, VOLUMEFLIP  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/align_xyz2ijk.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("align_xyz2ijk", *args, **kwargs)
