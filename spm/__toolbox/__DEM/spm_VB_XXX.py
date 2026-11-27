from spm._runtime import Runtime


def spm_VB_XXX(*args, **kwargs):
    r"""
      A fast form of MDP inversion  
        FORMAT pdp   = spm_VB_XXX(pdp)  
        pdp - likelihood (A) and transition (B) tensors for this sequence (O)  
         
        This subroutine is a stripped down version of the MDP inversion schemes  
        that exploits situations in which each likelihood mapping is a matrix;  
        i.e., the latent states are conditionally independent because each  
        likelihood has only one parent (and there are no priors).  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_VB_XXX.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_VB_XXX", *args, **kwargs)
