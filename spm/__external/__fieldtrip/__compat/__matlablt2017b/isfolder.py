from spm.__wrapper__ import Runtime


def isfolder(*args, **kwargs):
    """
     ISFOLDER Determine if the input path points to a folder  
          TF = ISFOLDER(PATH) returns true if PATH points to a folder and false otherwise.  
         
        This is a compatibility function that should only be added to the path on  
        MATLAB versions prior to R2017b.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/compat/matlablt2017b/isfolder.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("isfolder", *args, **kwargs)
