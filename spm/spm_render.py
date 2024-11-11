from spm.__wrapper__ import Runtime


def spm_render(*args, **kwargs):
    """
      Render blobs on surface of a 'standard' brain  
        FORMAT spm_render(dat,brt,rendfile)  
         
        dat      - a struct array of length 1 to 3  
                   each element is a structure containing:  
                   - XYZ - the x, y & z coordinates of the transformed SPM{.}  
                           values in units of voxels.  
                   - t   - the SPM{.} values.  
                   - mat - affine matrix mapping from XYZ voxels to MNI.  
                   - dim - dimensions of volume from which XYZ is drawn.  
        brt      - brightness control:  
                   If NaN, then displays using the old style with hot  
                   metal for the blobs, and grey for the brain.  
                   Otherwise, it is used as a ``gamma correction'' to  
                   optionally brighten the blobs up a little.  
        rendfile - the file containing the images to render on to (see also  
                   spm_surf.m) or a surface mesh file.  
         
        Without arguments, spm_render acts as its own UI.  
       __________________________________________________________________________  
          
        spm_render prompts for details of up to three SPM{.}s that are then  
        displayed superimposed on the surface of a 'standard' brain.  
         
        The first is shown in red, then green then blue.  
         
        The blobs which are displayed are the integral of all transformed t  
        values, exponentially decayed according to their depth. Voxels that  
        are 10mm behind the surface have half the intensity of ones at the  
        surface.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_render.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_render", *args, **kwargs)
