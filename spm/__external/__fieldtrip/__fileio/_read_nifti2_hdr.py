from spm.__wrapper__ import Runtime


def _read_nifti2_hdr(*args, **kwargs):
    """
      READ_NIFTI2_HDR  
         
        Use as  
          [hdr] = read_nifti2_hdr(filename)  
        where  
          filename   = string  
            
        This implements the format as described at  
          http://www.nitrc.org/forum/forum.php?thread_id=2148&forum_id=1941  
         
        Please note that it is different from the suggested format described here  
          http://www.nitrc.org/forum/forum.php?thread_id=2070&forum_id=1941  
        and  
          https://mail.nmr.mgh.harvard.edu/pipermail//freesurfer/2011-February/017482.html  
        Notably, the unused fields have been removed and the size has been  
        reduced from 560 to 540 bytes.  
         
        See also WRITE_NIFTI_HDR, READ_CIFTI, WRITE_CIFTI  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_nifti2_hdr.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_nifti2_hdr", *args, **kwargs)
