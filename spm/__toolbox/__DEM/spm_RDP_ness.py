from spm._runtime import Runtime


def spm_RDP_ness(*args, **kwargs):
    r"""
      BMR using eigen-decomposition of allowable transitions   
        FORMAT [MDP] = spm_RDP_ness(MDP,S,chi)  
        MDP - hierarchal RDP  
        S    - list of modality streams;    e.g., [2, 3]  
        chi  - log prior for each modality; e.g., [8,-8]   
         
        This routine uses the eigen-decomposition of allowable transitions (i.e.,  
        flow among states) to identify steady-state distributions (i.e., the  
        principal eigenvector with a real eigenvalue of unity). These  
        nonequilibrium steady-state (NESS) distributions correspond to the  
        attracting set; i.e., a pullback attractor.  
         
        The derivative of expected cost is then evaluated with respect to  
        reducing the transition probabilities to each state in turn (provided  
        it's removal does not render another state childless). If reducing the  
        probability of visiting a generalised state increases expected goals  
        (i.e., expected occupancy of goal states under the nonequilibrium  
        steady-state density), it is removed.  
       __________________________________________________________________________  
        Copyright (C) 2005 Wellcome Trust Centre for Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_RDP_ness.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_RDP_ness", *args, **kwargs)
