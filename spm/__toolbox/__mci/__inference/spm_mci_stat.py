from spm.__wrapper__ import Runtime


def spm_mci_stat(*args, **kwargs):
    """
      Test MCMC samples for stationarity  
        FORMAT [pstat,mu,nse,batch] = spm_mci_stat (post,nbatch,method)  
         
        post      posterior distribution  
        nbatch    number of batches (last batch contains last half of samples)  
        method    'geweke', 'ar1' (default) or 'geyer'  
         
        pstat     p-value for batch mean being different to final batch mean  
        mu        batch mean (of energy)  
        nse       batch numeric standard error (of energy)  
        batch     (n).ind, (n).N indices and number of samples in nth batch  
         
        This routine is based on Geweke 1992. But we also allow estimates   
        of the Numeric Standard Error (NSE) to be estimated using an AR1 model   
        or Geyer's method  
          
        J. Geweke (1992) Evaluating the accuracy of sampling-base approaches to   
        the calculation of posterior moments. Bayesian Statistics 4, OUP.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_stat.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mci_stat", *args, **kwargs)
