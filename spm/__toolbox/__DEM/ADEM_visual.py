from spm.__wrapper__ import Runtime


def ADEM_visual(*args, **kwargs):
    """
      DEM demo for active inference (i.e. action-perception optimisation of free  
        energy).  This simulation calls on spm_ADEM to simulate visual sampling of  
        the world and demonstrate retinal stabilisation or visual tracking. We  
        simulate a simple 2-D plaid stimulus and subject it to an exogenous  
        perturbations. By employing tight and broad priors on the location of the  
        stimulus, we can show that action does and does not explain away the visual  
        consequences of the perturbation (i.e., the movement is seen or not).  This  
        illustrates how one can reframe stabilisation or tracking in terms of  
        sampling sensory input to ensure conditional expectations are met; and  
        how these expectations are shaped by prior expectations.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/ADEM_visual.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ADEM_visual", *args, **kwargs, nargout=0)
