from spm.__wrapper__ import Runtime


def spm_lfp_demo(*args, **kwargs):
    """
      Demo routine for local field potential models  
       ==========================================================================  
         
        This is a generic demonstration of neural-mass models that illustrates  
        various impulse response behaviours. It is meant to show how to specify  
        a neural-mass model, examine its response properties using Volterra  
        kernels and transfer functions and generate electrophysiological and  
        hemodynamic responses from the same model. It is anticipated that people  
        will go through the code to see how the routines relate to each other.  
         
        This demo contains a linear stability analysis, which can be useful for  
        identifying useful domains of parameter space (here the inhibitory time-  
        constant)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Neural_Models/spm_lfp_demo.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_lfp_demo", *args, **kwargs, nargout=0)
