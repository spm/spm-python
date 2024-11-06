from spm.__wrapper__ import Runtime


def spm_check_filename(*args, **kwargs):
    """
      Check paths are valid and try to restore path names  
        FORMAT V = spm_check_filename(V)  
         
        V - struct array of file handles  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_check_filename.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_check_filename", *args, **kwargs)
