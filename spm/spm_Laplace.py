from spm.__wrapper__ import Runtime


def spm_Laplace(*args, **kwargs):
    """
      Solve Laplace's equation on a regular grid  
        FORMAT u = spm_Laplace(u)  
        u        - potential field as a 3D array with values:  
                   Inf: interior points (unknown values)  
                   NaN: insulated boundaries  
                   <b>: Dirichlet boundary conditions  
         
        u        - filled-in potential field using Laplace's equation  
       __________________________________________________________________________  
         
        Potential field u should not have unknown values (Inf) at the first order  
        boundary of the 3D array. Set them as insulated boundaries (NaN) if  
        needed.  
         
        See:  
         
        Laplace's Equation in 2 and 3 Dimensions  
        Douglas Wilhelm Harder, University of Waterloo, Canada  
        https://ece.uwaterloo.ca/~ne217/Laboratories/05/5.LaplacesEquation.pptx  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_Laplace.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_Laplace", *args, **kwargs)
