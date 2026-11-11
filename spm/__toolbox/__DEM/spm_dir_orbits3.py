from spm._runtime import Runtime


def spm_dir_orbits3(*args, **kwargs):
    r"""
      information geometry of a likelihood mapping  
        FORMAT [u] = spm_dir_orbits3(b,hid)  
        b      - transition tensor  
        hid    - states to highlight  
         
        This routine plots latent states in the first three principal  
        eigenvectors of (roughly) the graph Laplacian of transitions among  
        states. The transitions among states are supplied in terms of a  
        transition tensor (that is summed over the third dimension or perhaps).  
        This is a visual representation of orbits and paths in terms of follows  
        in latent state space.  
         
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_dir_orbits3.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dir_orbits3", *args, **kwargs)
