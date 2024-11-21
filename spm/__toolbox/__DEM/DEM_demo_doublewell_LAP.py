from spm.__wrapper__ import Runtime


def DEM_demo_doublewell_LAP(*args, **kwargs):
    """
      The double-well revisited:  
       __________________________________________________________________________  
        This demonstration compares generalised filtering and a state-of-the-art   
        Bayesian smoother (SCKS) in the context of a double-well system. Here the  
        Cubature filtering outperforms generalised schemes that are confounded by   
        the failure of the Laplace assumption. Note that generalised filtering  
        and DEM give the same conditional estimates of states because there are   
        no free parameters or hyperparameters and the mean-field assumption   
        implcit in DEM is irrelevant.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_doublewell_LAP.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_doublewell_LAP", *args, **kwargs, nargout=0)
