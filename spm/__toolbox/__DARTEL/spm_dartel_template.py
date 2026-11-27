from spm._runtime import Runtime


def spm_dartel_template(*args, **kwargs):
    r"""
      Iteratively compute a template with mean shape and intensities  
        FORMAT spm_dartel_template(job)  
         
        The outputs are flow fields, and a series of Template images.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DARTEL/spm_dartel_template.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dartel_template", *args, **kwargs)
