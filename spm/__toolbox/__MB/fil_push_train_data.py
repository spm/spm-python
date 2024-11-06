from spm.__wrapper__ import Runtime


def fil_push_train_data(*args, **kwargs):
    """
      Generate ``modulated categorical data'' for fil training  
        FORMAT fil_push_train_data(dw, Mw, Niiy, Nii1)  
        dw   - image dimensions of output  
        Mw   - voxel-to-world mapping of output  
        Niiy - NIfTI data structure of deformations  
        Nii1 - NIfTI data structure of categorical image data to push  
               Note that the first dimension encodes the number of subjects  
               and the behaviour of the code depends on the second dimension.  
               * If the second dimension is 1, then the images are assumed  
                 to be categorical labels. The output is a pcat_blah.mat file  
                 containing a sparse matrix that encodes the pushed labels.  
                 warped labels.  
               * If the second dimension is greater than 1, then the images  
                 are assumed to encode segmentation probabilities. The output  
                 in this case is a 4D image file. Note that the total  
                 Number of categories is the number of dimensions + 1, accounting  
                 for an implicit background class.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MB/fil_push_train_data.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fil_push_train_data", *args, **kwargs, nargout=0)
