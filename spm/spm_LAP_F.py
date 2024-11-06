from spm.__wrapper__ import Runtime


def spm_LAP_F(*args, **kwargs):
    """
      Return the Gibbs energy (L) as a function of contitional means  
        FORMAT [L] = spm_LAP_F(q,qu,qp,qh,pu,pp,ph,M)  
         
            q.x: {nx1 cell}  
            q.v: {dx1 cell}  
            q.p: {mx1 cell}  
            q.h: {mx1 cell}  
            q.g: {mx1 cell}  
         
        for an m-level hierarchy  
        See spm_LAP  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_LAP_F.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_LAP_F", *args, **kwargs)
