from spm.__wrapper__ import Runtime


def spm_DEM_M(*args, **kwargs):
    """
      Create a [template] model structure  
        FORMAT [M] = spm_DEM_M(model,l,n)  
        FORMAT [M] = spm_DEM_M(model,X1,X2,...)  
         
        model: 'General linear model','GLM'  
               'Factor analysis','FA'  
               'Independent component analysis','ICA'  
               'Sparse coding',"SC'  
               'convolution model'  
               'State space model','SSM',','Double Well'  
               'Lorenz'  
               'Ornstein_Uhlenbeck','OU'  
         
        l(i) - number of outputs from level i  
        n(i) - number of hidden states in level i  
         
        Xi   - deisgn matrix for level i  
         
       ==========================================================================  
        hierarchical generative model  
       --------------------------------------------------------------------------  
          M(i).g  = y(t)  = g(x,v,P)    {inline function, string or m-file}  
          M(i).f  = dx/dt = f(x,v,P)    {inline function, string or m-file}  
         
          M(i).pE = prior expectation of p model-parameters  
          M(i).pC = prior covariances of p model-parameters  
          M(i).hE = prior expectation of h hyper-parameters (cause noise)  
          M(i).hC = prior covariances of h hyper-parameters (cause noise)  
          M(i).gE = prior expectation of g hyper-parameters (state noise)  
          M(i).gC = prior covariances of g hyper-parameters (state noise)  
          M(i).Q  = precision components (input noise)  
          M(i).R  = precision components (state noise)  
          M(i).V  = fixed precision (input noise)  
          M(i).W  = fixed precision (state noise)  
         
          M(i).m  = number of inputs v(i + 1);  
          M(i).n  = number of states x(i);  
          M(i).l  = number of output v(i);  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_DEM_M.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_DEM_M", *args, **kwargs)
