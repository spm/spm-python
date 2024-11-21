from spm.__wrapper__ import Runtime


def fil_train(*args, **kwargs):
    """
      Fit the patch-wise CCA-like model.  
        FORMAT model = fil_train(data,sett,model)  
        data  - a data structure encoding the images used, as well as the  
                amount of jitter etc.  
        sett  - a data structure encoding settings.  Fields used are (with suggested values):  
                K       - Number of components to use in the model             [it depends]  
                nit     - Number of inner iterations for updating mu, W & Z    [5]  
                nu0     - Wishart degrees of freedom: A ~ W(I v_0 \nu_0, nu_0) [2]  
                v0      - Wishart scale parameter:    A ~ W(I v_0 \nu_0, nu_0) [6.0]  
                d1      - Patch-size (currently same in all directions)        [4]  
                r       - search radius                                        [2 voxels]  
                sd      - Standard deviation of weights within search radius   [0.75 voxels]  
                nit0    - Outer iterations                                     [8]  
                matname - filename for saving model                            [a string]  
                workers - Number of workers in parfor                          [it depends]  
        model - the estimated model  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MB/fil_train.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fil_train", *args, **kwargs)
