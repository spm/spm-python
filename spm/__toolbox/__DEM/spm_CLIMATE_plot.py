from spm.__wrapper__ import Runtime


def spm_CLIMATE_plot(*args, **kwargs):
    """
      Graphics for climate simulations  
        FORMAT spm_CLIMATE_plot(Y,X,U,T,A)  
        Y      - expected timeseries  
        X      - latent states  
        U      - indices of outcome  
        T      - dates (date numbers)  
        A      - data structure  
         
        This auxiliary routine plots the trajectory of outcome variables and  
        underlying latent or hidden states. The top panel corresponds to the  
        posterior predicted expectation of the requested outcome while the  
        subsequent panels show the (posterior expectations of) latent states over  
        time, in groups of three. If a data structure is supplied, the  
        appropriate empirical data will be superimposed over the predicted  
        outcomes.  
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_CLIMATE_plot.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_CLIMATE_plot", *args, **kwargs, nargout=0)
