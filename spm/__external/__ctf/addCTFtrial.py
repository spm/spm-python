from spm._runtime import Runtime


def addCTFtrial(*args, **kwargs):
    r"""
     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  
                                                                                       %  
          This program creates datasets that can be analyzed by CTF software.          %  
                                                                                       %  
          Datasets created by this program MUST NOT BE USED FOR CLINICAL APPLICATIONS. %  
                                                                                       %  
          Please do not redistribute it without permission from VSM MedTech Ltd.       %  
                                                                                       %  
       %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/ctf/addCTFtrial.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("addCTFtrial", *args, **kwargs)
