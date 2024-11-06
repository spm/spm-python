from spm.__wrapper__ import Runtime


def _cfg_maxextent(*args, **kwargs):
    """
      CFG_MAXEXTENT Returns the maximum extent of cellstr STR   
        Returns the maximum extent of obj OBJ when the cellstr STR will be  
        rendered in it. MATLAB is not able to work this out correctly on its own  
        for multiline strings. Therefore each line will be tried separately and  
        its extent will be returned. To avoid 'flicker' appearance, OBJ should be  
        invisible. The extent does not include the width of a scrollbar.  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/private/cfg_maxextent.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("cfg_maxextent", *args, **kwargs)
