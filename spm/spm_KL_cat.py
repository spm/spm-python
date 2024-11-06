from spm.__wrapper__ import Runtime


def spm_KL_cat(*args, **kwargs):
    """
      KL divergence between two categorical distributions  
        FORMAT [D] = spm_KL_cat(Q,P)  
         
        Calculates KL(Q||P) = <log Q/P> wrt Q between two categorical   
        distributions Q and P  
         
        If supplied with arrays, the KL divergence will be summed over the first  
        dimension. The arrays can be normalised (c.f., Dirichlet parameters).  
         
        See also: spm_kl_dirichlet.m (for row vectors)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_KL_cat.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_KL_cat", *args, **kwargs)
