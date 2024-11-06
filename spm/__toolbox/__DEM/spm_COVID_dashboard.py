from spm.__wrapper__ import Runtime


def spm_COVID_dashboard(*args, **kwargs):
    """
      Dashboard for coronavirus simulations  
        FORMAT spm_COVID_plot(Y,X,Z)  
        DCM.Ep  
        DCM.M  
        DCM.data  
         
        This auxiliary routine plots the predicted prevalence of infection, the  
        production rate and social distancing as a predicted timeline with  
        annotated dates and statistics.  
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_COVID_dashboard.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_COVID_dashboard", *args, **kwargs, nargout=0)
