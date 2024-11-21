from spm.__wrapper__ import Runtime


def spm_conv_full(*args, **kwargs):
    """
      Hanning convolution (return full arrays)  
        FORMAT [X] = spm_conv_full(X,sx,sy)  
        X    - matrix  
        sx   - kernel width (FWHM) in pixels  
        sy   - optional non-isomorphic smoothing  
       __________________________________________________________________________  
         
        spm_conv_full is a one or two dimensional convolution of a matrix  
        variable in working memory.  It capitalizes on the separablity of  
        multidimensional convolution with a hanning kernel by using  
        one-dimensional convolutions.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_conv_full.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_conv_full", *args, **kwargs)
