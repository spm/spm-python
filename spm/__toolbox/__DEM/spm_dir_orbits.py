from spm._runtime import Runtime


def spm_dir_orbits(*args, **kwargs):
    r"""
      information geometry of a likelihood mapping  
        FORMAT [u] = spm_dir_orbits(b,hid,N)  
        b      - transition tensor  
        hid    - states to highlight  
        P      - (Ns x Nt) sequence of (probabilistic) states  
        N      - rotate to show first N (generalised) states  
         
        This routine plots latent states in the first two principal eigenvectors  
        of (roughly) the graph Laplacian of transitions among states. The  
        transitions among states are supplied in terms of a transition tensor  
        (that is summed over the third dimension or perhaps). The states are then  
        connected with arrows denoting transitions over time. In effect, this is  
        a visual representation of orbits and paths in terms of follows in latent  
        state space.  
         
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_dir_orbits.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dir_orbits", *args, **kwargs)
