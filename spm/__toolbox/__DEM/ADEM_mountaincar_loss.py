from spm.__wrapper__ import Runtime


def ADEM_mountaincar_loss(*args, **kwargs):
    """
      This demo re-visits the mountain car problem to show that adaptive  
        (desired) behaviour can be prescribed in terms of loss-functions (i.e.  
        reward functions of state-space).  
        It exploits the fact that under the free-energy formulation, loss is  
        divergence. This means that priors can be used to make certain parts of  
        state-space costly (i.e. with high divergence) and others rewarding (low  
        divergence). Active inference under these priors will lead to sampling of  
        low cost states and (apparent) attractiveness of those states.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/ADEM_mountaincar_loss.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ADEM_mountaincar_loss", *args, **kwargs, nargout=0)
