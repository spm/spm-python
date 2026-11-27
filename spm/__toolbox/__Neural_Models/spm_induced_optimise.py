from spm._runtime import Runtime


def spm_induced_optimise(*args, **kwargs):
    r"""
      Demo routine that computes transfer functions for free parameters  
       ==========================================================================  
         
        This an exploratory routine that computes the modulation transfer function  
        for a range of parameters and states to enable the spectral responses to   
        be optimised with respect to the model parameters of neural mass models   
        under different hidden states.  
         
        By editing the script, one can change the neuronal model or the hidden  
        neuronal states that are characterised in terms of induced responses  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/Neural_Models/spm_induced_optimise.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_induced_optimise", *args, **kwargs, nargout=0)
