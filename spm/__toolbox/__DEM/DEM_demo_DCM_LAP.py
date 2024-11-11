from spm.__wrapper__ import Runtime


def DEM_demo_DCM_LAP(*args, **kwargs):
    """
      Demo applying the Laplace scheme to DCM with hidden states  
       __________________________________________________________________________  
        This routine demonstrates Generalized filtering for a DCM (Dynamic Causal  
        Model) of fMRI responses using simulated data. This is an endogenous   
        DCM in that there are no exogenous inputs. The demonstration specifies   
        and inverts a full connectivity model and then illustrates post-hoc model  
        optimization to recover (discover) the true architecture. It concludes   
        with an automatic model optimization in terms of the prior variances over  
        coupling parameters.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_DCM_LAP.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_DCM_LAP", *args, **kwargs, nargout=0)
