from spm.__wrapper__ import Runtime


def spm_get_matdim(*args, **kwargs):
    """
      Voxel-to-world matrix and image dimensions from image or bbox and vox-dim  
         
        FORMAT [mat, dim] = spm_get_matdim(img, vx, bb)  
         
        img - filename of image to use as reference (defaults to SPM's TPM.nii)  
        vx  - [1 x 3] vector of voxel dimensions (mm).  
        bb  - [2 x 3] array of the min and max X, Y, and Z coordinates (mm),  
              i.e. bb = [minX minY minZ; maxX maxY maxZ].  
         
        mat - [4 x 4] matrix mapping voxel coordinates to world (mm) coordinates  
        dim - [1 x 3] vector of image dimensions (number of voxels)  
              (both as in output from spm_vol)  
         
              Note that the output mat will correspond to the same orientation  
              as SPM's canonical templates (transverse and vx(1) forced negative)  
              if either or both bb and vx are specified (finite), but otherwise  
              will keep the orientation of the reference image.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_get_matdim.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_get_matdim", *args, **kwargs)
