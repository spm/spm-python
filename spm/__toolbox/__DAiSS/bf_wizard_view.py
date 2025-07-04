from spm._runtime import Runtime


def bf_wizard_view(*args, **kwargs):
    """
      A handy command-line based batch filler with some defaults for DAiSS  
        view module, pick a few options, and it will default for unpopulated  
        fields  
         
        Currently supported output methods include:  
          - glass  
          - surface  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_wizard_view.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_wizard_view", *args, **kwargs)
