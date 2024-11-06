from spm.__wrapper__ import Runtime


def spm_grid(*args, **kwargs):
    """
      Superimpose a Talairach and Tournoux grid  
        FORMAT O = spm_grid(I)  
        I - image matrix  
        O - image matrix with grid added  
       __________________________________________________________________________  
         
        spm_grid adds a grid to the input argument.  
        The grid is scaled to 10% of the input's maximum.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_grid.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_grid", *args, **kwargs)
