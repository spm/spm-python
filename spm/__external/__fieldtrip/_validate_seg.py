from spm.__wrapper__ import Runtime


def _validate_seg(*args, **kwargs):
    """
      VALIDATE_SEG ensures that the segmentation represents tissue types in a cumulative than exclusive   
        manner.   
         
        Use as  
          [tissue1, tissue2, tissue3] = validate_segmentation(tissue1, tissue2, tissue3)  
        where the second two input (and output) arguments are optional. In case of more than one input   
        argument the tissue-types should follow eachother from inside towards outside (e.g. tissue1 = brain,  
        tissue2 = skull, tissue = scalp).   
         
        The output will consist of one or more boolean segmentations without empty spaces inside.   
        In such way, more than one tissue-types will be represented in an overlapping manner. If  
        the input is invalid and cannot be converted to overlapping segmentations, this function will give  
        an error.  
         
        This function makes use of functions from the MATLAB Signal Processing Toolbox.  
         
        See also TRIANGULATE_SEG, PREPARE_MESH_SEGMENTATION  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/validate_seg.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("validate_seg", *args, **kwargs)
