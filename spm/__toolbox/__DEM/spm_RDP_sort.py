from spm._runtime import Runtime


def spm_RDP_sort(*args, **kwargs):
    r"""
      BMR using eigen-decomposition of allowable transitions   
        FORMAT [MDP,j] = spm_RDP_sort(MDP,['sort'])  
        MDP  - hierarchal RDP  
        sort - optional flag to supress pruning  
        j    - sorted indices (at highest level)  
         
        This routine uses the eigen-decomposition of allowable transitions (i.e.,  
        flow among states) to identify steady-state distributions (i.e., the  
        principal eigenvector with a real eigenvalue of unity). These  
        nonequilibrium steady-state (NESS) distributions correspond to the  
        attracting set; i.e., a pullback attractor.  
         
         Generalised states sorted according to the nonequilibrium steady-state  
         probability, which corresponds to the probability current through these  
         (generalised) states – because a path can never follow itself (and  
         therefore each generalised state will be vacated with probability one at  
         each time step).  
       __________________________________________________________________________  
        Copyright (C) 2005 Wellcome Trust Centre for Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_RDP_sort.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_RDP_sort", *args, **kwargs)
