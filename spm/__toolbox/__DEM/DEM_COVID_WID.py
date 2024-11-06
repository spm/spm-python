from spm.__wrapper__ import Runtime


def DEM_COVID_WID(*args, **kwargs):
    """
      FORMAT DCM = DEM_COVID_WID  
         
        Demonstration of COVID-19 modelling using variational Laplace  
       __________________________________________________________________________  
         
        This routine addresses the global factors that underwrite mortality and  
        morbidity (and economic cost) by comparing different countries in terms  
        of the epidemiological and sociobehavioural parameters that best explain  
        the trajectory of daily cases and deaths. a subset of countries with a  
        large population and a low vaccination rate are modelled by optimising a  
        subset of country specific (free) parameters that capture differences in  
        exposure to the virus and subsequent responses; in terms of quarantine,  
        containment, resistance to infection and so on. The remaining model  
        parameters are assumed to be conserved over countries and are based on  
        posterior estimates derived from comprehensive timeseries data from the  
        United Kingdom. The between country analyses are based upon available  
        timeseries from Our World in Data  
         
        The predictive validity of this modelling is established in terms of the  
        accuracy of long-term forecasting up to 6 months - in countries that are  
        modelled with sufficient accuracy (at least 50% variance in death rates   
        explained). A canonical correlation analysis is then used to establish  
        the key parameters or factors that account for differences in fatalities  
        over countries. Finally, the model is used to assess the impact of an  
        equable vaccination programme starting over the next month using scenario  
        modelling. This scenario modelling considers the impact of equable  
        vaccination on cumulative deaths and gross domestic product. The  
        conclusions are based upon a subset of countries accounting for over 50%  
        of the world's population.  
         
        Please see the annotations in this script for further details at each  
        section of the analysis.  
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_COVID_WID.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_COVID_WID", *args, **kwargs)
