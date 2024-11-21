from spm.__wrapper__ import Runtime


def spm_dilate(*args, **kwargs):
    """
      Perform a dilation on an image (2D or 3D)   
        FORMAT ima = spm_dilate(ima)  
        FORMAT ima = spm_dilate(ima,kernel)  
         
        Input:  
        ima    : 2 or 3D image  
        kernel : (Optional) voxel values in ima are replaced by the   
                 maximum value in a neighbourhood defined by kernel.  
                 The "standard" dilation operation (in 2D) is realised  
                 using the kernel:  
                 0 1 0  
                 1 1 1  
                 0 1 0  
         
        Output:  
        ima    : Dilated image.  
         
        The functionality of this routine has been modelled on the function  
        imdilate from the MATLAB Image processing toolbox. It doesn't (yet) have  
        a support function such as strel to help the user to define kernels (you  
        have to do it yourself if you want anything above 6-connectivty) and it  
        doesn't do the clever structuring element decomposition that strel does  
        (and imdilate uses). That should in principle mean that spm_dilate is  
        slower than imdilate, but at least for small (typical) kernels it is  
        actually more than twice as fast.  
        The actual job is done by spm_dilate_erode.c that serves both  
        spm_dilate.m and spm_erode.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dilate.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dilate", *args, **kwargs)
