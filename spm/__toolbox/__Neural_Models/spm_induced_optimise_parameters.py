from spm.__wrapper__ import Runtime


def spm_induced_optimise_parameters(*args, **kwargs):
    """
      Demo routine that optimises free parameters  
       ==========================================================================  
         
        This exemplar routine illustrates how one can adjust or tune prior  
        parameter expectations to produce desired spectral responses as specified  
        by the complex eigenvalue spectrum - or a reduced form that considers a  
        small number of complex values (roots).  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Neural_Models/spm_induced_optimise_parameters.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_induced_optimise_parameters", *args, **kwargs)
