from spm.__wrapper__ import Runtime


def _pos2dim(*args, **kwargs):
    """
      POS2DIM reconstructs the volumetric dimensions from an ordered list of  
        positions.  
         
        Use as  
          [dim] = pos2dim(pos)  
        where pos is an ordered list of positions.  
         
        The output dim is a 3-element vector which correspond to the 3D  
        volumetric dimensions  
         
        See also POS2TRANSFORM  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/pos2dim.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("pos2dim", *args, **kwargs)
