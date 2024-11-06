from spm.__wrapper__ import Runtime


def spm_dcm_neural_x(*args, **kwargs):
    """
      Return the fixed point or steady-state of a neural mass DCM  
        FORMAT [x] = spm_dcm_neural_x(P,M)  
         
        P   - parameter structure  
        M   - model structure  
         
        x   - steady state solution  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_dcm_neural_x.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_neural_x", *args, **kwargs)
