from spm.__wrapper__ import Runtime


def DEM_COVID_UTLA(*args, **kwargs):
    """
      FORMAT [DCM] = DEM_COVID_UTLA  
         
        Demonstration of COVID-19 modelling with stratified populations  
       __________________________________________________________________________  
         
        This demonstration routine fixed multiple regional death by date and new  
        cases data and compiles estimates of latent states for local  
        authorities served by an NHS trust provider.  
         
        Technical details about the dynamic causal model used here can be found  
        at https://www.fil.ion.ucl.ac.uk/spm/covid-19/.  
         
        The (annotated) open source code creating these graphics is  
        DEM_COVID_DASH.m  
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_COVID_UTLA.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_COVID_UTLA", *args, **kwargs)
