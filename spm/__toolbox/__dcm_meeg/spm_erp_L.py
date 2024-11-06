from spm.__wrapper__ import Runtime


def spm_erp_L(*args, **kwargs):
    """
      [projected] lead field L as a function of position and moments  
        FORMAT [L] = spm_erp_L(P,dipfit)  
        P       - model parameters  
        dipfit  - spatial model specification  
        L       - lead field  
       __________________________________________________________________________  
         
        The lead field (L) is constructed using the specific parameters in P and,  
        where necessary information in the dipole structure dipfit. For ECD  
        models P.Lpos and P.L encode the position and moments of the ECD. The  
        field dipfit.type:  
         
           'ECD', 'LFP' or 'IMG'  
         
        determines whether the model is ECD or not. For imaging reconstructions  
        the paramters P.L are a (m x n) matrix of coefficients that scale the  
        contrition of n sources to m = dipfit.Nm modes encoded in dipfit.G.  
         
        For LFP models (the default) P.L simply encodes the electrode gain for   
        each source contributing a LFP.  
         
        see; Kiebel et al. (2006) NeuroImage  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_erp_L.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_erp_L", *args, **kwargs)
