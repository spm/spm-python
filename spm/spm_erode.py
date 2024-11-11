from spm.__wrapper__ import Runtime


def spm_erode(*args, **kwargs):
    """
      Perform an erosion on an image (2D or 3D)  
        FORMAT ima = spm_erode(ima)  
        FORMAT ima = spm_erode(ima,kernel)  
         
        Input:  
        ima    : 2 or 3D image  
        kernel : (Optional) voxel values in ima are replaced by the   
                 minimum value in a neighbourhood defined by kernel.  
                 The "standard" erosion operation (in 2D) is realised  
                 using the kernel  
                 0 1 0  
                 1 1 1  
                 0 1 0  
         
        Output:  
        ima    : Eroded image.  
         
        The functionality of this routine has been modelled on the function  
        imerode from the MATLAB Image processing toolbox. It doesn't (yet) have a  
        support function such as strel to help the user to define kernels (you  
        have to do it yourself if you want anything above 6-connectivty) and it  
        doesn't do the clever structuring element decomposition that strel does  
        (and imdilate uses). That should in principle mean that spm_erode is  
        slower than imerode, but at least for small (typical) kernels it is  
        actually more than twice as fast.  
        The actual job is done by spm_dilate_erode.c that serves both  
        spm_dilate.m and spm_erode.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_erode.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_erode", *args, **kwargs)
