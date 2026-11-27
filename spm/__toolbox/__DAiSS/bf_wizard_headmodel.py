from spm._runtime import Runtime


def bf_wizard_headmodel(*args, **kwargs):
    r"""
      A handy command-line based batch filler with some defaults for SPM  
        head model specification for MEEG data. Will generate the job which  
        performs coregistration between the data and the MRI  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DAiSS/bf_wizard_headmodel.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_wizard_headmodel", *args, **kwargs)
