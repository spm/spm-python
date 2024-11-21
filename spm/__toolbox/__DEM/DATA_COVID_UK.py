from spm.__wrapper__ import Runtime


def DATA_COVID_UK(*args, **kwargs):
    """
      Data retrieval function for COVID modelling (UK)  
        FORMAT [Y,R] = DATA_COVID_UK(country)  
         
        Y  - daily deaths and confirmed cases  
        R  - daily test rates for the UK  
         
        country - optional country  
         
        This auxiliary routine retrieves data from comma separated data files  
        that can be downloaded from:  
        https://github.com/CSSEGISandData/COVID-19/  
        https://github.com/tomwhite/covid-19-uk-data  
         
            time_series_covid19_confirmed_global.csv  
            time_series_covid19_deaths_global.csv  
            time_series_covid19_recovered_global.csv  
            covid-19-tests-uk  
         
        It augments these data with population sizes from the United Nations,  
        returning the following data structure:  
         
        Data(k).country - country  
        Data(k).pop     - population size  
        Data(k).lat     - latitude  
        Data(k).long    - longitude  
        Data(k).date    - date when more than one case was reported  
        Data(k).cases   - number of cases,  from eight days prior to first cases  
        Data(k).death   - number of deaths, from eight days prior to first cases  
        Data(k).recov   - number recovered, from eight days prior to first cases  
        Data(k).days    - number of days in timeseries  
        Data(k).cum     - cumulative number of deaths  
         
        Population data from (cite as):  
        United Nations, Department of Economic and Social Affairs, Population  
        Division (2019). World Population Prospects 2019, Online Edition. Rev. 1.  
         
        Please see the main body of the script for a description of the graphical  
        outputs provided when the routine is called with at an output argument.  
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DATA_COVID_UK.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DATA_COVID_UK", *args, **kwargs)
