from spm.__wrapper__ import Runtime


def DATA_COVID_US(*args, **kwargs):
    """
      Data retrieval function for COVID modelling  
        FORMAT [Y,Data] = DATA_COVID_US  
         
        Y(:,i,1) = Data(i).death;  
        Y(:,i,2) = Data(i).cases;  
         
        This auxiliary routine retrieves data from comma separated data files  
        that can be downloaded from:  
        https://github.com/CSSEGISandData/COVID-19/  
         
            time_series_covid19_confirmed_US.csv  
            time_series_covid19_deaths_US.csv  
         
        Data(k).state   - State  
        Data(k).pop     - population size  
        Data(k).lat     - latitude  
        Data(k).long    - longitude  
        Data(k).date    - date of 8th day  
        Data(k).cases   - number of cases  
        Data(k).death   - number of deaths  
        Data(k).cum     - cumulative number of deaths  
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DATA_COVID_US.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DATA_COVID_US", *args, **kwargs)
