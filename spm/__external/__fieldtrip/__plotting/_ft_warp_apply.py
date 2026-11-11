from spm._runtime import Runtime


def _ft_warp_apply(*args, **kwargs):
    r"""
      FT_WARP_APPLY performs a 3D linear or nonlinear transformation on the input  
        coordinates, similar to those in AIR. You can find technical documentation  
        on warping in general at http://air.bmap.ucla.edu/AIR5  
         
        Use as  
          [output] = ft_warp_apply(transform, input, method, tol)  
        where  
          transform   vector or matrix with warping parameters  
          input       Nx3 matrix with input coordinates  
          output      Nx3 matrix with the transformed or warped output coordinates  
          method      string describing the transformation or warping method  
          tol         (optional) value determining the numerical precision of the  
                        output, to deal with numerical round-off imprecisions due to  
                        the warping  
         
        The methods 'nonlin0', 'nonlin2' ... 'nonlin5' specify a polynomial transformation.  
        The size of the specified transform depends on the order of the warp  
          zeroth order :  1 parameter  per coordinate (translation)  
          first  order :  4 parameters per coordinate (total 12, affine)  
          second order : 10 parameters per coordinate  
          third  order : 20 parameters per coordinate  
          fourth order : 35 parameters per coordinate  
          fifth  order : 56 parameters per coordinate (total 168)  
        The size of the specified transform should be 3xP, where P is the number of  
        parameters per coordinate. Alternatively, you can specify the method to be  
        'nonlinear', in which case the order will be determined from the size of the  
        specified transform.  
         
        If the method 'homogeneous' is selected, the specified transform should be a 4x4  
        homogenous transformation matrix.  
         
        If the method 'sn2individual' or 'individual2sn' is selected, the specified  
        transform should be a structure with the nonlinear spatial normalisation (warping)  
        parameters created by SPM8 or SPM12 for alignment between an individual subject and  
        a template brain. The specified transform is a structure with fields like this:  
            Affine: [4x4 double]  
                Tr: [4-D double]  
                VF: [1x1 struct]  
                VG: [1x1 struct]  
             flags: [1x1 struct]  
         
        If any other method is selected, it is assumed that it specifies the name of an  
        auxiliary function that will, when given the specified transform vector, return an  
        4x4 homogenous transformation matrix. Supplied functions are 'translate', 'rotate',  
        'scale', 'rigidbody', 'globalrescale', 'traditional', 'affine', 'perspective',  
        'quaternion'.  
         
        See also FT_AFFINECOORDINATES, FT_HEADCOORDINATES, FT_WARP_OPTIM, FT_WARP_ERROR,   
        MAKETFORM, AFFINE2D, AFFINE3D  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/plotting/private/ft_warp_apply.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_warp_apply", *args, **kwargs)
