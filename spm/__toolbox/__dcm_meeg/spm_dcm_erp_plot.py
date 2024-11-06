from spm.__wrapper__ import Runtime


def spm_dcm_erp_plot(*args, **kwargs):
    """
      Plot predicted source activity  
        FORMAT x = spm_dcm_erp_plot(DCM)  
         
        DCM - DCM structure:  
        store estimates in DCM  
       --------------------------------------------------------------------------  
        DCM.M  - model specification  
        DCM.xY - data structure  
        DCM.xU - input structure  
        DCM.Ep - conditional expectation f(x,u,p)  
        DCM.Cp - conditional covariances G(g)  
        DCM.Eg - conditional expectation  
        DCM.Cg - conditional covariances  
        DCM.Pp - conditional probability  
        DCM.H  - conditional responses (y), projected space  
        DCM.K  - conditional responses (x)  
        DCM.R  - conditional residuals (y)  
        DCM.F  - Laplace log evidence  
        DCM.L  - Laplace log evidence components  
        DCM.ID - data ID  
          
          
        DCM.options.h  
        DCM.options.Nmodes  
        DCM.options.onset  
        DCM.options.model  
        DCM.options.lock  
        DCM.options.symm  
         
        x{i}   - source activity contributing sources {trial i}  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_dcm_erp_plot.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_erp_plot", *args, **kwargs)
