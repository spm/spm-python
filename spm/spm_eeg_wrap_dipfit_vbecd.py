from spm.__wrapper__ import Runtime


def spm_eeg_wrap_dipfit_vbecd(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_wrap_dipfit_vbecd.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_wrap_dipfit_vbecd", *args, **kwargs)
