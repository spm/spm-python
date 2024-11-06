from spm.__wrapper__ import Runtime


def spm_fx_tfm_P(*args, **kwargs):
    """
      Exogenous input and input dependent parameters  
        FORMAT [u,P] = spm_fx_tfm_P(u,P)  
         
        arguments:  
        u  - inputs  
        P  - parameters  
         
        returns:  
        u  - exogenous (conductance) inputs driving states  
        P  - input dependent parameters  
         
        This is a help routine for the microcircuit models equations of motion -  
        it simply separates inputs into those affecting (driving) his neuronal  
        states and those modulating parameters. It returns the exogenous  
        (conductance) inputs and input dependent parameters.  
       ___________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_fx_tfm_P.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_fx_tfm_P", *args, **kwargs)
