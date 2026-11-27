from spm._runtime import Runtime


def _leadfield_duneuro(*args, **kwargs):
    r"""
      LEADFIELD_DUNEURO computes EEG/MEG leadfields for a set of given dipoles  
        using the finite element method (FEM), implemented in the duneuro  
        software  
         
        [lf] = leadfield_duneuro(pos, headmodel, sens, method);  
         
        with input arguments  
          pos     a matrix of dipole positions  
                  (there can be 'deep electrodes', too)  
          headmodel contains a FE volume conductor (output of ft_prepare_vol_sens)  
          sens    contains a sensor array description (output of ft_prepare_vol_sens)  
          method  string defining the modality ('eeg' or 'meg)  
        The output lf is the leadfield matrix of dimensions m (rows) x n*3 (columns)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/forward/private/leadfield_duneuro.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("leadfield_duneuro", *args, **kwargs)
