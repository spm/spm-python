from spm.__wrapper__ import Runtime


def DEM_COVID_UK4(*args, **kwargs):
    """
      FORMAT DCM = DEM_COVID_UK4  
         
        Demonstration of COVID-19 modelling using variational Laplace (4 groups)  
       __________________________________________________________________________  
        This routine illustrates the dynamic causal modelling of the epidemic in  
        the United Kingdom using four age groups that are coupled via (prevalence  
        -dependent) contact rates. It is the routine used to prepare the graphics  
        and report for the DCM COVID dashboard.  
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_COVID_UK4.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_COVID_UK4", *args, **kwargs)
