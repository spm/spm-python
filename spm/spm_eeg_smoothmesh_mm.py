from spm._runtime import Runtime


def spm_eeg_smoothmesh_mm(*args, **kwargs):
    r"""
      Compute smoothing kernel for triangle mesh in mm  
        FORMAT [allsmoothnames] = spm_eeg_smoothmesh_mm(meshname,allfwhm,redo)  
         
        smoothing kernel: each colum QG(:,j)  
        if redo==1 and file already exists then redo  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_smoothmesh_mm.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_smoothmesh_mm", *args, **kwargs)
