from spm._runtime import Runtime


def spm_unique(*args, **kwargs):
    r"""
      Information geometry of a likelihood mapping or [probabilitic] outcome  
        FORMAT [i,j] = spm_unique(O)  
        O{n,m}    - cell array of Dirichlet counts or outcomes  
         
        returns indices (i,j) where U = O(i) and O = U(j)  
        where U = unique(O{:,u})  
         
        This routine uses the information geometry inherent in a likelihood  
        mapping. It computes a distance matrix based upon the information length  
        between columns of likelihood tensors and finds unique columns.  
       __________________________________________________________________________  
        Karl Friston  
        Copyright (C) 2012-2022 Wellcome Centre for Human Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_unique.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_unique", *args, **kwargs)
