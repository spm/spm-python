from spm._runtime import Runtime


def spm_rgm_group(*args, **kwargs):
    r"""
      Compression of a (Dirichlet) probability tensor  
        FORMAT [G] = spm_rgm_group(O,dx)  
        O  - [No x Nt cell array] of likelhoods  
        dx - upper bound on size of group  
        m  - number of modalities per outcome  
         
        This auxiliary routine takes a set of probability distributions assembled  
        in a cell array (outcomes times the number of instances). It then  
        evaluates the mutual information among outcomes. In virtue of the  
        positive definiteness of this matrix, one can then use the principal  
        eigenvector to identify a partition of outcomes: c.f., Spectral  
        clustering under the Perron–Frobenius theorem. Outcomes that do not share  
        any information with other outcomes are assigned to their own group. The  
        size of each subset (i.e., group) is specified with an upper bound, which  
        determines the scaling law in terms of the renormalisation group.  
       __________________________________________________________________________  
        Copyright (C) 2005 Wellcome Trust Centre for Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_rgm_group.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_rgm_group", *args, **kwargs)
