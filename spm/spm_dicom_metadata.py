from spm.__wrapper__ import Runtime


def spm_dicom_metadata(*args, **kwargs):
    """
      Export image metadata as side-car JSON file  
        FORMAT N = spm_dicom_metadata(N,hdr)  
        N(input)  - nifti object  
        hdr       - a single header from spm_dicom_headers  
        N(output) - unchanged nifti object (for potential future use)  
         
        This function creates JSON-encoded metadata during DICOM to NIfTI  
        conversion, including all acquisition parameters, and saves them as a  
        JSON side-car file.  
         
        See also: spm_dicom_convert  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dicom_metadata.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dicom_metadata", *args, **kwargs)
