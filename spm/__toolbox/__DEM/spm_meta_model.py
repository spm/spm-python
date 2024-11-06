from spm.__wrapper__ import Runtime


def spm_meta_model(*args, **kwargs):
    """
      Meta-modelling of Bayes-optimal responses (Newton's method)  
        FORMAT DCM = spm_meta_model(DCM)  
         
        store estimates in DCM  
       --------------------------------------------------------------------------  
        DCM.M   - meta-model specification  
             M: [1 x m struct]   - hierarchical inference model (cf DEM.M)  
             G: [1 x s struct]   - generative process (for spm_ADEM or spm_ALAP)  
             U: [n x N double]   - n prior beliefs over N samples  
            pE: [1 x 1 struct]   - prior expectation of meta-model parameters  
            pC: [1 x 1 struct]   - prior variance of meta-model parameters  
         
        DCM.xY  - data structure  
             y: [N x p double]   - N samples of a p-variate response  
            X0: [N x q double]   - q-variate confounds  
            dt: [1 x 1 double]   - size of time bin for each sample  
             Q: {[N x N double]} - precision component[s]  
         
        DCM.xU  - input structure  
             u: [r x N double]   - r-variate input (hidden causes G in DEM)  
         
        Computes (and stores in DCM_MM_???)  
       --------------------------------------------------------------------------  
        DCM.DEM - Inference (with MAP parameters)  
        DCM.Ep  - conditional expectation  
        DCM.Cp  - conditional covariances  
        DCM.Eh  - conditional log-precision  
        DCM.Ey  - conditional response  
        DCM.F   - log-evidence  
         
        This routine illustrates Bayesian meta modelling - the Bayesian inversion  
        of a model of a Bayesian observer. This requires the specification of two  
        models: An inference model used by the subject (specified by a DEM  
        structure) and a meta-model (specified by a DCM structure). The inference  
        model is completed by a response model to furnish the meta-model; where  
        the response model takes the output of the (active) inference scheme  
        specified by the DEM and generates an observed (behavioural or  
        neurophysiological) response. Crucially either the inference model or  
        the response model or both can have free parameters - that are optimised  
        using Bayesian nonlinear system identification in the usual way.  
         
        Although this routine is a function, it is expected that people will fill  
        in the model-specific parts in a local copy, before running it.  The  
        current example uses a model of slow pursuit and generates synthetic data  
        (responses) to illustrate how it works. To replace these simulated data  
        with real data, simply specify the DCM.xY (and xU fields) with  
        empirical values. If other fields do not exist, exemplar fields will be filled in.  
         
        The conditional density of the parameters and F values (log-evidence) can  
        be used in the usual way for inference on parameters or Bayesian model  
        comparison (as for other DCMs)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_meta_model.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_meta_model", *args, **kwargs)
