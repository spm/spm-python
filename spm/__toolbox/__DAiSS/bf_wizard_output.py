from spm._runtime import Runtime


def bf_wizard_output(*args, **kwargs):
    r"""
      A handy command-line based batch filler with some defaults for DAiSS  
        output module, pick a few options, and it will default for unpopulated  
        fields  
         
        Current *definitely* supported output methods include:  
          - image_dics  
          - image_mv  
          - image_power  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DAiSS/bf_wizard_output.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_wizard_output", *args, **kwargs)
