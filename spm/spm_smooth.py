from spm.__wrapper__ import Runtime


def spm_smooth(*args, **kwargs):
    """
      3 dimensional convolution of an image  
        FORMAT spm_smooth(P,Q,s,dtype)  
        P     - image(s) to be smoothed (or 3D array)  
        Q     - filename for smoothed image (or 3D array)  
        s     - [sx sy sz] Gaussian filter width {FWHM} in mm (or edges)  
        dtype - datatype [Default: 0 == same datatype as P]  
       __________________________________________________________________________  
         
        spm_smooth is used to smooth or convolve images in a file (maybe).  
         
        The sum of kernel coefficients are set to unity.  Boundary  
        conditions assume data does not exist outside the image in z (i.e.  
        the kernel is truncated in z at the boundaries of the image space). S  
        can be a vector of 3 FWHM values that specify an anisotropic  
        smoothing.  If S is a scalar isotropic smoothing is implemented.  
         
        If Q is not a string, it is used as the destination of the smoothed  
        image.  It must already be defined with the same number of elements  
        as the image.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_smooth.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_smooth", *args, **kwargs, nargout=0)
