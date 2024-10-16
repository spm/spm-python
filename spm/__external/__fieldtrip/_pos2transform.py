from spm.__wrapper__ import Runtime


def _pos2transform(*args, **kwargs):
  """  POS2TRANSFORM reconstructs a transformation matrix from an ordered list   
    of positions.  
     
    Use as  
      [transform] = pos2transform(pos, dim)  
    where pos is an ordered list of positions that should specify a full 3D volume.  
     
    The output transform is a 4x4 homogenous transformation matrix which transforms  
    from 'voxelspace' into the positions provided in the input  
     
    See also POS2DIM  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/pos2transform.m)
  """

  return Runtime.call("pos2transform", *args, **kwargs)
