from spm.__wrapper__ import Runtime


def spm_changepath(*args, **kwargs):
    """
      Recursively replace all occurrences of a text pattern in a variable  
        FORMAT S = spm_changepath(Sf, oldp, newp)  
         
        Sf       - MATLAB variable to fix, or char array of MAT filenames,  
                   or directory name (all found MAT files will be analysed)  
        oldp     - old string to replace  
        newp     - new string replacing oldp  
         
        S        - updated MATLAB variable (only if Sf is one)  
         
        If the pattern is found in a string, any occurrence of an invalid file  
        separator is replaced to match that of the current system.  
         
        If MAT filenames are specified, they will be overwritten with the new  
        version. A backup of the initial version is made with a ".old" suffix.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_changepath.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_changepath", *args, **kwargs)
