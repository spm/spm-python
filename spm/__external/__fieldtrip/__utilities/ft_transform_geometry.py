from spm.__wrapper__ import Runtime


def ft_transform_geometry(*args, **kwargs):
    """
      FT_TRANSFORM_GEOMETRY applies a homogeneous coordinate transformation to a  
        structure with geometric information, for example a volume conduction model for the  
        head, gradiometer of electrode structure containing EEG or MEG sensor positions and  
        MEG coil orientations, a head shape or a source model.  
         
        Use as  
          [output] = ft_transform_geometry(transform, input)  
        where the transform should be a 4x4 homogeneous transformation matrix and the input  
        data structure can be any of the FieldTrip data structures that describes  
        geometrical data, or  
          [output] = ft_transform_geometry(transform, input, method)  
        where the transform contains a set of parameters that can be converted into a 4x4   
        homogeneous transformation matrix, using one of the supported methods:  
        'rotate', 'scale', 'translate', 'rigidbody'. All methods require a 3-element vector  
        as parameters, apart from rigidbody, which requires 6 parameters.   
         
        The units of the transformation matrix must be the same as the units in which the  
        geometric object is expressed.  
         
        The type of geometric object constrains the type of allowed transformations.  
         
        For sensor arrays:  
        If the input is an MEG gradiometer array, only a rigid-body translation plus  
        rotation are allowed. If the input is an EEG electrode or fNIRS optodes array,  
        global rescaling and individual axis rescaling is also allowed.  
         
        For volume conduction models:  
        If the input is a volume conductor model of the following type:  
          localspheres model  
          singleshell model with the spherical harmonic coefficients already computed  
          BEM model with system matrix already computed  
          FEM model with volumetric elements  
        only a rigid-body translation plus rotation are allowed.  
         
        If the input is a volume conductor model of the following type:  
          BEM model with the system matrix not yet computed  
          singleshell model with the spherical harmonic coefficients not yet computed  
        rotation, translation, global rescaling and individual axis rescaling is allowed.  
         
        If the input is a volume conductor model of the following type:  
          single sphere  
          concentric spheres  
        rotation, translation and global rescaling is allowed.  
         
        For source models, either defined as a 3D regular grid, a 2D mesh or unstructred  
        point cloud, rotation, translation, global rescaling and individual axis rescaling  
        is allowed.  
         
        For anatomical MRIs and functional volumetric data, rotation, translation, global  
        rescaling and individual axis rescaling are allowed.  
         
        See also FT_WARP_APPLY, FT_HEADCOORDINATES, FT_SCALINGFACTOR  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/ft_transform_geometry.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_transform_geometry", *args, **kwargs)
