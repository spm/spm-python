from spm.__wrapper__ import Runtime


def spm_MDP_VB_LFP(*args, **kwargs):
    """
      auxiliary routine for plotting simulated electrophysiological responses  
        FORMAT [v] = spm_MDP_VB_LFP(MDP,UNITS,FACTOR,SPECTRAL)  
         
        MDP        - structure (see spm_MDP_VB_X.m)  
         .xn       - neuronal firing  
         .dn       - phasic dopamine responses  
         
        UNITS(1,:) - hidden state                           [default: all]  
        UNITS(2,:) - time step  
         
        FACTOR     - hidden factor to plot                  [default: 1]  
        SPECTRAL   - replace raster with spectral responses [default: 0]  
         
        v - selected unit responses {number of trials, number of units}  
         
        This routine plots simulated electrophysiological responses. Graphics are  
        provided in terms of simulated spike rates (posterior expectations).  
         
        see also: spm_MDP_VB_ERP (for hierarchical belief updating)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_MDP_VB_LFP.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_MDP_VB_LFP", *args, **kwargs)
