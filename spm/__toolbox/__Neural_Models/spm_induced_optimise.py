from spm.__wrapper__ import Runtime


def spm_induced_optimise(*args, **kwargs):
    """
      Demo routine that computes transfer functions for free parameters  
       ==========================================================================  
         
        This an exploratory routine that computes the modulation transfer function  
        for a range of parameters and states to enable the spectral responses to   
        be optimised with respect to the model parameters of neural mass models   
        under different hidden states.  
         
        By editing the script, one can change the neuronal model or the hidden  
        neuronal states that are characterised in terms of induced responses  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Neural_Models/spm_induced_optimise.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_induced_optimise", *args, **kwargs, nargout=0)
