from spm.__wrapper__ import Runtime


def spm_mkdir(*args, **kwargs):
    """
      Make new directory trees  
        FORMAT sts = spm_mkdir(dir,...)  
        dir    - character array, or cell array of strings  
         
        sts    - true if all directories were successfully created or already  
                 existing, false otherwise.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mkdir.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mkdir", *args, **kwargs)
