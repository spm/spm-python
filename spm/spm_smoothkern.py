from spm.__wrapper__ import Runtime


def spm_smoothkern(*args, **kwargs):
    """
      Generate a Gaussian smoothing kernel  
        FORMAT krn = spm_smoothkern(fwhm,x,t)  
        fwhm - full width at half maximum  
        x    - position  
        t    - either 0 (nearest neighbour) or 1 (linear).  
               [Default: 1]  
         
        krn  - value of kernel at position x  
       __________________________________________________________________________  
         
        For smoothing images, one should really convolve a Gaussian with a sinc  
        function. For smoothing histograms, the kernel should be a Gaussian  
        convolved with the histogram basis function used. This function returns  
        a Gaussian convolved with a triangular (1st degree B-spline) basis   
        function (by default). A Gaussian convolved with a hat function (0th   
        degree B-spline) can also be returned.  
         
        Note that the convolution kernel returned by this function differ from  
        the ones that other packages currently use for Gaussian smoothing -  
        particularly when the FWHM is small compared with the voxel dimensions.  
        The fact that SPM does it differently from other software does not mean  
        that it is wrong.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_smoothkern.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_smoothkern", *args, **kwargs)
