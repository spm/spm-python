from spm._runtime import Runtime


def DEM_COVID_COUNTRY(*args, **kwargs):
    r"""
      FORMAT DCM = DEM_COVID_COUNTRY(country)  
        country - country to model [default: 'United Kingdom')  
        T       - prediction period (days)  
         
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
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_COVID_COUNTRY.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_COVID_COUNTRY", *args, **kwargs)
