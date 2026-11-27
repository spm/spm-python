from spm._runtime import Runtime


def _pos2transform(*args, **kwargs):
    r"""
      POS2TRANSFORM reconstructs a transformation matrix from an ordered list   
        of positions.  
         
        Use as  
          [transform] = pos2transform(pos, dim)  
        where pos is an ordered list of positions that should specify a full 3D volume.  
         
        The output transform is a 4x4 homogenous transformation matrix which transforms  
        from 'voxelspace' into the positions provided in the input  
         
        See also POS2DIM  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/pos2transform.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("pos2transform", *args, **kwargs)
