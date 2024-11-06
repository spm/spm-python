from spm.__wrapper__ import Runtime


def spm_platform(*args, **kwargs):
    """
      Platform specific configuration parameters  
         
        FORMAT ans = spm_platform(param)  
        param - optional string argument, can be  
                - 'bigend'  - return whether this architecture is big endian  
                              - false  - is little endian  
                              - true   - is big endian  
                - 'mexext'  - return MEX filename extension  
                - 'soext'   - return shared library filename extension  
                - 'user'    - return username  
                - 'host'    - return system's host name  
                - 'tempdir' - return name of temp directory  
                - 'desktop' - return whether or not the Desktop is in use  
         
        FORMAT PlatFontNames = spm_platform('fonts')  
        Return structure with fields named after the generic (UNIX) fonts, the  
        field containing the name of the platform specific font.  
         
        FORMAT PlatFontName = spm_platform('font',GenFontName)  
        Map generic (UNIX) FontNames to platform specific FontNames  
         
        FORMAT meminfo = spm_platform('memory',['available','total'])  
        Return memory information concerning the amount of available physical  
        memory or the total amount of physical memory.  
         
        FORMAT PLATFORM = spm_platform  
        Initialise platform specific parameters in persistent variable.  
        PLATFORM - copy of persistent variable containing platform specific  
        parameters.  
         
        FORMAT PLATFORM = spm_platform('init')  
        (Re)initialise platform specific parameters in persistent variable.  
         
       --------------------------------------------------------------------------  
        Since calls to spm_platform will be made frequently, most platform  
        specific parameters are stored in a persistent variable.  
        Subsequent calls use the information from this persistent variable, if  
        it exists.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_platform.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_platform", *args, **kwargs)
