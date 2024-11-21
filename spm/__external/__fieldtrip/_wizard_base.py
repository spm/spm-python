from spm.__wrapper__ import Runtime


def _wizard_base(*args, **kwargs):
    """
      This is the low level wizard function. It evaluates the MATLAB content  
        in the workspace of the calling function. To prevent overwriting  
        variables in the BASE workspace, this function should be called from a  
        wrapper function. The wrapper function whoudl pause execution untill the  
        wizard figure is deleted.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/wizard_base.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("wizard_base", *args, **kwargs)
