from spm.__wrapper__ import Runtime


def spm_DEM_M_set(*args, **kwargs):
    """
      Set indices and performs checks on hierarchical models  
        FORMAT [M] = spm_DEM_M_set(M)  
         
        for each level (i); required fields  
         
          M(i).g  = y(t)  = g(x,v,P)    {inline function, string or m-file}  
          M(i).f  = dx/dt = f(x,v,P)    {inline function, string or m-file}  
         
        and  
         
          M(i).m  = number of inputs v(i + 1);  
          M(i).n  = number of states x(i);  
          M(i).l  = number of output v(i);  
         
        or  
         
          M(i).x  = hidden states;  
          M(i).v  = causal states;  
         
        for each level (i); optional fields  
         
          M(i).pE = prior expectation of p model-parameters  
          M(i).pC = prior covariances of p model-parameters  
          M(i).hE = prior expectation of h log-precision (cause noise)  
          M(i).hC = prior covariances of h log-precision (cause noise)  
          M(i).gE = prior expectation of g log-precision (state noise)  
          M(i).gC = prior covariances of g log-precision (state noise)  
          M(i).xC = prior covariances of states  
          M(i).Q  = precision components (input noise)  
          M(i).R  = precision components (state noise)  
          M(i).V  = fixed precision (input noise)  
          M(i).W  = fixed precision (state noise)  
         
         
        sets fields, checks internal consistency of model specification and sets  
        estimation parameters.  If a single hyperparameter is supplied i.i.d  
        components are assumed (i.e., Q = I, R = I)  
       --------------------------------------------------------------------------  
         
          M(1).E.s;     = smoothness (s.d. in time bins)  
          M(1).E.d;     = embedding order q(v)  (i.e., number of derivatives)  
          M(1).E.n;     = embedding order q(x)  
         
        If the highest level involves any dynamic or static transformation  
        of its inputs a further level is added with flat priors  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_DEM_M_set.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_DEM_M_set", *args, **kwargs)
