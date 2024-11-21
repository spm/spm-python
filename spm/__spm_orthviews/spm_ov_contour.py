from spm.__wrapper__ import Runtime


def spm_ov_contour(*args, **kwargs):
    """
      Contour tool - plugin for spm_orthviews  
         
        This routine is a plugin to spm_orthviews. For general help about  
        spm_orthviews and plugins type  
                    help spm_orthviews  
        at the MATLAB prompt.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_orthviews/spm_ov_contour.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_ov_contour", *args, **kwargs)
