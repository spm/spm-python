from spm.__wrapper__ import Runtime


def spm_write_filtered(*args, **kwargs):
    """
      Write the filtered SPM as an image  
        FORMAT Vo = spm_write_filtered(Z,XYZ,DIM,M,descrip,F)  
        Z         - {1 x ?} vector point list of SPM values for MIP  
        XYZ       - {3 x ?} matrix of coordinates of points (voxel coordinates)  
        DIM       - image dimensions {voxels}  
        M         - voxels -> mm matrix [default: spm_matrix(-(DIM+1)/2)]  
        descrip   - description string [default: 'SPM-filtered']  
        F         - output file's basename [default: user query]  
         
        FORMAT V0 = spm_write_filtered(xSPM)  
        xSPM      - SPM results structure from spm_getSPM  
         
        Vo        - output image volume information  
       __________________________________________________________________________  
         
        spm_write_filtered takes a pointlist image (parallel matrices of  
        coordinates and voxel intensities), and writes it out into an image  
        file.  
         
        It is intended for writing out filtered SPM's from the results section  
        of SPM, but can be used freestanding.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_write_filtered.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_write_filtered", *args, **kwargs)
