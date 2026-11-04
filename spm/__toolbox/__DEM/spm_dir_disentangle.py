from spm._runtime import Runtime


def spm_dir_disentangle(*args, **kwargs):
    r"""
      information geometry of a likelihood mapping  
        FORMAT [e,v,c] = spm_dir_disentangle(a,n)  
        a{g}    - Dirichlet tensor for modality g  
        n       - nummber of (first) latent states to plot  
         
        This routine illustrates the information geometry inherent in a  
        likelihood mapping. It computes a similarity matrix based upon an  
        approximation to the information length between columns of a likelihood  
        tensor (as approximated by the KL divergence of the implicit categorical  
        distributions). It then plots a certain number of latent states in the  
        ensuing eigenspace; along with the eiegnspectrum.  
         
        seee also spm_information_distance.m  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_dir_disentangle.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dir_disentangle", *args, **kwargs)
