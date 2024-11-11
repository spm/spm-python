from spm.__wrapper__ import Runtime


def spm_dicom_header(*args, **kwargs):
    """
      Read header information from a DICOM file  
        FORMAT Header = spm_dicom_header(DicomFilename, DicomDictionary, Options)  
        DicomFilename   - DICOM filename  
        DicomDictionary - DICOM dictionary (see spm_dicom_headers)  
        Options         - an (optional) structure containing fields  
                          abort      - if this is a function handle, it will  
                                       be called with field name and value  
                                       arguments.  If this function returns true,  
                                       then reading the header will be aborted.  
                                       [Default: false]  
                          all_fields - binary true/false, indicating what to do  
                                       with fields that are not included in the  
                                       DICOM dictionary.  
                                       [Default: true]  
         
        Header          - Contents of DICOM header  
         
        Contents of headers are approximately explained in:  
        http://medical.nema.org/standard.html  
         
        This code may not work for all cases of DICOM data, as DICOM is an  
        extremely complicated "standard".  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dicom_header.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dicom_header", *args, **kwargs)
