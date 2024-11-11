from spm.__wrapper__ import Runtime


def bf_wizard_headmodel(*args, **kwargs):
    """
      A handy command-line based batch filler with some defaults for SPM  
        head model specification for MEEG data. Will generate the job which  
        performs coregistration between the data and the MRI  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_wizard_headmodel.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bf_wizard_headmodel", *args, **kwargs)
