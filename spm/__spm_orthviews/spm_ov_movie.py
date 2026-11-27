from spm._runtime import Runtime


def spm_ov_movie(*args, **kwargs):
    r"""
      Movie tool - plugin for spm_orthviews  
         
        This plugin allows an automatic "fly-through" through all displayed  
        volumes. Apart from pre-defined trajectories along the x-, y- and z-axis,  
        resp., it is possible to define custom start and end points (in mm) for  
        oblique trajectories.  
         
        Displayed movies can be captured and saved as video files. One movie per  
        image and axis (i.e. slice display) will be created. Movie resolution is  
        given by the displayed image size, frame rate is MATLAB standard.  
         
        This routine is a plugin to spm_orthviews. For general help about  
        spm_orthviews and plugins type  
                    help spm_orthviews  
        at the MATLAB prompt.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_orthviews/spm_ov_movie.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_ov_movie", *args, **kwargs)
