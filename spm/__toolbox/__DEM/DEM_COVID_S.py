from spm.__wrap__ import _Runtime


def DEM_COVID_S(*args, **kwargs):
  """  FORMAT [DCM] = DEM_COVID_S  
     
    Demonstration of COVID-19 modelling with stratified populations  
   __________________________________________________________________________  
     
    This demonstration routine uses a stratified population by age to fit  
    death by date according to age bins. In brief, this uses the same kind of  
    DCM for each age group; and the accompanying population densities  
    are coupled via contact matrices; in other words, the number of people  
    from another group I expect to be in contact with perday. In addition,  
    some of the clinical and epidemiological parameters are group specific  
    using prespecified profiles encoded in R. the parameters of the contact  
    matrices are optimised and a reasonably uninformative priors.  
     
    Technical details about the dynamic causal model used here can be found  
    at https://www.fil.ion.ucl.ac.uk/spm/covid-19/.  
     
    The (annotated) open source code creating these graphics is  
    DEM_COVID_DASH.m  
   __________________________________________________________________________  
    Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_COVID_S.m)
  """

  return _Runtime.call("DEM_COVID_S", *args, **kwargs)
