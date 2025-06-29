from spm._runtime import Runtime


def spm_neil(*args, **kwargs):
    """
      Demo routine for hemodynamic model  
       ==========================================================================  
        For Prof Neil Burgess  
        Inst of Cognitive Neuroscience (Deputy Director), and Inst of Neurology  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Neural_Models/spm_neil.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_neil", *args, **kwargs, nargout=0)
