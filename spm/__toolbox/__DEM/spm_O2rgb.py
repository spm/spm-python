from spm._runtime import Runtime


def spm_O2rgb(*args, **kwargs):
    r"""
      O to RGB image format  
        FORMAT I = spm_O2rgb(O,RGB)  
         
        Converts discrete (probabilistic) image into an RGB format for image  
        display.  
         
        This routine generates an image[s] using spatiotemporal basis functions  
        weighted by expected singular variates; where the requisite expectations  
        are evaluated over discrete values, given a multinomial distribution over  
        those values. (If multiple images are supplied over the first is shown)  
         
        see: spm_rgb2O  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_O2rgb.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_O2rgb", *args, **kwargs)
