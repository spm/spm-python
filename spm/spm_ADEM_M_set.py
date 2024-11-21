from spm.__wrapper__ import Runtime


def spm_ADEM_M_set(*args, **kwargs):
    """
      Set indices and perform checks on hierarchical action models  
        FORMAT M = spm_ADEM_M_set(M)  
         
        for each level (i); required fields  
         
          M(i).g  = y(t)  = g(x,v,a,P)    {inline function, string or m-file}  
          M(i).f  = dx/dt = f(x,v,a,P)    {inline function, string or m-file}  
         
        and  
         
          M(i).m  = number of inputs v(i + 1);  
          M(i).n  = number of states x(i);  
          M(i).l  = number of output v(i);  
          M(i).k  = number of action a(i);  
         
        or  
         
          M(i).x  = hidden states;  
          M(i).v  = causal states;  
          M(i).a  = action states;  
         
        for each level (i); optional fields  
         
          M(i).pE = prior expectation of p model-parameters  
          M(i).V  = precision (input noise)  
          M(i).W  = precision (state noise)  
          M(i).U  = precision (action)  
         
         
        sets fields, checks internal consistency of model specification and sets  
        estimation parameters.  If (V,W) are not specified infinite precision is  
        assumed.  
       --------------------------------------------------------------------------  
         
          M(1).E.s;     = smoothness (s.d. in time bins)  
          M(1).E.d;     = embedding order q(v)  (i.e., number of derivatives)  
          M(1).E.n;     = embedding order q(x)  
         
        If the highest level involves any dynamic or static transformation  
        of its inputs a further level is added with flat priors  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_ADEM_M_set.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_ADEM_M_set", *args, **kwargs)
