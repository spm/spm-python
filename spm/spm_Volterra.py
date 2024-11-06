from spm.__wrapper__ import Runtime


def spm_Volterra(*args, **kwargs):
    """
      Generalized convolution of inputs (U) with basis set (bf)  
        FORMAT [X,Xname,Fc] = spm_Volterra(U,bf,V)  
        U          -  input structure array (see spm_get_ons.m)  
        bf         -  Basis functions (see spm_get_bf.m)  
        V          -  [1 or 2] order of Volterra expansion [default = 1]  
         
        X          -  Design Matrix  
        Xname      -  names of regressors [columns] in X  
        Fc(i).i    -  indices pertaining to input i (and interactions)  
        Fc(i).name -  names pertaining to input i   (and interactions)  
        Fc(i).p    -  grouping of regressors per parameter  
       __________________________________________________________________________  
         
        For first order expansions spm_Volterra simply convolves the causes (e.g.  
        stick functions) in U.u by the basis functions in bf to create a design  
        matrix X.  For second order expansions new entries appear in X, Xname and  
        Fc that correspond to the interaction among the original causes. The  
        basis functions for these effects are two dimensional and are used to  
        assemble the second order kernel in spm_graph.m. Second order effects are  
        computed for only the first column of U.u.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_Volterra.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_Volterra", *args, **kwargs)
