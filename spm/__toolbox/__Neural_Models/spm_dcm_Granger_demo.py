from spm.__wrapper__ import Runtime


def spm_dcm_Granger_demo(*args, **kwargs):
    """
      Demo routine for induced responses  
       ==========================================================================  
         
        This routine illustrates the relationship between Granger-Geweke    
        causality (GC) in frequency space and modulation transfer functions   
        (MTF).  We first compare and contrast analytic results for GC with   
        estimates based on a simulated time series. These synthetic data are   
        chosen to show that (analytic) GC can, in principle, detect sparsity   
        structure in terms of missing causal connections (however, GC estimates   
        are not so efficient). We then demonstrate the behaviour of (analytic)   
        GC by varying the strength of forward connections, backward connections   
        and intrinsic gain.  There is reasonable behaviour under these   
        manipulations. However, when we introduce realistic levels of (power law)   
        measurement noise, GC fails. The simulations conclude by showing that DCM   
        recovery of the underlying model parameters can furnish  (analytic) GC   
        among sources (in the absence of measurement noise). [delete the 'return'  
        below to see these simulations].  
          
        See also:  
         spm_ccf2csd.m, spm_ccf2mar, spm_csd2ccf.m, spm_csd2mar.m, spm_mar2csd.m,   
         spm_csd2coh.m, spm_ccf2gew, spm_dcm_mtf.m, spm_Q.m, spm_mar.m and   
         spm_mar_spectral.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Neural_Models/spm_dcm_Granger_demo.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_Granger_demo", *args, **kwargs, nargout=0)
