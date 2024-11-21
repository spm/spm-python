from spm.__wrapper__ import Runtime


def ft_affinecoordinates(*args, **kwargs):
    """
      FT_AFFINECOORDINATES returns the affine coordinate transformation matrix that  
        converts FROM a specific head coordinate TO a specific head coordinate system.  
         
        Use as  
          [transform] = ft_affinecoordinates(from, to)  
         
        Note that translations are expressed in millimeters, therefore the geometrical data  
        to which this coordinate transformation is applied must also be specified in  
        millimeters.  
         
        See also FT_CONVERT_COORDSYS, FT_CONVERT_UNITS, FT_HEADCOORDINATES, FT_WARP_APPLY  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/ft_affinecoordinates.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_affinecoordinates", *args, **kwargs)
