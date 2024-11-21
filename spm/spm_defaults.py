from spm.__wrapper__ import Runtime


def spm_defaults(*args, **kwargs):
    """
      Set the defaults which are used by SPM  
       __________________________________________________________________________  
         
        If you want to customise some defaults for your installation, do not  
        modify this file directly, but create a file named spm_my_defaults.m  
        instead, accessible from MATLAB search path; e.g., it can be saved in  
        MATLAB Startup Folder: <userhome>/Documents/MATLAB.  
         
        Example: create the following file to change the image file extension:  
        ----------- file /home/karl/Documents/MATLAB/spm_my_defaults.m -----------  
        global defaults  
        defaults.images.format = 'img';  
       --------------------------------------------------------------------------  
         
        spm_defaults should not be called directly in any script or function  
        (apart from SPM internals).  
        To load the defaults, use spm('Defaults',modality).  
        To get/set the defaults, use spm_get_defaults.  
         
                        ** This file should not be edited **  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_defaults.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_defaults", *args, **kwargs, nargout=0)
