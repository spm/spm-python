from spm.__wrapper__ import Runtime


def spm_dcm_erp_dipfit(*args, **kwargs):
    """
      Prepare structures for ECD forward model (EEG, MEG and LFP)  
        FORMAT DCM = spm_dcm_erp_dipfit(DCM, save_vol_sens)  
        DCM           - DCM structure  
        save_vol_sens - optional argument indicating whether to perform  
                        the time consuming step required for actually using  
                        the forward model to compute lead fields (1, default)  
                        or skip it if the function is only called for  
                        verification of the input (0).  
         
        Input DCM structure requires:  
              DCM.xY.Dfile  
              DCM.xY.Ic  
              DCM.Lpos  
              DCM.options.spatial - 'ERP', 'LFP' or 'IMG'  
         
        fills in:  
         
              DCM.M.dipfit  
         
           dipfit.location - 0 or 1 for source location priors  
           dipfit.symmetry - 0 or 1 for symmetry constraints on sources  
           dipfit.modality - 'EEG', 'MEG', 'MEGPLANAR' or 'LFP'  
           dipfit.type     - 'ECD', 'LFP' or 'IMG''  
           dipfit.symm     - distance (mm) for symmetry constraints (ECD)  
           dipfit.Lpos     - x,y,z source positions (mm)            (ECD)  
           dipfit.Nm       - number of modes                        (Imaging)  
           dipfit.Ns       - number of sources  
           dipfit.Nc       - number of channels  
         
           dipfit.vol      - volume structure (for M/EEG)  
           dipfit.datareg  - registration structure (for M/EEG)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_dcm_erp_dipfit.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_erp_dipfit", *args, **kwargs)
