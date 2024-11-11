from spm.__wrapper__ import Runtime


def spm_vol(*args, **kwargs):
    """
      Get header information for images  
        FORMAT V = spm_vol(P)  
        P - a char or cell array of filenames  
        V - a structure array containing image volume information  
            The elements of the structures are:  
              V.fname - the filename of the image.  
              V.dim   - the x, y and z dimensions of the volume  
              V.dt    - A 1x2 array.  First element is datatype (see spm_type).  
                        The second is 1 or 0 depending on the endian-ness.  
              V.mat   - a 4x4 affine transformation matrix mapping from  
                        voxel coordinates to real world coordinates.  
              V.pinfo - plane info for each plane of the volume.  
                     V.pinfo(1,:) - scale for each plane  
                     V.pinfo(2,:) - offset for each plane  
                        The true voxel intensities of the jth image are given  
                        by: val*V.pinfo(1,j) + V.pinfo(2,j)  
                     V.pinfo(3,:) - offset into image (in bytes).  
                        If the size of pinfo is 3x1, then the volume is assumed  
                        to be contiguous and each plane has the same scalefactor  
                        and offset.  
       __________________________________________________________________________  
         
        The fields listed above are essential for the mex routines, but other  
        fields can also be incorporated into the structure.  
         
        Note that spm_vol can also be applied to the filename(s) of 4-dim  
        volumes. In that case, the elements of V will point to a series of 3-dim  
        images.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_vol.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_vol", *args, **kwargs)
