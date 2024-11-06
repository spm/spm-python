from spm.__wrapper__ import Runtime


def fil_label(*args, **kwargs):
    """
      Label image(s)  
        FORMAT files = fil_label(fil,mbsett,mbdat,iterations,vsett_scale,odir,df,Mf)  
        fil         - a trained model (see fil_train) loaded with  
                          fil    = load('fil_blah.mat');  
        mbsett      - global parameters from mb toolbox registration  
        mbdat       - subject data from mb toolbox registration  
                          mb     = load('mb_blah.mat');  
                          mbsett = mb.sett;  
                          mbdat  = mb.dat;  
        iterations  - three elements containing  
                          Number of registration Gauss-Newton updates  
                          Number of outer iterations to update the latent vars  
                          Number of inner iterations to update the latent vars  
                      (defaults to [6 10 10])  
        vsett_scale - scaling of the regularisation, relative to what was used  
                      originally by the mb toolbox (defaults to 0.25)  
        odir        - output directory name (defaults to '.')  
        df          - dimensions of label image (optional)  
        Mf          - voxel-to-world matrix of label image (optional)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MB/fil_label.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fil_label", *args, **kwargs)
