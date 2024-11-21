from spm.__wrapper__ import Runtime


def fiff_read_coord_trans(*args, **kwargs):
    """
       
         usage: [trans_head2mri] = fiff_read_coord_trans(transfile)  
         
         input:  
              transfile = name of transformation fif file (usually stored in  
              the subject's Freesurfer directory in /mri/T1-neuromag/sets).  
         
         output:  
              trans_head2mri = transformation structure from head to MRI coordinate systems.  
         
                           Note: the inverse transformation, from MRI to head coordinate systems  
                                     can be obtained by just taking the inverse:  
                                          trans_mri2head.from=5; trans_mri2head.to=4;  
                                          trans_mri2head.trans=inv(trans_head2mri.trans);  
         
         author:  Rey Ramirez  email: rrramir@uw.edu  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_read_coord_trans.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fiff_read_coord_trans", *args, **kwargs)
