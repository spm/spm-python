from spm.__wrapper__ import Runtime


def _avw_hdr_read(*args, **kwargs):
    """
      avw_hdr_read - read Analyze format data header (*.hdr)  
         
        [ avw, machine ] = avw_hdr_read(fileprefix, [machine], [verbose])  
         
        fileprefix - string filename (without .hdr); the file name  
                     can be given as a full path or relative to the  
                     current directory.  
         
        machine - a string, see machineformat in fread for details.  
                  The default here is 'ieee-le' but the routine  
                  will automatically switch between little and big  
                  endian to read any such Analyze header.  It  
                  reports the appropriate machine format and can  
                  return the machine value.  
         
        avw.hdr - a struct, all fields returned from the header.  
                  For details, find a good description on the web  
                  or see the Analyze File Format pdf in the  
                  mri_toolbox doc folder or read this .m file.  
         
        verbose - the default is to output processing information to the command  
                  window.  If verbose = 0, this will not happen.  
         
        This function is called by avw_img_read  
         
        See also avw_hdr_write, avw_hdr_make, avw_view_hdr, avw_view  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/avw_hdr_read.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("avw_hdr_read", *args, **kwargs)
