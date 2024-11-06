from spm.__wrapper__ import Runtime


def _read_asa_mri(*args, **kwargs):
    """
      READ_ASA_MRI reads an ASA format MRI file  
         
        Use as  
          [mri, seg, hdr] = read_asa_mri(filename)  
         
        The raw image data is returned, together with the position of the  
        external head markers in raw image coordinates.  
         
        In the ASA default PAN (pre-auricular/nasion) coordinate system  
          PointOnPositiveYAxis -> LPA  
          PointOnNegativeYAxis -> RPA  
          PointOnPositiveXAxis -> nasion  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_asa_mri.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_asa_mri", *args, **kwargs)
