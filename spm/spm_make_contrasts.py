from spm.__wrapper__ import Runtime


def spm_make_contrasts(*args, **kwargs):
    """
      Make contrasts for one, two or three-way ANOVAs  
        FORMAT Con = spm_make_contrasts(k)  
         
        k        - vector where the ith entry is the number of levels of factor i  
         
        Con      - struct array with fields:  
        Con(c).c    - Contrast matrix  
              .name - Name  
         
        This function computes contrasts for a generic k(1)-by-k(2)-by-k(3)  
        design. It is assumed that the levels of the first factor change slowest.  
         
        For one-way ANOVAs set k=L, where L is the number of  
        levels, for two-way ANOVAs set k=[L1 L2], for three way set k=[L1 L2 L3]  
         
        This function generates (transposed) contrast matrices to test  
        average effect, main effect of each factor and interactions.  
       __________________________________________________________________________  
         
        Reference:  
         
        For details of Kronecker operations, see section 5 of  
            http://www.fil.ion.ucl.ac.uk/~wpenny/publications/rik_anova.pdf  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_make_contrasts.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_make_contrasts", *args, **kwargs)
