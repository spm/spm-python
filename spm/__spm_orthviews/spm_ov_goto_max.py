from spm._runtime import Runtime


def spm_ov_goto_max(*args, **kwargs):
    """
      Goto maximum intensity tool - plugin for spm_orthviews  
         
        This tool provides capabilities similar to the "Goto ... maximum"  
        functionality in spm_mip_ui.m. When the tool is called for the first  
        time, it has to read the whole image data file. This might result in a  
        slow response depending on the image dimensions.  
         
        This routine is a plugin to spm_orthviews. For general help about  
        spm_orthviews and plugins type  
                    help spm_orthviews  
        at the MATLAB prompt.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_orthviews/spm_ov_goto_max.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_ov_goto_max", *args, **kwargs)
