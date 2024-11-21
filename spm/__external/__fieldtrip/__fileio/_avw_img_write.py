from spm.__wrapper__ import Runtime


def _avw_img_write(*args, **kwargs):
    """
      avw_img_write - write Analyze image files (*.img)  
         
        avw_img_write(avw,fileprefix,[IMGorient],[machine],[verbose])  
         
        avw.img    - a 3D matrix of image data (double precision).  
        avw.hdr    - a struct with image data parameters.  If  
                     not empty, this function calls avw_hdr_write.  
         
        fileprefix - a string, the filename without the .img  
                     extension. If empty, may use avw.fileprefix  
         
        IMGorient - optional int, force writing of specified  
                    orientation, with values:  
         
          [],  if empty, will use avw.hdr.hist.orient field  
           0,  transverse/axial unflipped (default, radiological)  
           1,  coronal unflipped  
           2,  sagittal unflipped  
           3,  transverse/axial flipped, left to right  
           4,  coronal flipped, anterior to posterior  
           5,  sagittal flipped, superior to inferior  
         
        This function will set avw.hdr.hist.orient and write the  
        image data in a corresponding order.  This function is  
        in alpha development, so it has not been exhaustively  
        tested (07/2003). See avw_img_read for more information  
        and documentation on the orientation option.  
        Orientations 3-5 are NOT recommended!  They are part  
        of the Analyze format, but only used in Analyze  
        for faster raster graphics during movies.  
         
        machine - a string, see machineformat in fread for details.  
                  The default here is 'ieee-le'.  
         
        verbose - the default is to output processing information to the command  
                  window.  If verbose = 0, this will not happen.  
         
        Tip: to change the data type, set avw.hdr.dime.datatype to:  
         
            1    Binary             (  1 bit  per voxel)  
            2    Unsigned character (  8 bits per voxel)  
            4    Signed short       ( 16 bits per voxel)  
            8    Signed integer     ( 32 bits per voxel)  
           16    Floating point     ( 32 bits per voxel)  
           32    Complex, 2 floats  ( 64 bits per voxel), not supported  
           64    Double precision   ( 64 bits per voxel)  
          128    Red-Green-Blue     (128 bits per voxel), not supported  
         
        See also: avw_write, avw_hdr_write,  
                  avw_read, avw_hdr_read, avw_img_read, avw_view  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/avw_img_write.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("avw_img_write", *args, **kwargs, nargout=0)
