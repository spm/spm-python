from spm._runtime import Runtime


def spm_bsd_reduce(*args, **kwargs):
    r"""
     SPM_BSD_REDUCE Prunes frequency components from BSD model and evaluates model evidence.  
          [BSDs, F, Rfq, dF] = spm_bsd_reduce(BSD) iteratively removes the least  
          significant frequency component from the BSD structure, fits the reduced  
          model, and computes the change in model evidence (log Bayes factor).  
         
          Inputs:  
              BSD  - Structure containing BSD model parameters and frequency components.  
         
          Outputs:  
              BSDs - Cell array of BSD structures after each pruning step.  
              F    - Array of model evidence values for each model.  
              Rfq  - Cell array of removed frequency labels.  
              dF   - Array of log Bayes factors for each pruning step.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/BSD/spm_bsd_reduce.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_bsd_reduce", *args, **kwargs)
