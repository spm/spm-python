from spm._runtime import Runtime


def spm_neil(*args, **kwargs):
    r"""
      Demo routine for hemodynamic model  
       ==========================================================================  
        For Prof Neil Burgess  
        Inst of Cognitive Neuroscience (Deputy Director), and Inst of Neurology  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/Neural_Models/spm_neil.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_neil", *args, **kwargs, nargout=0)
