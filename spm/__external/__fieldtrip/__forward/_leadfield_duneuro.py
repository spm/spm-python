from spm.__wrapper__ import Runtime


def _leadfield_duneuro(*args, **kwargs):
    """
      LEADFIELD_DUNEURO computes EEG/MEG leadfields for a set of given dipoles  
        using the finite element method (FEM)  
         
        [lf] = leadfield_duneuro(pos, vol);  
         
        with input arguments  
          pos     a matrix of dipole positions  
                  (there can be 'deep electrodes', too)  
          vol     contains a FE volume conductor (output of ft_prepare_vol_sens)  
          method  string defining the modality ('eeg' or 'meg)  
        The output lf is the leadfield matrix of dimensions m (rows) x n*3 (columns)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/leadfield_duneuro.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("leadfield_duneuro", *args, **kwargs)
