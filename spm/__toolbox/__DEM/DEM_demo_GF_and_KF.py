from spm.__wrapper__ import Runtime


def DEM_demo_GF_and_KF(*args, **kwargs):
    """
      A demonstration of generalised and Kalman filtering where the number  
        of hidden states exceeds the number of variables observed. The metrics of  
        performance are the mean sum of squared error and the SSE normalized by  
        the posterior precision (NESS). The results of a single time series  
        analysis are shown first and then the simulations are repeated under  
        linear and nonlinear observation models to compare the relative  
        performance of DEM and EKF. The superiority of DEM (generalised filtering)  
        over Kalman filtering rests on the optimisation of K - the rate of  
        generalised descent on free energy (see code after 'return').  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_GF_and_KF.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_GF_and_KF", *args, **kwargs, nargout=0)
