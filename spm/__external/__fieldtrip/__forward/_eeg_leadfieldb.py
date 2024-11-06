from spm.__wrapper__ import Runtime


def _eeg_leadfieldb(*args, **kwargs):
    """
      EEG_LEADFIELDB computes the electric leadfield for a dipole in a volume  
        using the boundary element method  
         
        Use as  
          [lf] = eeg_leadfieldb(dippos, elc, vol)  
        with the input arguments  
          dippos     = position dipole, 1x3 or Nx3  
          elc        = electrode positions, Nx3 (optional, can be empty)  
          vol        = volume conductor model  
         
        The volume conductor model is a structure and should have the fields  
          vol.bnd    = structure array with vertices and triangles of each boundary  
          vol.cond   = conductivity for each compartment  
          vol.mat    = system matrix, which can include the electrode interpolation  
         
        The compartment boundaries are described by a structure array with  
          vol.bnd(i).pos  
          vol.bnd(i).pos  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/eeg_leadfieldb.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("eeg_leadfieldb", *args, **kwargs)
