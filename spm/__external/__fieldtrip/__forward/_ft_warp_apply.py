from spm.__wrapper__ import Runtime


def _ft_warp_apply(*args, **kwargs):
    """
      FT_WARP_APPLY performs a 3D linear or nonlinear transformation on the input  
        coordinates, similar to those in AIR. You can find technical documentation  
        on warping in general at http://air.bmap.ucla.edu/AIR5  
         
        Use as  
          [output] = ft_warp_apply(M, input, method, tol)  
        where  
          M        vector or matrix with warping parameters  
          input    Nx3 matrix with input coordinates  
          output   Nx3 matrix with the transformed or warped output coordinates  
          method   string describing the transformation or warping method  
          tol      (optional) value determining the numerical precision of the  
                   output, to deal with numerical round-off imprecisions due to  
                   the warping  
         
        The methods 'nonlin0', 'nonlin2' ... 'nonlin5' specify a polynomial transformation.  
        The size of the transformation matrix depends on the order of the warp  
          zeroth order :  1 parameter  per coordinate (translation)  
          first  order :  4 parameters per coordinate (total 12, affine)  
          second order : 10 parameters per coordinate  
          third  order : 20 parameters per coordinate  
          fourth order : 35 parameters per coordinate  
          fifth  order : 56 parameters per coordinate (total 168)  
        The size of M should be 3xP, where P is the number of parameters per coordinate.  
        Alternatively, you can specify the method to be 'nonlinear', in which case the  
        order will be determined from the size of the matrix M.  
         
        If the method 'homogeneous' is selected, the input matrix M should be a 4x4  
        homogenous transformation matrix.  
         
        If the method 'sn2individual' or 'individual2sn' is selected, the input M should be  
        a structure with the nonlinear spatial normalisation (warping) parameters created  
        by SPM8 or SPM12 for alignment between an individual subject and a template brain.  
        When using the 'old' method, M will have subfields like this:  
            Affine: [4x4 double]  
                Tr: [4-D double]  
                VF: [1x1 struct]  
                VG: [1x1 struct]  
             flags: [1x1 struct]  
        When using the 'new' or the 'mars' method, M will have subfields like this:  
         
        If any other method is selected, it is assumed that it specifies the name of an  
        auxiliary function that will, when given the input parameter vector M, return an  
        4x4 homogenous transformation matrix. Supplied functions are 'translate', 'rotate',  
        'scale', 'rigidbody', 'globalrescale', 'traditional', 'affine', 'perspective',  
        'quaternion'.  
         
        See also FT_AFFINECOORDINATES, FT_HEADCOORDINATES, FT_WARP_OPTIM, FT_WARP_ERROR,   
        MAKETFORM, AFFINE2D, AFFINE3D  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/ft_warp_apply.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_warp_apply", *args, **kwargs)
