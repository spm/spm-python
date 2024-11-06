from spm.__wrapper__ import Runtime


def isfile(*args, **kwargs):
    """
     ISFILE Determine if the input points to a file  
          TF = ISFILE(INPUT) returns true if INPUT points to a file and false otherwise.  
         
        This is a compatibility function that should only be added to the path on  
        MATLAB versions prior to R2017b. Note that currently this function only allows  
        for a single string in the input, as opposed to the isfile function from MATLAB,  
        which allows for multiple inputs  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/compat/matlablt2017b/isfile.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("isfile", *args, **kwargs)
