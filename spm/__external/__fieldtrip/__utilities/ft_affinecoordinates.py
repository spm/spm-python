from spm._runtime import Runtime


def ft_affinecoordinates(*args, **kwargs):
    r"""
      FT_AFFINECOORDINATES returns the affine coordinate transformation matrix that  
        converts FROM a specific head coordinate TO a specific head coordinate system.  
         
        Use as  
          [transform] = ft_affinecoordinates(from, to)  
         
        Note that translations are expressed in millimeters, therefore the geometrical data  
        to which this coordinate transformation is applied must also be specified in  
        millimeters.  
         
        See also FT_CONVERT_COORDSYS, FT_CONVERT_UNITS, FT_HEADCOORDINATES, FT_WARP_APPLY  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/ft_affinecoordinates.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_affinecoordinates", *args, **kwargs)
