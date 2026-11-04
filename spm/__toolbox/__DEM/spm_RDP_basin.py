from spm._runtime import Runtime


def spm_RDP_basin(*args, **kwargs):
    r"""
      BMR of superordinate states based upon predicted outcomes  
        FORMAT [MDP,d,o,h,c] = spm_RDP_basin(MDP,S,chi,L)  
        MDP  - cell array of MDP structures  
        S    - list of modality streams;    e.g., [2,3]  
        chi  - log prior for each modality; e.g., [8,-8]  
        L    - length of paths to and from goal states; e.g., [32,1]   
         
        MDP  - reduced MDP  
        d    - vector indicating whether deep states have children [true]  
        o    - vector indicating whether deep states have parents  [true]  
        h    - list of goal states  
        c    - list of cost states  
         
        This routine implements a Bayesian model reduction in which the latent  
        (generalised) states at the highest level of the model are retained only  
        if they lie in the basins of attraction of generalised (deep) states  
        specified by intended states (i.e., indexed by hid) precluding  
        transitions through costly states (i.e., indexed by cid).  
         
        see: https://en.wikipedia.org/wiki/Absorbing_Markov_chain  
       __________________________________________________________________________  
        Copyright (C) Karl Friston  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_RDP_basin.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_RDP_basin", *args, **kwargs)
