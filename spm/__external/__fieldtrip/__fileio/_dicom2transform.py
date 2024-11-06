from spm.__wrapper__ import Runtime


def _dicom2transform(*args, **kwargs):
    """
      DICOM2TRANSFORM converts the DICOM header parameters into a 4x4 homogenous  
        transformation matrix that maps voxel indices to the Patient Coordinate System.  
        Note that voxel indices are to be counted starting from 1 (MATLAB and Fortran  
        convention, not C/C++ and Python convention). This implementation is known to  
        result in a different transformation than FreeSurfer, but corresponds to Horos.  
         
        Use as  
          M = dicom2transform(dcmheader)  
        where the input argument dcmheader is a structure array with header information for  
        each slice. The first structure in the DICOM header array must correspond to slice  
        1 and the last one to slice N.  
         
        The header structure for each of the slices must contain  
          dcmheader(i).ImagePositionPatient  
          dcmheader(i).ImageOrientationPatient  
         
        The output argument M is a 4x4 homogenous transformation matrix that maps voxel  
        indices onto PCS world coordinates in millimeter.  
         
        Here are some usefull DICOM references  
          https://doi.org/10.1016/j.jneumeth.2016.03.001  
          https://dicom.innolitics.com/ciods/mr-image/image-plane/00200032  
          https://horosproject.org  
         
        See also DCMINFO, LOAD_DICOM_SERIES  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/dicom2transform.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("dicom2transform", *args, **kwargs)
