from spm.__wrapper__ import Runtime


def DEM_path_integrals(*args, **kwargs):
    """
     --------------------------------------------------------------------------  
        Illustration of approximations to path integrals. This routine generates  
        a path from dynamics whose Fokker Planck solution corresponds to a  
        Gaussian with a given (diagonal) precision. It then samples random  
        segments (after scaling and smoothing) and evaluates their action. This  
        evaluation is in terms of the sum of squares residuals between realised  
        and predicted flow and path dependent and path-independent terms based  
        upon the surprisal associated with the solution of the Fokker Planck  
        equation. The point being made here is that the terms based upon the  
        surprisal (cyan dots) upper bound the action (blue dots).  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_path_integrals.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_path_integrals", *args, **kwargs, nargout=0)
