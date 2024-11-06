from spm.__wrapper__ import Runtime


def _align_ijk2xyz(*args, **kwargs):
    """
      ALIGN_IJK2XYZ flips and permutes the 3D volume data such that the axes of  
        the voxel indices and the headcoordinates approximately correspond. The  
        homogeneous transformation matrix is modified accordingly, to ensure that  
        the headcoordinates of each individual voxel do not change. The intention  
        is to create a volume structure that has a transform matrix which is  
        approximately diagonal in the rotation part.  
         
        First, the volume is permuted in order to get the largest (absolute)  
        values on the diagonal of the transformation matrix. This permutation is  
        reflected by the second output argument.  
         
        Second, the volumes are flipped along the dimensions for which the main  
        diagonal elements of the transformation matrix are negative. This is  
        reflected by the third output argument.  
         
        The second and third argument returned to allow you to reverse the operation.   
        Note that first the data have to be 'unflipped', and then 'unpermuted' (using   
        ipermute, rather than permute).  
         
        See also ALIGN_XYZ2IJK, VOLUMEPERMUTE, VOLUMEFLIP  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/align_ijk2xyz.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("align_ijk2xyz", *args, **kwargs)
