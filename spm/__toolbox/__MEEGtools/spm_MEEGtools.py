from spm.__wrapper__ import Runtime


def spm_MEEGtools(*args, **kwargs):
    """
      GUI gateway to MEEGtools toolbox  
         
        Disclaimer: the code in this directory is provided as an example and is  
        not guaranteed to work with data on which it was not tested. If it does  
        not work for you, feel free to improve it and contribute your  
        improvements to the MEEGtools toolbox in SPM  
        (https://www.fil.ion.ucl.ac.uk/spm)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_MEEGtools.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_MEEGtools", *args, **kwargs, nargout=0)
