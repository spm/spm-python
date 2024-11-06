from spm.__wrapper__ import Runtime


def spm_eeg_displayECD(*args, **kwargs):
    """
      Plot dipole positions onto the SPM canonical mesh  
        FORMAT [out] = spm_eeg_displayECD(Pos,Orient,Var,Names,options)  
         
        IN (admissible choices):  
          - Pos: a 3xndip matrix containing the positions of the dipoles in  
          the canonical frame of reference  
          - Orient: the same with dipole orientations  
          - Var: the same with position variance  
          - Names: the same with dipole names  
          - options: an optional structure containing  
              .hfig: the handle of the display figure  
              .tag: the tag to be associated with the created UI objects  
              .add: binary variable ({0}, 1: just add dipole in the figure .hfig)  
         
        OUT:  
          - out: a structure containing the handles of the object in the figure  
          (including the mesh, the dipoles, the transparency slider, etc...)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_displayECD.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_displayECD", *args, **kwargs)
