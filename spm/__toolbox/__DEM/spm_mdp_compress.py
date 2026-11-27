from spm._runtime import Runtime


def spm_mdp_compress(*args, **kwargs):
    r"""
      FORMAT mdp = spm_mdp_compress(mdp)  
        mdp  - MDP structure  
          mdp.a{g} - likelihood matrices   
          mdp.b{1} - prior transition tensor   
         
        This routine compresses the likelihood and transition tensors for a  
        single factor, encoded in the a and B (Dirichlet) fields of mdp. This  
        lossless compression is based upon changes in the mutual information  
        (i.e., negative expected free energy) after moving Dirichlet counts among  
        various rows and columns.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_mdp_compress.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mdp_compress", *args, **kwargs)
