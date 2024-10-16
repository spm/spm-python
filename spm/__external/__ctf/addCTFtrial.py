from spm.__wrapper__ import Runtime


def addCTFtrial(*args, **kwargs):
  """ %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  
                                                                                   %  
      This program creates datasets that can be analyzed by CTF software.          %  
                                                                                   %  
      Datasets created by this program MUST NOT BE USED FOR CLINICAL APPLICATIONS. %  
                                                                                   %  
      Please do not redistribute it without permission from VSM MedTech Ltd.       %  
                                                                                   %  
   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/ctf/addCTFtrial.m)
  """

  return Runtime.call("addCTFtrial", *args, **kwargs)
