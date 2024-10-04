from spm.__wrap__ import _Runtime


def spm_dicom_essentials(*args, **kwargs):
  """  Remove unused fields from DICOM header  
    FORMAT hdr1 = spm_dicom_essentials(hdr0)  
    hdr0 - original DICOM header  
    hdr1 - Stripped down DICOM header  
     
    With lots of DICOM files, the size of all the headers can become too  
    big for all the fields to be saved.  The idea here is to strip down  
    the headers to their essentials.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_dicom_essentials.m)
  """

  return _Runtime.call("spm_dicom_essentials", *args, **kwargs)
