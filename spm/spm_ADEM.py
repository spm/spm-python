from spm.__wrapper__ import Runtime


def spm_ADEM(*args, **kwargs):
    """
      Dynamic expectation maximisation:  Active inversion  
        FORMAT DEM = spm_ADEM(DEM)  
         
        DEM.G  - generative process  
        DEM.M  - recognition  model  
        DEM.C  - causes  
        DEM.U  - prior expectation of causes  
       __________________________________________________________________________  
         
        This implementation of DEM is the same as spm_DEM but integrates both the  
        generative process and model inversion in parallel. Its functionality is   
        exactly the same apart from the fact that confounds are not accommodated  
        explicitly.  The generative model is specified by DEM.G and the veridical  
        causes by DEM.C; these may or may not be used as priors on the causes for  
        the inversion model DEM.M (i.e., DEM.U = DEM.C).  Clearly, DEM.G does not  
        require any priors or precision components; it will use the values of the  
        parameters specified in the prior expectation fields.  
         
        This routine is not used for model inversion per se but to simulate the  
        dynamical inversion of models.  Critically, it includes action   
        variables a - that couple the model back to the generative process   
        This enables active inference (c.f., action-perception) or embodied   
        inference.  
         
        hierarchical models M(i)  
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
          M(i).xP = precision (states)  
         
          M(i).m  = number of inputs v(i + 1);  
          M(i).n  = number of states x(i)  
          M(i).l  = number of output v(i)  
          M(i).k  = number of action a(i)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_ADEM.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_ADEM", *args, **kwargs)
