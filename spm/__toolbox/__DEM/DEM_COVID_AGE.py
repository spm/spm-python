from spm.__wrapper__ import Runtime


def DEM_COVID_AGE(*args, **kwargs):
    """
      FORMAT [DCM] = DEM_COVID_AGE  
        LA - local authority  
         
        Demonstration of COVID-19 modelling  
       __________________________________________________________________________  
         
        This demonstration routine fits multiple regional death by date and new  
        cases data and compiles estimates of latent states for local  
        authorities.  
         
        Technical details about the dynamic causal model used here can be found  
        at https://www.fil.ion.ucl.ac.uk/spm/covid-19/.  
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_COVID_AGE.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_COVID_AGE", *args, **kwargs)
