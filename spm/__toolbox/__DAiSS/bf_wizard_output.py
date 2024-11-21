from spm.__wrapper__ import Runtime


def bf_wizard_output(*args, **kwargs):
    """
      A handy command-line based batch filler with some defaults for DAiSS  
        output module, pick a few options, and it will default for unpopulated  
        fields  
         
        Current *definitely* supported output methods include:  
          - image_dics  
          - image_mv  
          - image_power  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_wizard_output.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bf_wizard_output", *args, **kwargs)
