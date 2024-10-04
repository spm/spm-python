from spm.__wrap__ import _Runtime


def spm_dicom_headers(*args, **kwargs):
  """  Read header information from DICOM files  
    FORMAT Headers = spm_dicom_headers(DicomFilenames [,Essentials])  
    DicomFilenames - array of filenames  
    Essentials     - if true, then only save the essential parts of the header  
     
    Headers        - cell array of headers, one element for each file.  
     
    Contents of headers are approximately explained in:  
    http://medical.nema.org/standard.html  
     
    This code may not work for all cases of DICOM data, as DICOM is an  
    extremely complicated "standard".  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_dicom_headers.m)
  """

  return _Runtime.call("spm_dicom_headers", *args, **kwargs)
