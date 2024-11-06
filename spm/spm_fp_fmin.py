from spm.__wrapper__ import Runtime


def spm_fp_fmin(*args, **kwargs):
    """
      Optimise the parameters with respect to an equilibrium density  
        FORMAT [P] = spm_fp_fmin(M)  
         
        M   - model structure with desired density specified by M(1).fq and  
              support specified by M(1).X = spm_ndgrid(x)  
         
        P   - optimised parameters  
         
       --------------------------------------------------------------------------  
        This routine uses EM (spm_nlsi_NG) and the Fokker Planck formulation to  
        minimise the difference between the flow and dispersion terms induced by  
        the free parameters of the flow (M(1),f).  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_fp_fmin.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_fp_fmin", *args, **kwargs)
