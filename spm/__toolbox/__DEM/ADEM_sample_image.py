from spm.__wrapper__ import Runtime


def ADEM_sample_image(*args, **kwargs):
    """
      samples a (memory mapped) image at displacement o  
        FORMAT [s] = ADEM_sample_image(V,o,R)  
        FORMAT [s] = ADEM_sample_image(o,h)  
         
        V - a structure array containing image volume information  
        o - coordinates of foveal sampling:  
          o(1) - oculomotor angle  
          o(2) - oculomotor angle  
        R - retinal modulation (n x n)  
         
        or  
         
        o - coordinates of foveal sampling  
        h - vector of coefficients weighting images in STIM.H{:}  
         
        s - sensory sample (n x n)  
          
        requires a global variable with the following fields:  
        STIM.R = contrast modulation matrix that defines resolution  
        STIM.W = width of foveal sampling of an image   (default: 1/6)  
        STIM.P = image position in retinal  coordinates (default: [0;0])  
        STIM.B = basis functions or receptive fields    (default: 1)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/ADEM_sample_image.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ADEM_sample_image", *args, **kwargs)
