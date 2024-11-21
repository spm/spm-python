from spm.__wrapper__ import Runtime


def _pos2dim3d(*args, **kwargs):
    """
      POS2DIM3D reconstructs the volumetric dimensions from an ordered list of   
        positions. optionally, the original dim can be provided, and the (2:end)  
        elements are appended to the output.  
         
        Use as  
          [dim] = pos2dim3d(pos, dimold)  
        where pos is an ordered list of positions and where the (optional)  
        dimold is a vector with the original dimensionality of the anatomical  
        or functional data.  
         
        The output dim is a 1x3 or 1xN vector of which the first three elements  
        correspond to the 3D volumetric dimensions.  
         
        See also POS2DIM, POS2TRANSFORM  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/pos2dim3d.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("pos2dim3d", *args, **kwargs)
