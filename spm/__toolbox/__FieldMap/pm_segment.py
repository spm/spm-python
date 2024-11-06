from spm.__wrapper__ import Runtime


def pm_segment(*args, **kwargs):
    """
      Segment an MR image into Gray, White & CSF.  
         
        FORMAT VO = pm_segment(PF,PG,flags)  
        PF    - name(s) of image(s) to segment (must have same dimensions).  
        PG    - name(s) of template image(s) for realignment.  
              - or a 4x4 transformation matrix which maps from the image to  
                the set of templates.  
        flags - a structure normally based on defaults.segment  
        VO    - optional output volume  
        M     - affine transformation between template and image to segment  
         
                             The algorithm is four step:  
         
        1) Determine the affine transform which best matches the image with a  
           template image. If the name of more than one image is passed, then  
           the first image is used in this step. This step is not performed if  
           no template images are specified.  
         
        2) Perform Cluster Analysis with a modified Mixture Model and a-priori  
           information about the likelihoods of each voxel being one of a  
           number of different tissue types. If more than one image is passed,  
           then they they are all assumed to be in register, and the voxel  
           values are fitted to multi-normal distributions.  
         
        3) Perform morphometric operations on the grey and white partitions  
           in order to more accurately identify brain tissue. This is then used  
           to clean up the grey and white matter segments.   
         
        4) If no or 2 output arguments is/are specified, then the segmented   
           images are written to disk. The names of these images have "c1",   
           "c2" & "c3" appended to the name of the first image passed. The   
           'brainmask' is also created with "BrMsk_" as an appendix.  
         
       _______________________________________________________________________  
        Refs:  
         
        Ashburner J & Friston KJ (1997) Multimodal Image Coregistration and  
        Partitioning - a Unified Framework. NeuroImage 6:209-217  
         
       _______________________________________________________________________  
         
        The template image, and a-priori likelihood images are modified  
        versions of those kindly supplied by Alan Evans, MNI, Canada  
        (ICBM, NIH P-20 project, Principal Investigator John Mazziotta).  
       _______________________________________________________________________  
          
        This is a renamed version of the original spm_segment which has been  
        removed from the main spm distribution, but copied into the FieldMap  
        toolbox where it is still used.  
       _______________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/FieldMap/pm_segment.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("pm_segment", *args, **kwargs)
