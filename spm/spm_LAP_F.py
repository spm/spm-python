from spm._runtime import Runtime


def spm_LAP_F(*args, **kwargs):
    r"""
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
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_LAP_F.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_LAP_F", *args, **kwargs)
