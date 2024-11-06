from spm.__wrapper__ import Runtime


def spm_dcm_bma(*args, **kwargs):
    """
      Model-independent samples from DCM posterior  
        FORMAT BMA = spm_dcm_bma(DCM)  
        FORMAT bma = spm_dcm_bma(post,post_indx,subj,Nsamp,oddsr)  
         
        DCM   - {subjects x models} cell array of DCMs over which to average  
        ---------------------------------------------------------------------  
            DCM{i,j}.Ep - posterior expectation  
            DCM{i,j}.Cp - posterior covariances  
            DCM{i,j}.F  - free energy  
         
        BMA   - Baysian model average structure  
        ---------------------------------------------------------------------  
            BMA.Ep      - BMA posterior mean  
            BMA.Cp      - BMA posterior VARIANCE  
            BMA.F       - Accumulated free energy over subjects;  
            BMA.P       - Posterior model probability over subjects;  
         
            BMA.SUB.Ep  - subject specific BMA posterior mean  
            BMA.SUB.Sp  - subject specific BMA posterior variance  
            BMA.nsamp   - Number of samples  
            BMA.Nocc    - number of models in Occam's window  
            BMA.Mocc    - index of models in Occam's window  
         
        If DCM is an array, Bayesian model averaging will be applied over   
        subjects (i.e., over columns) using FFX Baysian parameter averaging  
         
       --------------------------------------------------------------------------  
        OR  
       --------------------------------------------------------------------------  
         
        post      [Ni x M] vector of posterior model probabilities  
                  If Ni > 1 then inference is based on subject-specific RFX posterior  
        post_indx models to use in BMA (position of models in subj structure)  
        subj      subj(n).sess(s).model(m).fname: DCM filename  
        Nsamp     Number of samples (default = 1e4)  
        oddsr     posterior odds ratio for defining Occam's window (default=0, ie  
                  all models used in average)  
         
        bma       Returned data structure contains  
         
                  .nsamp  Number of samples  
                  .oddsr  odds ratio  
                  .Nocc   number of models in Occam's window  
                  .Mocc   index of models in Occam's window  
                  .indx   subject specific indices of models in Occam's window  
         
                  For `Subject Parameter Averaging (SPA)':  
         
                  .mEp    posterior mean   
                  .sEp    posterior SD             
                  .mEps   subject specific posterior mean   
                  .sEps   subject specific posterior SD  
         
                  use the above values in t-tests, ANOVAs to look for significant  
                  effects in the group  
         
                  For `Group Parameter Averaging (GPA)':  
         
                  The following structures contain samples of the DCM A,B,C and D  
                  matrices from the group posterior density. See pages 6 and 7 of [1]  
         
                  .a [dima x Nsamp]   
                  .b [dima x Nsamp]   
                  .c [dima x Nsamp]   
                  .d [dima x Nsamp]   
                                
                  Use these to make inferences using the group posterior density approach.   
                  Essentially, for each parameter, GPA gets a sample which is the average   
                  over subjects. The collection of samples then constitutes a distribution of  
                  the group mean from which inferences can be made directly. This is to  
                  be contrasted with SPA where, for each subject, we average over  
                  samples to get a mean for that subject. Group level inferences  
                  are then made using classical inference. SPA is the standard  
                  approach.  
         
         
                  For RFX BMA, different subject can have different models in  
                  Occam's window (and different numbers of models in Occam's  
                  window)  
         
        This routine implements Bayesian averaging over models and subjects  
         
        See [1] W Penny, K Stephan, J. Daunizeau, M. Rosa, K. Friston, T. Schofield   
        and A Leff. Comparing Families of Dynamic Causal Models.   
        PLoS Computational Biology, Mar 2010, 6(3), e1000709.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_bma.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_bma", *args, **kwargs)
