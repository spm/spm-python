from spm._runtime import Runtime


def _pos2dim(*args, **kwargs):
    r"""
      POS2DIM reconstructs the volumetric dimensions from an ordered list of  
        positions.  
         
        Use as  
          [dim] = pos2dim(pos)  
        where pos is an ordered list of positions.  
         
        The output dim is a 3-element vector which correspond to the 3D  
        volumetric dimensions  
         
        See also POS2TRANSFORM  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/pos2dim.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("pos2dim", *args, **kwargs)
