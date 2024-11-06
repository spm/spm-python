from spm.__wrapper__ import Runtime


def spm_transverse(*args, **kwargs):
    """
      Rendering of regional effects [SPM{T/F}] on transverse sections  
        FORMAT spm_transverse('set',SPM,hReg)  
        FORMAT spm_transverse('setcoords',xyzmm)  
        FORMAT spm_transverse('clear')  
         
        SPM    - structure containing SPM, distribution & filtering details  
                 about the excursion set (xSPM)  
               - required fields are:  
        .Z     - minimum of n Statistics {filtered on u and k}  
        .STAT  - distribution {Z, T, X or F}       
        .u     - height threshold  
        .XYZ   - location of voxels {voxel coords}  
        .iM    - mm  -> voxels matrix  
        .VOX   - voxel dimensions {mm}  
        .DIM   - image dimensions {voxels}  
         
        hReg   - handle of MIP XYZ registry object (see spm_XYZreg for details)  
         
        spm_transverse automatically updates its coordinates from the  
        registry, but clicking on the slices has no effect on the registry.  
        i.e., the updating is one way only.  
         
        See also: spm_getSPM  
       __________________________________________________________________________  
         
        spm_transverse is called by the SPM results section and uses  
        variables in SPM and SPM to create three transverse sections though a  
        background image.  Regional foci from the selected SPM{T/F} are  
        rendered on this image.  
         
        Although the SPM{.} adopts the neurological convention (left = left)  
        the rendered images follow the same convention as the original data.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_transverse.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_transverse", *args, **kwargs, nargout=0)
