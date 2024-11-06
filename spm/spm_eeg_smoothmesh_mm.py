from spm.__wrapper__ import Runtime


def spm_eeg_smoothmesh_mm(*args, **kwargs):
    """
      Compute smoothing kernel for triangle mesh in mm  
        FORMAT [allsmoothnames] = spm_eeg_smoothmesh_mm(meshname,allfwhm,redo)  
         
        smoothing kernel: each colum QG(:,j)  
        if redo==1 and file already exists then redo  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_smoothmesh_mm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_smoothmesh_mm", *args, **kwargs)
