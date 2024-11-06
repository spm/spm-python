from spm.__wrapper__ import Runtime


def spm_opm_read_lvm(*args, **kwargs):
    """
      Read LVM file  
        FORMAT [lbv] = spm_opm_read_lvm(S)  
          S               - input structure  
        Optional fields of S:  
          S.filename           - filepath to LVM file             -Default: no Default                        
          S.headerlength       - integer specifying how many      -Default: 23  
                                 lines of file are header  
          S.timeind            - integer specifying which         -Default: 1  
                                 column is time variable  
          S.decimalTriggerInds - Indices of trigger Channels      -Default: 74:81  
          S.binaryTriggerInds  - Indices of trigger Channels      -Default: []  
          S.trigThresh         - Value to threshold triggers at   -Default: Auto  
            
        Output: lbv - output Structure  
         Fields of lbv:  
          lbv.B                  - MEG data  
          lbv.Time               - Time variable  
          lbv.decimalTrigs       - Trigger Channels  
          lbv.binaryTrigs        - Trigger Channels  
          lbv.pinout             - pinout of lbv file(coming soon)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_opm_read_lvm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_opm_read_lvm", *args, **kwargs)
