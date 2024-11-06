from spm.__wrapper__ import Runtime


def spm_orientations(*args, **kwargs):
    """
      Show the orientations that SPM assumes that the data are  
        stored in.  Standard Analyze format axial images will  
        normally be reported as 'RPI   Left-handed'.  Some people  
        will represent their axial images as Right-handed.  
        'RPI' means that the fastest changing direction (i.e.  
        the first element of the voxel coordinate) in the  
        file is Right->left, the middle (second element of  
        voxel coordinate) is Posterior->anterior and the  
        slowest (third element - indicating slice number) is  
        Inferior->superior.  
         
        One thing to watch out for is the image orientation. The  
        proper Analyze format uses a left-handed coordinate system,  
        whereas Talairach uses a right-handed one. In SPM99, images  
        were flipped at the spatial normalisation stage (from one  
        coordinate system to the other). In SPM2, a different  
        approach is used, so that either a left- or right-handed  
        coordinate system is used throughout. The SPM2 program is  
        told about the handedness that the images are stored with by  
        the spm_flip_analyze_images.m function and the  
        defaults.analyze.flip parameter that is specified in the  
        spm_defaults.m file. These files are intended to be  
        customised for each site. If you previously used SPM99 and  
        your images were flipped during spatial normalisation, then  
        set defaults.analyze.flip=1. If no flipping took place, then  
        set defaults.analyze.flip=0.  
         
        Check that when using the Display facility (possibly after  
        specifying some rigid-body rotations) that:  
         
            * The top-left image is coronal with the top (superior)  
              of the head displayed at the top and the left shown on  
              the left. This is as if the subject is viewed from  
              behind.  
         
            * The bottom-left image is axial with the front  
              (anterior) of the head at the top and the left shown  
              on the left. This is as if the subject is viewed from  
              above.  
         
            * The top-right image is sagittal with the front  
              (anterior) of the head at the left and the top of the  
              head shown at the top. This is as if the subject is  
              viewed from the left.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_orientations.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_orientations", *args, **kwargs, nargout=0)
