from spm._runtime import Runtime


def spm_MDP_da(*args, **kwargs):
    r"""
      Simulated histograms of dopamine firing  
        FORMAT spm_MDP_da(MDP)  
         
        See also: spm_MDP_game, which generalises this scheme and replaces prior  
        beliefs about KL control with minimisation of expected free energy.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_MDP_da.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_MDP_da", *args, **kwargs, nargout=0)
