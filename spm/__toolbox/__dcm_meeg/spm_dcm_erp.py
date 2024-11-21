from spm.__wrapper__ import Runtime


def spm_dcm_erp(*args, **kwargs):
    """
      Estimate parameters of a DCM model (Variational Lapalce)  
        FORMAT [DCM,dipfit] = spm_dcm_erp(DCM)  
         
        DCM  
           name: name string  
              Lpos:  Source locations  
              xY:    data   [1x1 struct]  
              xU:    design [1x1 struct]  
         
          Sname: cell of source name strings  
              A: {[nr x nr double]  [nr x nr double]  [nr x nr double]}  
              B: {[nr x nr double], ...}   Connection constraints  
              C: [nr x 1 double]  
         
          options.trials       - indices of trials  
          options.Tdcm         - [start end] time window in ms  
          options.D            - time bin decimation       (usually 1 or 2)  
          options.h            - number of DCT drift terms (usually 1 or 2)  
          options.Nmodes       - number of spatial models to invert  
          options.analysis     - 'ERP', 'SSR' or 'IND'  
          options.model        - 'ERP', 'SEP', 'CMC', 'CMM', 'NMM' or 'MFM'  
          options.spatial      - 'ECD', 'LFP' or 'IMG'  
          options.onset        - stimulus onset (ms)  
          options.dur          - and dispersion (sd)  
          options.CVA          - use CVA for spatial modes [default = 0]  
          options.Nmax         - maxiumum number of iterations [default = 64]  
         
        dipfit - Dipole structure (for electromagnetic forward model)  
               See spm_dcm_erp_dipfit:  this field is removed from DCM.M to save  
               memory - and is offered as an output argument if needed  
         
        The scheme can be initialised with parameters for the neuronal model  
        and spatial (observer) model by specifying the fields DCM.P and DCM.Q,   
        respectively. If previous priors (DCM.M.pE and pC or DCM.M.gE and gC or   
        DCM.M.hE and hC) are specified, they will be used. Explicit priors can be  
        useful for Bayesian parameter averaging - but would not normally be  
        called upon - because prior constraints are specified by DCM.A, DCM.B,...  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_dcm_erp.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_erp", *args, **kwargs)
