from spm._runtime import Runtime


def spm_run_dcm_bms(*args, **kwargs):
    """
      Compare DCMs on the basis of their log-evidences  
        Four methods are available to identify the best among alternative models:  
         
         (1) single subject BMS using Bayes factors  
             (see Penny et al, NeuroImage, 2004)  
         (2) fixed effects group BMS using group Bayes factors  
             (see Stephan et al, NeuroImage, 2007)  
         (3) random effects group BMS using exceedance probabilities  
             (see Stephan et al, NeuroImage, 2009)  
         (4) comparing model families  
             (see Penny et al, PLOS-CB, 2010)  
         
        Note: All functions use the negative free energy (F) as an approximation  
        to the log model evidence.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_run_dcm_bms.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_run_dcm_bms", *args, **kwargs)
