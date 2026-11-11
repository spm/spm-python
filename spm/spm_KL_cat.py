from spm._runtime import Runtime


def spm_KL_cat(*args, **kwargs):
    r"""
      KL divergence between two categorical distributions  
        FORMAT [D] = spm_KL_cat(Q,P)  
         
        Calculates KL(Q||P) = <log Q/P> wrt Q between two categorical   
        distributions Q and P  
         
        If supplied with arrays, the KL divergence will be summed over the first  
        dimension. The arrays can be normalised (c.f., Dirichlet parameters).  
         
        See also: spm_KL_dir (for arrays) and spm_kl_dirichlet.m (for row vectors)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_KL_cat.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_KL_cat", *args, **kwargs)
