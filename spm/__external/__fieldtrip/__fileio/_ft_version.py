from spm.__wrapper__ import Runtime


def _ft_version(*args, **kwargs):
    """
      FT_VERSION returns the version of FieldTrip and the path where it is installed  
         
        FieldTrip is not released with version numbers as "2.0", "2.1", etc. Instead, we  
        share our development version on http://github.com/fieldtrip/fieldtrip. You can use  
        git to make a local clone of the development version. Furthermore, we make  
        more-or-less daily releases of the code available on  
        https://github.com/fieldtrip/fieldtrip/releases and as zip file on our FTP server.  
         
        If you use git with the development version, the version is labeled with the hash  
        of the latest commit like "128c693". You can access the specific version "XXXXXX"  
        at https://github.com/fieldtrip/fieldtrip/commit/XXXXXX.  
         
        If you download the daily released version from our FTP server, the version is part  
        of the file name "fieldtrip-YYYYMMDD.zip", where YYY, MM and DD correspond to year,  
        month and day.  
         
        Use as  
          ft_version  
        to display the latest revision number on screen, or  
          [ftver, ftpath] = ft_version  
        to get the version and the installation root directory.  
         
        When using git with the development version, you can also get additional information with  
          ft_version revision  
          ft_version branch  
          ft_version clean  
         
        On macOS you might have installed git along with Xcode instead of with homebrew,  
        which then requires that you agree to the Apple license. In that case it can  
        happen that this function stops, as in the background (invisible to you) it is  
        asking whether you agree. You can check this by typing "/usr/bin/git", which will  
        show the normal help message, or which will mention the license agreement. To  
        resolve this please open a terminal and type "sudo xcodebuild -license"  
         
        See also FT_PLATFORM_SUPPORTS, VERSION, VER, VERLESSTHAN  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/ft_version.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_version", *args, **kwargs)
