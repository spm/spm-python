from spm._runtime import Runtime


def spm_dartel_template(*args, **kwargs):
    """
      Iteratively compute a template with mean shape and intensities  
        FORMAT spm_dartel_template(job)  
         
        The outputs are flow fields, and a series of Template images.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DARTEL/spm_dartel_template.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dartel_template", *args, **kwargs)
