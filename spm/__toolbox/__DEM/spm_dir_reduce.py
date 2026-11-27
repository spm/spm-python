from spm._runtime import Runtime


def spm_dir_reduce(*args, **kwargs):
    r"""
      Compression of a (Dirichlet) probability tensor  
        FORMAT [R] = spm_dir_reduce(a)  
        a  - [cell array] of likelhoods  
        R  - reduction matrix: a*R = reduced Dirichlet likelihood mapping  
         
        This routine returns a reduction matrix (R) that compresses a joint  
        probability distribution parameterised with Dirichlet counts. This can be  
        regarded as a simple and efficient kind of Bayesian model reduction in  
        which the mutual information or expected free energy is preserved (i.e.,  
        with minimal information loss). The reduction effectively combines  
        columns of the implicit likelihood that are similar — in the sense that  
        there information distance is less than one natural unit [more precisely,  
        sqrt(2)]. This uses an efficient unique operator, based upon thresholded  
        information distance.  
       __________________________________________________________________________  
        Copyright (C) 2005 Wellcome Trust Centre for Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_dir_reduce.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dir_reduce", *args, **kwargs)
