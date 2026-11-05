from spm._runtime import Runtime


def spm_eeg_wrap_dipfit_vbecd(*args, **kwargs):
    r"""
      A cost function/wrapper to sit between non-linear optimisation spm_nlsi_gn.m  
        and dipole fit routine spm__eeg_inv_vbecd.m  
        sens and vol structures should be passed in M, where  
          sens=M.Setup.forward.sens;  
          vol=M.Setup.forward.vol;  
        P contains a list of the free parameters (assuming all position  
          parameters come first (in triplets) followed by all moment paameters  
          (also in triplets)  
        U is unused  
        At the momnent reduces the rank of the MEG leadfield 2 dimensions.  
        leads are the lead fields of the dipoles fit  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_wrap_dipfit_vbecd.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_wrap_dipfit_vbecd", *args, **kwargs)
