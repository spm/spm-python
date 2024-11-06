from spm.__wrapper__ import Runtime


def DEM_SARS_I(*args, **kwargs):
    """
      FORMAT DEM_COVID_I  
        data    - data    to model [default: data = DATA_COVID_JHU]  
        country - country to model [default: 'United Kingdom')  
         
        Demonstration of COVID-19 modelling using variational Laplace  
       __________________________________________________________________________  
         
        This routine illustrates Bayesian model comparison using a line search  
        over periods of imunity and pooling over countries. In brief,32 countries  
        are inverted and 16 with the most informative posterior over the period  
        of immunity are retained for Bayesian parameter averaging. The Christian  
        predictive densities are then provided in various formats for the average  
        country and (16) individual countries.  
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_SARS_I.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_COVID_I", *args, **kwargs, nargout=0)
