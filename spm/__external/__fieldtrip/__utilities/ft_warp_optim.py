from spm.__wrapper__ import Runtime


def ft_warp_optim(*args, **kwargs):
    """
      FT_WARP_OPTIM determine intermediate positions using warping (deformation)  
        the input cloud of points is warped to match the target.  
        The strategy is to start with simpelest linear warp, followed by a more  
        elaborate linear warp, which then is followed by the nonlinear warps up  
        to the desired order.  
         
        [result, M] = ft_warp_pnt(input, target, method)  
            input          contains the Nx3 measured 3D positions  
            target         contains the Nx3 template 3D positions  
            method         should be any of   
                            'rigidbody'  
                            'globalrescale'  
                            'traditional' (default)  
                            'nonlin1'  
                            'nonlin2'  
                            'nonlin3'  
                            'nonlin4'  
                            'nonlin5'  
         
        The default warping method is a traditional linear warp with individual  
        rescaling in each dimension. Optionally you can select a nonlinear warp  
        of the 1st (affine) up to the 5th order.  
         
        When available, this function will use the MATLAB optimization toolbox.  
         
        See also FT_WARP_APPLY, FT_WARP_ERRROR  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/ft_warp_optim.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_warp_optim", *args, **kwargs)
