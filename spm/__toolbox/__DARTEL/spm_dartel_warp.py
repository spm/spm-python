from spm.__wrapper__ import Runtime


def spm_dartel_warp(*args, **kwargs):
    """
      Register images to template data  
        format spm_dartel_warp(job)  
         
        The outputs are flow fields.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DARTEL/spm_dartel_warp.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dartel_warp", *args, **kwargs)
