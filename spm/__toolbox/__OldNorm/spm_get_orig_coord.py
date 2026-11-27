from spm._runtime import Runtime


def spm_get_orig_coord(*args, **kwargs):
    r"""
      Determine corresponding co-ordinate in un-normalised image.  
        FORMAT orig_coord = get_orig_coord2(coord, matname,PU)  
        coord      - [x1 y1 z1 ; x2 y2 z2 ; etc] in MNI space (mm).  
        matname    - File containing transformation information (_sn.mat).  
                   - or the structure containing the transformation.  
        PU         - Name of un-normalised image  
        orig_coord - Co-ordinate in un-normalised image (voxel).  
         
        FORMAT orig_coord = get_orig_coord2(coord, matname)  
        coord      - [x1 y1 z1 ; x2 y2 z2 ; etc] in MNI space (mm).  
        matname    - File containing transformation information (_sn.mat).  
                   - or the structure containing the transformation.  
        orig_coord - Original co-ordinate (mm).  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/OldNorm/spm_get_orig_coord.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_get_orig_coord", *args, **kwargs)
