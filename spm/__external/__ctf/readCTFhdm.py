from spm.__wrapper__ import Runtime


def readCTFhdm(*args, **kwargs):
    """
       Version 1.1   19 April 2007 - Test date.  
                       21 March 2007.  Modified to read v6.0 .hdm files that have additional   
                                       fields in MultiSphere_Data  
         Reads a head model file and returns the contents as a structure.  The purpose is  
         to make localSpheres head models available in the MATLAB environment.  
         Head Model File format is a "Config Reader" file.  It is defined in document   
         "CTF MEG FIle Formats', PN900-0088.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/ctf/readCTFhdm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("readCTFhdm", *args, **kwargs)
