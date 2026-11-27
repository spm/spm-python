from spm._runtime import Runtime


def spm_ov_rgb(*args, **kwargs):
    r"""
      RGB overlays - plugin for spm_orthviews  
        A shorthand to overlaying the absolute value of three different images  
        onto a displayed image in colours red, green and blue. The overlay images  
        are optionally masked and multiplied with a scaling image. The displayed  
        overlay images are the absolute value of the given overlays.  
         
        This routine is a plugin to spm_orthviews. For general help about  
        spm_orthviews and plugins type  
                    help spm_orthviews  
        at the MATLAB prompt.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_orthviews/spm_ov_rgb.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_ov_rgb", *args, **kwargs)
