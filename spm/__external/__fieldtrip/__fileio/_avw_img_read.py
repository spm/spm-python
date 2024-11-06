from spm.__wrapper__ import Runtime


def _avw_img_read(*args, **kwargs):
    """
      avw_img_read - read Analyze format data image (*.img)  
         
        [ avw, machine ] = avw_img_read(fileprefix,[orient],[machine],[verbose])  
         
        fileprefix - a string, the filename without the .img extension  
         
        orient - read a specified orientation, integer values:  
         
                 '', use header history orient field  
                 0,  transverse unflipped (LAS*)  
                 1,  coronal unflipped (LA*S)  
                 2,  sagittal unflipped (L*AS)  
                 3,  transverse flipped (LPS*)  
                 4,  coronal flipped (LA*I)  
                 5,  sagittal flipped (L*AI)  
         
        where * follows the slice dimension and letters indicate +XYZ  
        orientations (L left, R right, A anterior, P posterior,  
        I inferior, & S superior).  
         
        Some files may contain data in the 3-5 orientations, but this  
        is unlikely. For more information about orientation, see the  
        documentation at the end of this .m file.  See also the  
        AVW_FLIP function for orthogonal reorientation.  
         
        machine - a string, see machineformat in fread for details.  
                  The default here is 'ieee-le' but the routine  
                  will automatically switch between little and big  
                  endian to read any such Analyze header.  It  
                  reports the appropriate machine format and can  
                  return the machine value.  
         
        verbose - the default is to output processing information to the command  
                  window.  If verbose = 0, this will not happen.  
         
        Returned values:  
         
        avw.hdr - a struct with image data parameters.  
        avw.img - a 3D matrix of image data (double precision).  
         
        A returned 3D matrix will correspond with the  
        default ANALYZE coordinate system, which  
        is Left-handed:  
         
        X-Y plane is Transverse  
        X-Z plane is Coronal  
        Y-Z plane is Sagittal  
         
        X axis runs from patient right (low X) to patient Left (high X)  
        Y axis runs from posterior (low Y) to Anterior (high Y)  
        Z axis runs from inferior (low Z) to Superior (high Z)  
         
        The function can read a 4D Analyze volume, but only if it is in the  
        axial unflipped orientation.  
         
        See also: avw_hdr_read (called by this function),  
                  avw_view, avw_write, avw_img_write, avw_flip  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/avw_img_read.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("avw_img_read", *args, **kwargs)
