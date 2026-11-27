from spm._runtime import Runtime


def ft_transform_geometry(*args, **kwargs):
    r"""
      FT_TRANSFORM_GEOMETRY applies a homogeneous coordinate transformation to a  
        structure with geometric information, for example a volume conduction model for the  
        head, gradiometer of electrode structure containing EEG or MEG sensor positions and  
        MEG coil orientations, a head shape or a source model.  
         
        Use as  
          [output] = ft_transform_geometry(transform, input), or  
          [output] = ft_transform_geometry(transform, input, method)  
          
        The input data structure can be any of the FieldTrip data structures that describes  
        geometrical data.  
          
        Without specifying the method, the transform input argument should be a 4x4  
        homogeneous transformation matrix.  
          
        The method can also be specified as 'rotate', 'scale', 'translate', 'rigidbody', in  
        which case the transform is a set of parameters that can be converted into a 4x4  
        homogeneous transformation matrix. All methods require a 3-element vector as  
        parameters, apart from rigidbody, which requires a 6-element vector.  
         
        The units of the translation or transformation matrix must be the same as the units  
        in which the geometric object is expressed.  
         
        The type of geometric object constrains the type of allowed transformations.  
         
        If the input is an MEG gradiometer array, only a rigid-body translation plus  
        rotation are allowed. If the input is an EEG electrode or fNIRS optodes array,  
        global rescaling and individual axis rescaling is also allowed.  
         
        If the input is a volume conductor model of the following type:  
          - BEM model with system matrix already computed  
          - FEM model with volumetric elements  
          - localspheres model  
          - singleshell model with the spherical harmonic coefficients already computed  
        then only a rigid-body translation plus rotation are allowed.  
         
        If the input is a volume conductor model of the following type:  
          - BEM model with the system matrix not yet computed  
          - singleshell model with the spherical harmonic coefficients not yet computed  
        then rotation, translation, global rescaling and individual axis rescaling is  
        allowed.  
         
        If the input is a volume conductor model of the following type:  
          single sphere  
          concentric spheres  
        then rotation, translation and global rescaling is allowed.  
         
        For source models, either defined as a 3D regular grid, a 2D mesh or unstructred  
        point cloud, rotation, translation, global rescaling and individual axis rescaling  
        is allowed.  
         
        For anatomical MRIs and functional volumetric data, rotation, translation, global  
        rescaling and individual axis rescaling are allowed.  
         
        See also FT_WARP_APPLY, FT_HEADCOORDINATES, FT_SCALINGFACTOR  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/ft_transform_geometry.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_transform_geometry", *args, **kwargs)
